from __future__ import annotations

from typing import Any


READ_ONLY_METHODS = {"eth_chainId", "eth_blockNumber", "eth_getBalance", "eth_getTransactionByHash", "eth_getTransactionReceipt"}


def classify_rpc_response(response: Any, expected_id: int | str | None = 1) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(response, dict):
        return {"valid": False, "classification": "malformed_response", "errors": ["response must be an object"]}
    if response.get("jsonrpc") != "2.0":
        errors.append("jsonrpc must equal 2.0")
    if response.get("id") != expected_id:
        errors.append("response id does not match request id")
    has_result = "result" in response
    has_error = "error" in response
    if has_result == has_error:
        errors.append("response must contain exactly one of result or error")
    classification = "ok"
    if has_error and isinstance(response.get("error"), dict):
        code = response["error"].get("code")
        classification = {
            -32700: "parse_error",
            -32600: "invalid_request",
            -32601: "method_not_found",
            -32602: "invalid_params",
            -32603: "internal_error",
        }.get(code, "node_error")
    elif errors:
        classification = "malformed_response"
    return {"valid": not errors, "classification": classification, "errors": errors}


def inspect_transaction(tx: Any) -> dict[str, Any]:
    if tx is None:
        return {"found": False, "errors": ["transaction not found"]}
    if not isinstance(tx, dict):
        return {"found": True, "errors": ["transaction must be an object"]}
    errors: list[str] = []
    for field in ("hash", "from", "to", "value", "blockNumber"):
        if field not in tx:
            errors.append(f"missing field: {field}")
    for field in ("value", "blockNumber"):
        value = tx.get(field)
        if not isinstance(value, str) or not value.startswith("0x"):
            errors.append(f"{field} must be a hex quantity")
    return {"found": True, "errors": errors, "valid": not errors}


def verify_state_transition(before: dict[str, Any], after: dict[str, Any]) -> dict[str, Any]:
    before_block = before.get("block_number")
    after_block = after.get("block_number")
    errors: list[str] = []
    if not isinstance(before_block, int) or not isinstance(after_block, int):
        errors.append("block numbers must be integers")
    elif after_block < before_block:
        errors.append("block number moved backwards")
    if before.get("chain_id") != after.get("chain_id"):
        errors.append("chain id changed between observations")
    return {"valid": not errors, "errors": errors}

