#!/usr/bin/env python3
"""Extract key frames from the video as preview images"""

from moviepy import VideoFileClip
import os

# Create frames directory
os.makedirs('preview_frames', exist_ok=True)

# Load video
clip = VideoFileClip('linkedin_ai_governance_video.mp4')

# Extract one frame from each scene
timestamps = {
    'scene1_hook': 1.5,
    'scene2_problem': 6.0,
    'scene3_stakes': 13.0,
    'scene4_shift': 20.0,
    'scene5_cta': 26.0
}

for name, time in timestamps.items():
    frame = clip.get_frame(time)
    from PIL import Image
    img = Image.fromarray(frame)
    img.save(f'preview_frames/{name}.png')
    print(f"Saved {name}.png")

clip.close()
print("\nAll preview frames extracted to preview_frames/ directory")
