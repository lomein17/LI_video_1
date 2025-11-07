#!/usr/bin/env python3
"""
LinkedIn Article Cover Video Generator
Creates a 30-second corporate-style video with text animations
"""

from moviepy import *
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

# Video specifications
WIDTH = 1920
HEIGHT = 1080
FPS = 30

# Color palette
BG_DARK = (26, 26, 26)
BG_LIGHTER = (35, 35, 35)
TEXT_WHITE = "white"
TEXT_RED = "#ef4444"


def create_gradient_background(width, height, color1=(26, 26, 26), color2=(10, 25, 41)):
    """Create a subtle gradient background"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    for i in range(height):
        ratio = i / height
        r = int(color1[0] + (color2[0] - color1[0]) * ratio)
        g = int(color1[1] + (color2[1] - color1[1]) * ratio)
        b = int(color1[2] + (color2[2] - color1[2]) * ratio)
        draw.line([(0, i), (width, i)], fill=(r, g, b))

    return np.array(img)


def create_simple_graph(width, height):
    """Create a simple upward trending line graph"""
    img = Image.new('RGB', (width, height), BG_DARK)
    draw = ImageDraw.Draw(img)

    points = [
        (width // 4, height * 3 // 4),
        (width // 2, height // 2),
        (width * 3 // 4, height // 4)
    ]

    draw.line(points, fill=(239, 68, 68), width=4)

    arrow_x = width * 3 // 4
    arrow_y = height // 4
    draw.polygon([
        (arrow_x, arrow_y),
        (arrow_x - 15, arrow_y + 25),
        (arrow_x + 15, arrow_y + 25)
    ], fill=(239, 68, 68))

    return np.array(img)


def scene_1_hook():
    """SCENE 1 (0-3s): The Hook"""
    duration = 3

    bg_array = create_gradient_background(WIDTH, HEIGHT)
    background = ImageClip(bg_array).with_duration(duration)

    text = TextClip(
        text="Your board can't\ngovern AI.",
        font_size=90,
        color=TEXT_WHITE,
        stroke_color='black',
        stroke_width=3,
        size=(WIDTH, HEIGHT),
        text_align='center',
        vertical_align='center',
        horizontal_align='center'
    ).with_duration(duration).with_position('center')

    return CompositeVideoClip([background, text], size=(WIDTH, HEIGHT))


def scene_2_problem():
    """SCENE 2 (4-9s): The Problem"""
    duration = 6

    background = ColorClip(size=(WIDTH, HEIGHT), color=BG_DARK).with_duration(duration)

    text1 = TextClip(
        text="Traditional oversight models",
        font_size=54,
        color=TEXT_WHITE,
        stroke_color='black',
        stroke_width=2,
        size=(WIDTH, None),
        text_align='center'
    ).with_duration(duration).with_position(('center', HEIGHT // 2 - 150))

    text2 = TextClip(
        text="FAIL",
        font_size=100,
        color=TEXT_RED,
        stroke_color='black',
        stroke_width=3,
        size=(WIDTH, None),
        text_align='center'
    ).with_duration(duration).with_position(('center', HEIGHT // 2))

    text3 = TextClip(
        text="at AI speed.",
        font_size=54,
        color=TEXT_WHITE,
        stroke_color='black',
        stroke_width=2,
        size=(WIDTH, None),
        text_align='center'
    ).with_duration(duration).with_position(('center', HEIGHT // 2 + 150))

    return CompositeVideoClip([background, text1, text2, text3], size=(WIDTH, HEIGHT))


def scene_3_stakes():
    """SCENE 3 (10-16s): The Stakes"""
    duration = 7

    bg_array = create_simple_graph(WIDTH, HEIGHT)
    background = ImageClip(bg_array).with_duration(duration)

    text1 = TextClip(
        text="Risk moves faster",
        font_size=90,
        color=TEXT_WHITE,
        stroke_color='black',
        stroke_width=3,
        size=(WIDTH, None),
        text_align='center'
    ).with_duration(duration).with_position(('center', HEIGHT // 2 - 100))

    text2 = TextClip(
        text="than quarterly reviews.",
        font_size=54,
        color=TEXT_WHITE,
        stroke_color='black',
        stroke_width=2,
        size=(WIDTH, None),
        text_align='center'
    ).with_duration(duration).with_position(('center', HEIGHT // 2 + 100))

    return CompositeVideoClip([background, text1, text2], size=(WIDTH, HEIGHT))


def scene_4_shift():
    """SCENE 4 (17-24s): The Shift"""
    duration = 8

    background = ColorClip(size=(WIDTH, HEIGHT), color=BG_LIGHTER).with_duration(duration)

    text1 = TextClip(
        text="Boards need\nnew muscles.",
        font_size=90,
        color=TEXT_WHITE,
        stroke_color='black',
        stroke_width=3,
        size=(WIDTH, HEIGHT // 2),
        text_align='center',
        vertical_align='center'
    ).with_duration(duration).with_position(('center', HEIGHT // 2 - 120))

    text2 = TextClip(
        text="Not more meetings.",
        font_size=54,
        color=TEXT_WHITE,
        stroke_color='black',
        stroke_width=2,
        size=(WIDTH, None),
        text_align='center'
    ).with_duration(duration).with_position(('center', HEIGHT // 2 + 120))

    return CompositeVideoClip([background, text1, text2], size=(WIDTH, HEIGHT))


def scene_5_cta():
    """SCENE 5 (25-28s): The CTA"""
    duration = 4

    background = ColorClip(size=(WIDTH, HEIGHT), color=BG_DARK).with_duration(duration)

    text = TextClip(
        text="Read the full framework ↓",
        font_size=64,
        color=TEXT_WHITE,
        stroke_color='black',
        stroke_width=2,
        size=(WIDTH, HEIGHT),
        text_align='center',
        vertical_align='center',
        horizontal_align='center'
    ).with_duration(duration).with_position('center')

    return CompositeVideoClip([background, text], size=(WIDTH, HEIGHT))


def main():
    """Generate the complete video"""
    print("🎬 Starting video generation...")
    print("=" * 50)

    print("Creating Scene 1: The Hook (0-3s)...")
    scene1 = scene_1_hook()

    print("Creating Scene 2: The Problem (3-9s)...")
    scene2 = scene_2_problem()

    print("Creating Scene 3: The Stakes (9-16s)...")
    scene3 = scene_3_stakes()

    print("Creating Scene 4: The Shift (16-24s)...")
    scene4 = scene_4_shift()

    print("Creating Scene 5: The CTA (24-28s)...")
    scene5 = scene_5_cta()

    print("\nConcatenating all scenes...")
    final_video = concatenate_videoclips([scene1, scene2, scene3, scene4, scene5], method="compose")

    output_file = "linkedin_ai_governance_video.mp4"
    print(f"\n📹 Rendering final video: {output_file}")
    print("This may take a few minutes...")

    final_video.write_videofile(
        output_file,
        fps=FPS,
        codec='libx264',
        audio=False,
        preset='medium',
        bitrate='8000k',
        threads=4
    )

    print("\n✅ Video generation complete!")
    print(f"📊 Output: {output_file}")
    print(f"⏱️  Duration: {final_video.duration:.1f} seconds")

    file_size = os.path.getsize(output_file) / (1024 * 1024)
    print(f"💾 File size: {file_size:.2f} MB")

    if file_size > 50:
        print("⚠️  Warning: File size exceeds 50MB threshold")


if __name__ == "__main__":
    main()
