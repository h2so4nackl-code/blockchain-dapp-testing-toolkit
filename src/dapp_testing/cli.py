import argparse
import json
from pathlib import Path

from .inspector import classify_rpc_response


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect a saved, sanitized JSON-RPC response")
    parser.add_argument("fixture", type=Path)
    args = parser.parse_args()
    response = json.loads(args.fixture.read_text(encoding="utf-8"))
    report = classify_rpc_response(response)
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["valid"] else 1)


if __name__ == "__main__":
    main()

