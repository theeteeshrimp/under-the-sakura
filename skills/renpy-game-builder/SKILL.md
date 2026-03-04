---
name: renpy-game-builder
description: Build and iterate Ren'Py visual novels end-to-end with script writing, branching design, asset prompt packs, image generation pipelines, and git release workflow. Use when user asks to autonomously create or expand a visual novel project.
---

# Ren'Py Game Builder

## Workflow
1. Define chapter goal + endings.
2. Implement or update `game/script.rpy` with clear labels and variables.
3. Maintain `game/prompts/cg_prompts.json` for every CG/background.
4. Generate assets with `scripts/generate_cg.py`.
5. Verify assets via `scripts/check_assets.py`.
6. Commit and push with concise changelog.

## Rules
- Keep each scene visually mapped to one background/CG.
- Ensure at least one meaningful branch per chapter.
- Keep dialogue concise and emotional.
- Never hardcode API keys into repo files.
