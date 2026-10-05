# Blockchain / dApp Testing Toolkit

[![Tests](https://github.com/h2so4nackl-code/blockchain-dapp-testing-toolkit/actions/workflows/tests.yml/badge.svg)](https://github.com/h2so4nackl-code/blockchain-dapp-testing-toolkit/actions/workflows/tests.yml)

A read-only personal portfolio project for validating sanitized JSON-RPC responses, inspecting transaction fields, classifying network/node errors, and checking simple state progression.

The toolkit never signs, submits, recovers, or constructs transactions. It contains no private keys, seed phrases, wallet files, credentials, production endpoints, private IP addresses, mining accounts, or proprietary code.

## What it demonstrates

- JSON-RPC 2.0 envelope and request/response ID validation
- Separation of successful results from structured errors
- Standard parse, request, method, parameter, and internal-error classification
- Read-only transaction field and hex-quantity inspection
- Chain ID stability and non-decreasing block-state checks
- Reproducible tests and a sanitized machine-readable report

## Run locally

Create and activate the virtual environment before installing dependencies. On Windows PowerShell, use `.\.venv\Scripts\Activate.ps1` instead of `source .venv/bin/activate`.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest -q
dapp-check fixtures/rpc-success.json
```

All tests run against local fictional fixtures. No network connection is required.

## Evidence

- [`docs/test-plan.md`](docs/test-plan.md) defines scope, exclusions, and cases.
- [`fixtures/rpc-success.json`](fixtures/rpc-success.json) is a sanitized successful response.
- [`fixtures/transaction.json`](fixtures/transaction.json) uses obvious fictional addresses and a fictional hash.
- [`tests/test_inspector.py`](tests/test_inspector.py) covers positive and negative cases.
- [`reports/sample-report.json`](reports/sample-report.json) records a safe example outcome.

## Safety boundary

Only read-only methods belong in this project. `READ_ONLY_METHODS` documents the allowed examples. Wallet methods and transaction submission are intentionally absent; the `.gitignore` also blocks common key, wallet, recovery, and environment-file names.

## Limitations

- This is a QA demonstration, not a smart-contract audit or security certification.
- Fixtures model Ethereum-style JSON-RPC only and do not imply experience with a specific private network.
- Availability and latency of live providers are not benchmarked.

## Suggested GitHub description

Read-only JSON-RPC and dApp QA toolkit for health, error classification, transaction inspection, state checks, and reproducible reports.

## Suggested topics

`blockchain-testing`, `dapp`, `json-rpc`, `quality-assurance`, `software-testing`, `python`, `pytest`, `api-testing`

## License

MIT
