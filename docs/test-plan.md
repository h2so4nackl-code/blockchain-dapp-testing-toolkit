# Read-only dApp test plan

## Objective

Demonstrate repeatable verification of JSON-RPC availability, response envelopes, transaction shape, block progression, and network-error classification without signing or submitting a transaction.

## In scope

- Read-only JSON-RPC methods
- Request/response ID correlation
- Result versus error envelope validation
- Standard JSON-RPC error families
- Transaction field and hex-quantity inspection
- Chain ID stability and non-decreasing block observations
- Sanitized, reproducible JSON reports

## Out of scope

- Wallet connection, signing, seed phrases, private keys, mining accounts, or recovery files
- State-changing RPC methods
- Production credentials, private endpoints, or private IP addresses
- Proprietary chain or application protocols
- Claims about financial correctness or smart-contract security

## Example cases

| ID | Case | Expected |
| --- | --- | --- |
| RPC-001 | Valid `eth_blockNumber` fixture | Envelope and hex result accepted |
| RPC-002 | Request ID mismatch | Correlation failure reported |
| RPC-003 | Result and error both present | Malformed envelope reported |
| RPC-004 | Error code -32602 | Classified as `invalid_params` |
| TX-001 | Complete transaction fixture | Required fields and hex quantities accepted |
| STATE-001 | Later block on same chain | State progression accepted |
| STATE-002 | Block decreases | Possible stale/inconsistent provider reported |

