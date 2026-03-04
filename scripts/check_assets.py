#!/usr/bin/env python3
import json
import pathlib

root = pathlib.Path(__file__).resolve().parents[1]
prompts = json.loads((root / "game" / "prompts" / "cg_prompts.json").read_text())
missing = []
for p in prompts:
    path = root / p["output"]
    if not path.exists():
        missing.append(str(path))

if missing:
    print("Missing assets:")
    for m in missing:
        print(" -", m)
    raise SystemExit(1)
print("All assets present.")
