from dapp_testing.inspector import classify_rpc_response, inspect_transaction, verify_state_transition


def test_success_response_is_valid():
    report = classify_rpc_response({"jsonrpc": "2.0", "id": 1, "result": "0x1"})
    assert report == {"valid": True, "classification": "ok", "errors": []}


def test_rpc_error_is_classified():
    report = classify_rpc_response({"jsonrpc": "2.0", "id": 1, "error": {"code": -32602, "message": "Invalid params"}})
    assert report["valid"] is True
    assert report["classification"] == "invalid_params"


def test_invalid_envelope_is_rejected():
    report = classify_rpc_response({"jsonrpc": "1.0", "id": 2, "result": "0x1", "error": {}})
    assert report["valid"] is False
    assert len(report["errors"]) == 3


def test_transaction_fields_are_checked():
    report = inspect_transaction({"hash": "0x1", "from": "0x2", "value": "1"})
    assert "missing field: to" in report["errors"]
    assert "value must be a hex quantity" in report["errors"]


def test_state_transition_cannot_move_backwards_or_change_network():
    report = verify_state_transition({"block_number": 100, "chain_id": 1}, {"block_number": 99, "chain_id": 5})
    assert report["valid"] is False
    assert len(report["errors"]) == 2

