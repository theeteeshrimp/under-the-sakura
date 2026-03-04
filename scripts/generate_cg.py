#!/usr/bin/env python3
import base64
import json
import os
import pathlib
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROMPTS_FILE = ROOT / "game" / "prompts" / "cg_prompts.json"

API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
MODEL = os.getenv("GEMINI_IMAGE_MODEL", "gemini-2.5-flash-image").strip()


def call_gemini(prompt: str):
    if not API_KEY:
        raise RuntimeError("Missing GEMINI_API_KEY")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]}
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST", headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.loads(r.read().decode("utf-8"))


def extract_image_bytes(resp: dict):
    for cand in resp.get("candidates", []):
        content = cand.get("content", {})
        for part in content.get("parts", []):
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and inline.get("data"):
                return base64.b64decode(inline["data"])
    raise RuntimeError(f"No image data in response: {json.dumps(resp)[:300]}")


def main():
    prompts = json.loads(PROMPTS_FILE.read_text())
    ok, fail = 0, 0
    for item in prompts:
        out_path = ROOT / item["output"]
        out_path.parent.mkdir(parents=True, exist_ok=True)
        print(f"[gen] {item['id']} -> {out_path}")
        try:
            resp = call_gemini(item["prompt"])
            img = extract_image_bytes(resp)
            out_path.write_bytes(img)
            ok += 1
        except Exception as e:
            fail += 1
            print(f"  !! failed: {e}")
    print(f"done: ok={ok} fail={fail}")


if __name__ == "__main__":
    main()
