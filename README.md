# Under the Sakura 🌸

A Ren'Py visual novel built for agent-assisted production.

## Current state
- Playable prologue with branching endings
- Structured CG/background prompt pack
- Gemini image generation pipeline
- Placeholder images included so project boots immediately

## Project structure
- `game/script.rpy` — story + branching logic
- `game/prompts/cg_prompts.json` — all image prompts and output mapping
- `scripts/generate_cg.py` — generate backgrounds/CGs using Gemini image model
- `scripts/check_assets.py` — verify required assets exist
- `docs/ART_STYLE_GUIDE.md` — art direction

## Generate CGs
```bash
cp .env.example .env
# set GEMINI_API_KEY in env
set -a; source .env; set +a
python3 scripts/generate_cg.py
python3 scripts/check_assets.py
```

## Play
1. Open Ren'Py Launcher
2. Select this folder (`under-the-sakura`)
3. Launch Project

## Notes
If Gemini API quota is exceeded, generation may fail. Re-run once quota/billing is available.
