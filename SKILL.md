---
name: pyquant-xqx
title: PyQuant-XQX · 小清新萌萌哒「古装穿越现代」写真生成
version: 1.0.0
author: PY (PyQuant / 抖音「PyQuant的隔壁工位」)
language: zh-CN
tags: [AI生图, 小清新, 萌系, 古装穿越, 胶片写真, 图文创作, prompt-engineering]
---

# PyQuant-XQX · 小清新萌萌哒「古装穿越现代」写真

把神话/古装角色放进**真实的现代日常生活**里，用日系小清新的胶片质感拍出来——
威严的角色认真做着最平凡的小事，反差自然产生活泼与萌感，全程**治愈系**，不搞怪不恶搞。

一句话配方：**身份反差提供萌点 + 时代错置提供趣味 + 日系胶片质感提供高级感**。

## 一、风格定义：小清新萌萌哒

五个情绪档位（可混搭，一组系列图建议 3 档以上轮换）：

| 档位 | 情绪关键词 | 典型场景 |
|------|-----------|---------|
| 小清新 | 空气感、微风、暖阳 | 芒草花田捧野花、清晨地铁打盹 |
| 小确幸 | 小小的满足、一口幸福 | 便利店门口吃冰淇淋、咖啡馆窗边午后 |
| 俏皮 | 有点调皮、藏不住的坏笑 | 夜晚自动贩卖机前探头、雨后水洼踩水 |
| 搞怪 | 认真地干傻事、憨态 | 洗衣店头顶叠衣服、水果摊抱大西瓜炫耀 |
| 反差萌 | 极凶外表 × 极软内心 | 满脸横肉的大汉在娃娃机前全神贯注 |

**与"冷幽默 deadpan"路线的区别**：deadpan 靠面无表情制造荒诞；本风格靠**微表情与暖调**制造治愈——
嘴角轻扬、眼里有光、认真投入。两者都拒绝夸张大笑和挤眉弄眼。

## 二、视觉配方（关键词可直接进 prompt）

| 维度 | 配方 |
|------|------|
| 媒介质感 | `35mm film photograph, Kodak Portra 400, visible film grain, slight halation, printed photo with thin white border` |
| 光线 | `available natural light, warm golden hour backlight / soft overcast daylight, no studio lighting` |
| 镜头 | `50mm lens, f/1.8, shallow depth of field, candid snapshot` |
| 构图 | `medium / full shot, subject slightly off-center, generous negative space` |
| 色调 | 小清新档用 `airy warm gold and soft green, gentle pastel, low saturation`；夜景档用 `neon bokeh, warm-cool contrast` |
| 情绪 | `gently happy, softly smiling, completely absorbed, matter-of-fact - never goofy` |
| 文字 | `no text, no lettering`（文字一律后期用脚本叠加，AI 写字必乱码） |

NEGATIVE 固定底座：`3D render, CGI, plastic over-smoothed skin, studio backdrop, HDR oversaturation, distorted hands, extra fingers, garbled text, watermark, logo`

## 三、Prompt 主模板（中英混写）

```
[SHOT] 35mm film photograph, candid snapshot, printed photo with a thin white
border, visible film grain.
[SUBJECT] {角色}, {古装/神话造型细节: flowing pink-white hanfu with red sash /
furry dark beast-king robe with curved horns}, {微表情: softly smiling, eyes
gentle and warm / totally absorbed, brows slightly furrowed in concentration}.
[ACTION] {现代日常动作: holding a small bouquet of wildflowers / licking an
ice cream cone / jumping over a rain puddle}.
[PROP] {现代道具: iced coffee in a plastic cup / pink plush bunny in a claw
machine / stack of folded laundry balanced on the head}.
[SETTING] {真实生活场景: a sunlit reed field in early autumn / a quiet subway
car at dawn / a nighttime arcade glowing with neon}.
[LIGHT] available natural light, warm golden hour backlight, no studio lighting.
[COLOR] Kodak Portra 400 palette, airy warm gold and soft green, gentle pastel,
low saturation, gentle halation.
[FRAME] medium shot, 50mm lens, f/1.8, shallow depth of field, subject slightly
off-center, generous negative space.
[MOOD] gently happy and completely natural, quietly adorable - never goofy.
[TEXT] no text, no lettering.
NEGATIVE: 3D render, CGI, digital sheen, plastic over-smoothed skin, studio
backdrop, HDR oversaturation, distorted hands, extra fingers, garbled text,
watermark, logo.
```

### 实战示例（复原自实拍样图，见 examples/）

