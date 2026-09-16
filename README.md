# PyQuant-XQX · "Ancient-Meets-Modern" Cute & Fresh Photo Skill

> 中文版 / Chinese version: [README.zh-CN.md](README.zh-CN.md)

Drop mythological / classical-costume characters into **real, everyday modern life**
and shoot them with a Japanese "kawaii fresh" film aesthetic.
The contrast — a dignified figure earnestly doing the most ordinary little things —
naturally produces playfulness and charm. Wholesome and healing, never gimmicky.

> 🌸 Example: a classical-dressed girl in a waist-high reed field, holding wildflowers
> and an iced coffee; or a burly, bearded Bull Demon King totally absorbed in a claw
> machine, a pink plush bunny inside.

## Package layout

```
PyQuant-XQX.skill/
├── SKILL.md            # Full recipe: style definition / prompt template / workflow / pitfalls
├── README.md           # Chinese version
├── README_EN.md        # This file (English)
├── LICENSE             # Copyright notice
├── scripts/
│   └── photo_frame.py  # Photo-paper border + vertical caption + title (pure Pillow)
└── examples/           # 9 original sample images (01–09, five mood tiers)
```

## Quick start

1. Read `SKILL.md` for the prompt master template and the five-mood ammo library.
2. Prepare an **anchor photo where the face fills ≥1/4 of the frame** (crop face →
   square → upscale to 1024×1024).
3. Generate from the template (film grain is inherently random — produce 2–3 variants
   per prompt and pick the best).
4. Finally, run the script to add the photo-paper border and vertical caption
   (**text is always composited in post — AI-written text is guaranteed to be garbled**):

```bash
python scripts/photo_frame.py input.png output.png \
  --ratio 0.055 --crop-bottom 0.06 --bottom-extra 0.9 \
  --title-in-margin --halo 0.5 \
  --caption "風にゆれて" --caption2 "はるのいろ" --title "野原の 小さな幸せ"
```

Dependencies: Pillow only (`pip install pillow`), Python ≥ 3.9.

## Sample gallery (examples/, five moods)

| # | File | Tier | Scene |
|---|------|------|-------|
| 01 | 小清新_少女花田 | Fresh & airy | Reed field · wildflowers & iced coffee |
| 02 | 小清新_行者地铁 | Fresh & airy | Dawn subway · dozing against the pole |
| 03 | 小确幸_行者冰淇淋 | Tiny happiness | Convenience-store step · a satisfied bite |
| 04 | 小确幸_少女咖啡馆 | Tiny happiness | Café window seat · gazing at a latte |
| 05 | 俏皮_少女贩卖机 | Playful | Night vending machine · neon smirk |
| 06 | 俏皮_行者踩水 | Playful | Rain puddle · boot splash |
| 07 | 搞怪_莽汉洗衣店 | Goofy | Laundromat · stacked laundry on head |
| 08 | 搞怪_莽汉大西瓜 | Goofy | Roadside fruit stand · showing off a huge watermelon |
| 09 | 反差萌_牛魔王娃娃机 | Contrast-cute | Dead-serious at a claw machine |

## ⚖️ Copyright notice (important)

- **Copyright © 2026 (PyQuant)** — Douyin account "Quanty的隔壁工位".
- All documents, scripts and `examples/` sample images in this repo are original works
  by the author (AI-assisted generation; the creative process and recipe constitute this
  skill's content).
- **Please keep this notice and attribution.** Misattribution or unauthorized reposting
  is infringement.
- Free for personal study and practice; **commercial use requires prior authorization**.
- This package **contains no third-party image assets**; the stylistic method derives
  from observing publicly available content.
- Character designs in the samples are fictional artistic creations with no association
  to any real person or film/TV rights holder.

## License

Code & docs: [MIT](LICENSE) ｜ Sample images: © the author; reposting requires
attribution, commercial use requires authorization.
