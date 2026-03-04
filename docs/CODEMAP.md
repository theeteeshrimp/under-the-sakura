# Code Map (v0.2)

## Runtime variables
- `trust_mika`: relationship closeness
- `discipline`: execution consistency
- `clarity`: self-honesty
- `journal`: route log used in end recap
- `side_aoi_seen`, `side_rooftop_seen`: side-scene flags
- `festival_fight`: tracks confrontation outcome
- `route_focus`: early route intent marker

## Main flow
`start`
→ `chapter_1`
→ `chapter_2`
→ (`side_scene_aoi` optional)
→ `chapter_3`
→ `chapter_4`
→ (`side_scene_rooftop` optional)
→ `chapter_5`
→ `chapter_6`
→ `ending_router`
→ `ending_*`
→ `epilogue_week_later`
→ `credits_stub`

## End routing thresholds
- `ending_true_plus`: trust>=4, discipline>=3, clarity>=4
- `ending_true`: trust>=3, discipline>=2, clarity>=2
- `ending_functional`: discipline>=4 and trust>=0
- else `ending_distant`

## Extend points
- Add Act 3 labels before `ending_router` if expanding pacing.
- Add route-specific labels keyed by `route_focus`.
- Replace placeholder assets when image pipeline is unlocked.