1. **小清新·少女花田** — 古装少女手捧野花+一杯冰咖啡，站在及腰的芒草花田里，逆光微笑。
2. **小清新·行者地铁** — 清晨地铁车厢，行者靠着扶杆打盹，晨光斜照。
3. **小确幸·行者冰淇淋** — 便利店门口台阶，行者咬一口冰淇淋，满足眯眼。
4. **小确幸·少女咖啡馆** — 午后咖啡馆窗边座位，少女与一杯拿铁对望。
5. **俏皮·少女贩卖机** — 夜晚自动贩卖机的霓虹光里，少女探头挑选，坏笑。
6. **俏皮·行者踩水** — 雨后湿漉漉的街道，行者穿着靴子跳进水洼，溅起水花。
7. **搞怪·莽汉洗衣店** — 自助洗衣店里，莽汉头顶叠起一摞叠好的衣物，一本正经。
8. **搞怪·莽汉大西瓜** — 乡间水果摊，莽汉双手抱超大西瓜，得意地咧嘴。
9. **反差萌·牛魔王娃娃机** — 游戏厅娃娃机前，满脸虬髯的牛魔王全神贯注摇杆，机内一只粉色兔子玩偶。

## 四、工作流（六步出货）

1. **备角色锚点图**：必须是**脸占画面 ≥1/4 的近景照片**（不是插画）。裁脸 → 方形化 → 放大到 1024×1024。
   远景小脸会让模型自造一张脸，角色必崩。
2. **定场景**：`{角色} + {现代日常行为} + {真实场景}`，一张图只讲一个梗。
3. **出试稿**：同一 prompt 出 2–3 张挑最好——胶片感自带随机性，多出容易出神图。
4. **脸不对就换脸保场景**：`image1`=正确脸部特写，`image2`=待修成图，prompt 先写
   `Keep this exact same photograph otherwise` + 要保住的要素，再写 `ONLY change the face...`；
   NEGATIVE 必加 `pasted-on face, visible seam`。
5. **质检**：把每张的脸部裁出来放大拼板复查（脸型/眉眼/眼睛开合/贴脸接缝/调色一致）。缩略图看不出脸的问题。
6. **裱框 + 注记**：用随附 `scripts/photo_frame.py` 叠加白相纸边框、右上竖排注记、右下标题（见下节）。
   最终对外发布导出 JPG（quality≈92，单张 ≤500KB，体积小加载快）。

## 五、photo_frame.py · 相纸边框 + 竖排注记

纯 Pillow 实现，无其他依赖（Python ≥3.9）。

```bash
python scripts/photo_frame.py 输入.png 输出.png \
  --ratio 0.055 --crop-bottom 0.06 --bottom-extra 0.9 \
  --title-in-margin --halo 0.5 \
  --caption "風にゆれて" --caption2 "はるのいろ" --title "野原の 小さな幸せ"
```

| 参数 | 说明 |
|------|------|
| `--ratio` | 相纸边框宽度（占原图宽度比例），0.055 ≈ 5.5% |
| `--crop-bottom` | 裱框前裁掉底部比例（去水印/杂物） |
| `--bottom-extra` | 底边额外加宽系数（给标题留位） |
| `--title-in-margin` | 标题放在底边白框内（右对齐） |
| `--caption/--caption2` | 右上角竖排注记两列（日文写真集风格） |
| `--halo` | 注记文字后白色柔光强度 0–1（保证在画面上可读） |
| `--font` | 手动指定 CJK 字体文件（默认自动探测：Yu Gothic / MS Gothic / Noto / 雅黑） |

> ⚠️ 同一系列所有图的注记风格、边框参数必须完全一致，成组看才不出戏。

## 六、避坑清单（每条都是真金白银试出来的）

- ✅ 表情写**可观察的肌肉动作**（嘴角轻扬 3 分、眼睛弯成月牙、眉毛放松），写情绪名词等于没写
- ✅ 道具具体到"有品牌感"的程度：不说"喝饮料"，说"透明塑料杯冰咖啡配绿色吸管"
- ✅ 场景必须是真实生活空间，无绿幕无仙侠棚
- ✅ 同系列锁定同一套 `[COLOR]/[LIGHT]/[FRAME]`，逐字相同
- ✅ 闭眼要写 `BOTH EYES COMPLETELY CLOSED, eyelids fully shut, no pupils`（`eyes half closed` 会漏瞳孔）
- ✅ 古装配 `natural anatomically correct human proportions` + 明确腰线（如 `a narrow sash cinched in at the waist`），防止鼓成"大头娃娃"
- ❌ 夸张大笑、瞪眼搞怪 → 立刻掉档成表情包
- ❌ 3D 感 / 数字锐化 / 棚拍布光 → 胶片感全丢
- ❌ 让 AI 直接写中日文 → 必然乱码，文字一律脚本后期叠
- ❌ 真实品牌道具商用前必须换虚构品牌
- ❌ 直接复刻他人具体作品——学风格可以，抄作品不行

## 七、版权与使用声明

- 本 skill 的文档、脚本与 `examples/` 全部样图均为 **PY (PyQuant)** 的原创作品。
- 风格方法源于对公开内容的观察学习，包内**不含任何第三方图片素材**。
- 详见 [LICENSE](LICENSE) 与 [README.md](README.md)。
