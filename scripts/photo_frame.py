#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
photo_frame.py — 相纸边框 + 右上竖排注记 + 底部标题（小清新萌萌哒写真出图最后一道工序）

PyQuant-XQX.skill · Copyright (c) 2026 PY (PyQuant) · MIT License

用法:
    python photo_frame.py 输入.png 输出.png \
        --ratio 0.055 --crop-bottom 0.06 --bottom-extra 0.9 \
        --title-in-margin --halo 0.5 \
        --caption "風にゆれて" --caption2 "はるのいろ" \
        --title "野原の 小さな幸せ"

输出可选 .png（无损母版）或 .jpg/.jpeg（对外发布，自动转 RGB）。
仅依赖 Pillow（>= 9.0）。Python >= 3.9。
"""

import argparse
import math
import os
import sys

from PIL import Image, ImageDraw, ImageFont, ImageFilter

# ---------------- CJK 字体自动探测 ----------------

FONT_CANDIDATES = [
    # Windows（日文优先，注记多为日文）
    r"C:\Windows\Fonts\YuGothR.ttc",
    r"C:\Windows\Fonts\YuGothM.ttc",
    r"C:\Windows\Fonts\msgothic.ttc",
    r"C:\Windows\Fonts\msyh.ttc",
    r"C:\Windows\Fonts\NotoSansSC-VF.ttf",
    r"C:\Windows\Fonts\simhei.ttf",
    r"C:\Windows\Fonts\simsun.ttc",
    # macOS
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/System/Library/Fonts/STHeiti Light.ttc",
    "/System/Library/Fonts/PingFang.ttc",
    # Linux
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/noto-cjk/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
]

# 竖排时需要旋转 90° 的字符（日文纵书规范）
ROTATE_CHARS = set("ー－―—…‥・！？!?，,。.：:；;")


def find_font(user_font: str | None) -> str:
    if user_font:
        if os.path.exists(user_font):
            return user_font
        sys.exit(f"[photo_frame] 指定的字体不存在: {user_font}")
    for p in FONT_CANDIDATES:
        if os.path.exists(p):
            return p
    sys.exit(
        "[photo_frame] 未找到 CJK 字体，请用 --font 指定一个 ttf/otf/ttc 文件\n"
        "  例: --font C:\\Windows\\Fonts\\YuGothR.ttc"
    )


def load_font(path: str, size: int) -> ImageFont.FreeTypeFont:
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        # ttc 需要索引时兜底
        return ImageFont.truetype(path, size, index=0)


# ---------------- 竖排文字 ----------------

def draw_vertical_text(
    canvas: Image.Image,
    text: str,
    x_center: int,
    y_top: int,
    font: ImageFont.FreeTypeFont,
    font_path: str,
    fill=(60, 60, 60),
    halo: float = 0.0,
    halo_color=(255, 255, 255),
) -> int:
    """从 (x_center, y_top) 开始向下竖排一列字，返回该列结束的 y。"""
    glyph_px = font.size
    line_h = int(glyph_px * 1.12)

    # 柔光底层（保证文字在画面上可读）
    if halo > 0:
        layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        ld = ImageDraw.Draw(layer)
        yy = y_top
        for ch in text:
            if ch in ("\n", " "):
                yy += line_h
                continue
            _draw_one_glyph(ld, ch, x_center, yy, font, font_path, fill=halo_color)
            yy += line_h
        layer = layer.filter(ImageFilter.GaussianBlur(radius=max(2, glyph_px * 0.45)))
        layer = _scale_alpha(layer, halo)
        canvas.alpha_composite(layer) if canvas.mode == "RGBA" else canvas.paste(
            Image.alpha_composite(canvas.convert("RGBA"), layer).convert("RGB"), (0, 0)
        )

    draw = ImageDraw.Draw(canvas)
    yy = y_top
    for ch in text:
        if ch in ("\n", " "):
            yy += line_h
            continue
        _draw_one_glyph(draw, ch, x_center, yy, font, font_path, fill=fill)
        yy += line_h
    return yy


def _draw_one_glyph(draw, ch, x_center, y_top, font, font_path, fill):
    # 需要旋转的字符：先画到小图再旋转贴回
    if ch in ROTATE_CHARS:
        pad = int(font.size * 0.3)
        tmp = Image.new("RGBA", (font.size + pad * 2, font.size + pad * 2), (0, 0, 0, 0))
        td = ImageDraw.Draw(tmp)
        td.text((pad, pad), ch, font=font, fill=fill)
        tmp = tmp.rotate(90, expand=False, resample=Image.BICUBIC)
        draw._image.paste(tmp, (int(x_center - tmp.width / 2), int(y_top - pad)), tmp)
    else:
        w = draw.textlength(ch, font=font)
        draw.text((x_center - w / 2, y_top), ch, font=font, fill=fill)


def _scale_alpha(layer: Image.Image, factor: float) -> Image.Image:
    a = layer.getchannel("A").point(lambda v: int(v * max(0.0, min(1.0, factor))))
    layer.putalpha(a)
    return layer


# ---------------- 主流程 ----------------

def frame_photo(args) -> None:
    im = Image.open(args.input)
    im = im.convert("RGB")
    W, H = im.size

    # 1) 裁底
    if args.crop_bottom > 0:
        H = int(round(H * (1.0 - args.crop_bottom)))
        im = im.crop((0, 0, W, H))

    # 2) 相纸几何（经实拍样图校准：border=W*ratio, 底边=border*(1+bottom_extra)）
    border = int(round(W * args.ratio))
    bottom = int(border * (1.0 + args.bottom_extra))
    canvas = Image.new("RGB", (W + 2 * border, H + border + bottom), args.paper)
    canvas.paste(im, (border, border))

    draw = ImageDraw.Draw(canvas)
    font_path = find_font(args.font)

    # 3) 右上竖排注记（caption 在最右列，caption2 在其左）
    if args.caption or args.caption2:
        cap_size = max(14, int(round(W * args.caption_ratio)))
        cap_font = load_font(font_path, cap_size)
        col_gap = int(cap_size * 1.55)
        x_right = border + W - int(border * 0.55) - cap_size // 2
        y_top = border + int(border * 1.1)
        x_cur = x_right
        for text in (args.caption, args.caption2):
            if text:
                draw_vertical_text(
                    canvas, text, x_cur, y_top, cap_font, font_path,
                    fill=tuple(args.ink), halo=args.halo,
                )
            x_cur -= col_gap

    # 4) 标题
    if args.title:
        t_size = max(16, int(round(border * 0.55)))
        t_font = load_font(font_path, t_size)
        tw = draw.textlength(args.title, font=t_font)
        if args.title_in_margin:
            # 底边白框内右对齐
            tx = W + 2 * border - border // 2 - tw
            ty = H + border + (bottom - t_size) // 2 - int(t_size * 0.15)
        else:
            # 画面内右下角
            tx = W + border - border // 2 - tw
            ty = H + border - int(border * 0.9) - t_size
        if args.halo > 0 and not args.title_in_margin:
            halo_layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
            hd = ImageDraw.Draw(halo_layer)
            hd.text((tx, ty), args.title, font=t_font, fill=(255, 255, 255))
            halo_layer = halo_layer.filter(ImageFilter.GaussianBlur(radius=max(2, t_size * 0.4)))
            halo_layer = _scale_alpha(halo_layer, args.halo)
            canvas = Image.alpha_composite(canvas.convert("RGBA"), halo_layer).convert("RGB")
            draw = ImageDraw.Draw(canvas)
        draw.text((tx, ty), args.title, font=t_font, fill=tuple(args.ink))

    # 5) 输出
    ext = os.path.splitext(args.output)[1].lower()
    if ext in (".jpg", ".jpeg"):
        canvas.save(args.output, "JPEG", quality=args.quality, optimize=True)
    else:
        canvas.save(args.output)
    print(
        f"[photo_frame] {os.path.basename(args.input)} {W}x{H} -> "
        f"{canvas.size[0]}x{canvas.size[1]} -> {args.output}"
    )


def main():
    ap = argparse.ArgumentParser(
        description="相纸边框 + 右上竖排注记 + 底部标题（PyQuant-XQX.skill）",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    ap.add_argument("input", help="输入图片")
    ap.add_argument("output", help="输出图片（.png 或 .jpg）")
    ap.add_argument("--ratio", type=float, default=0.055, help="边框宽度 / 原图宽度")
    ap.add_argument("--crop-bottom", type=float, default=0.0, help="裱框前裁掉底部比例")
    ap.add_argument("--bottom-extra", type=float, default=0.9, help="底边加宽系数（给标题留位）")
    ap.add_argument("--title-in-margin", action="store_true", help="标题放在底边白框内")
    ap.add_argument("--caption", default="", help="右上竖排注记第一列（最右）")
    ap.add_argument("--caption2", default="", help="右上竖排注记第二列")
    ap.add_argument("--title", default="", help="右下标题")
    ap.add_argument("--halo", type=float, default=0.5, help="文字柔光强度 0-1")
    ap.add_argument("--caption-ratio", type=float, default=0.024, help="注记字号 / 原图宽度")
    ap.add_argument("--ink", type=int, nargs=3, default=(60, 60, 60), metavar=("R", "G", "B"),
                    help="文字颜色")
    ap.add_argument("--paper", type=int, nargs=3, default=(250, 249, 246), metavar=("R", "G", "B"),
                    help="相纸颜色（微暖白）")
    ap.add_argument("--font", default=None, help="手动指定 CJK 字体文件")
    ap.add_argument("--quality", type=int, default=92, help="JPG 输出质量")
    args = ap.parse_args()
    frame_photo(args)


if __name__ == "__main__":
    main()
