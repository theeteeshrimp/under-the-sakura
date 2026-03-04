#!/usr/bin/env python3
import base64
import json
import os
import pathlib
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROMPTS_FILE = ROOT / "game" / "prompts" / "cg_prompts.json"

# Provider mode: gemini | openai
IMAGE_PROVIDER = os.getenv("IMAGE_PROVIDER", "openai").strip().lower()

# OpenAI-compatible settings (ImageRouter etc.)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.imagerouter.io/v1").strip().rstrip("/")
OPENAI_IMAGE_MODEL = os.getenv("OPENAI_IMAGE_MODEL", "black-forest-labs/FLUX-2-klein-4b").strip()

# Gemini settings (fallback)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
GEMINI_IMAGE_MODEL = os.getenv("GEMINI_IMAGE_MODEL", "gemini-2.5-flash-image").strip()


def call_openai_compatible(prompt: str):
    if not OPENAI_API_KEY:
        raise RuntimeError("Missing OPENAI_API_KEY")
    url = f"{OPENAI_BASE_URL}/images/generations"
    payload = {
        "model": OPENAI_IMAGE_MODEL,
        "prompt": prompt,
        "size": "1280x720"
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}",
        },
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        resp = json.loads(r.read().decode("utf-8"))

    # OpenAI-style responses
    item = (resp.get("data") or [{}])[0]
    b64 = item.get("b64_json")
    if b64:
        return base64.b64decode(b64)

    # URL fallback
    url = item.get("url")
    if url:
        req2 = urllib.request.Request(url, method="GET")
        with urllib.request.urlopen(req2, timeout=120) as r2:
            return r2.read()

    raise RuntimeError(f"No image data in OpenAI-compatible response: {json.dumps(resp)[:400]}")


def call_gemini(prompt: str):
    if not GEMINI_API_KEY:
        raise RuntimeError("Missing GEMINI_API_KEY")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_IMAGE_MODEL}:generateContent?key={GEMINI_API_KEY}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]},
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST", headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.loads(r.read().decode("utf-8"))


def extract_gemini_image_bytes(resp: dict):
    for cand in resp.get("candidates", []):
        content = cand.get("content", {})
        for part in content.get("parts", []):
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and inline.get("data"):
                return base64.b64decode(inline["data"])
    raise RuntimeError(f"No image data in Gemini response: {json.dumps(resp)[:300]}")


def main():
    prompts = json.loads(PROMPTS_FILE.read_text())
    ok, fail = 0, 0
    for item in prompts:
        out_path = ROOT / item["output"]
        out_path.parent.mkdir(parents=True, exist_ok=True)
        print(f"[gen] {item['id']} -> {out_path}")
        try:
            if IMAGE_PROVIDER == "gemini":
                resp = call_gemini(item["prompt"])
                img = extract_gemini_image_bytes(resp)
            else:
                img = call_openai_compatible(item["prompt"])
            out_path.write_bytes(img)
            ok += 1
        except Exception as e:
            fail += 1
            print(f"  !! failed: {e}")
    print(f"done: ok={ok} fail={fail}")


if __name__ == "__main__":
    main()
