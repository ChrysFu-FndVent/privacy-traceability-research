"""Minimal hash-chain integrity demo; not the unpublished research prototype."""

from __future__ import annotations

import argparse
import hashlib
import json
from typing import Any


def canonical_json(value: dict[str, Any]) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()


def record_hash(previous_hash: str, payload: dict[str, Any]) -> str:
    material = previous_hash.encode() + b"\x00" + canonical_json(payload)
    return hashlib.sha256(material).hexdigest()


def append_record(chain: list[dict[str, Any]], payload: dict[str, Any]) -> None:
    previous_hash = chain[-1]["hash"] if chain else "GENESIS"
    chain.append(
        {
            "index": len(chain),
            "previous_hash": previous_hash,
            "payload": payload,
            "hash": record_hash(previous_hash, payload),
        }
    )


def verify_chain(chain: list[dict[str, Any]]) -> tuple[bool, int | None]:
    previous_hash = "GENESIS"
    for index, record in enumerate(chain):
        expected = record_hash(previous_hash, record["payload"])
        if record.get("index") != index or record.get("previous_hash") != previous_hash or record.get("hash") != expected:
            return False, index
        previous_hash = record["hash"]
    return True, None


def build_demo_chain() -> list[dict[str, Any]]:
    chain: list[dict[str, Any]] = []
    append_record(chain, {"batch": "demo-001", "state": "registered"})
    append_record(chain, {"batch": "demo-001", "state": "verified"})
    return chain


def run_self_test() -> None:
    chain = build_demo_chain()
    assert verify_chain(chain) == (True, None)
    chain[0]["payload"]["state"] = "changed"
    assert verify_chain(chain) == (False, 0)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        run_self_test()
        print("self-test: ok")
        return

    chain = build_demo_chain()
    valid, failed_at = verify_chain(chain)
    print(json.dumps({"valid": valid, "failed_at": failed_at, "chain": chain}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
