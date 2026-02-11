"""Create video and audio clips using Pixeltable."""

from pathlib import Path
import pixeltable as pxt

MEDIA_DIR = Path(__file__).parent / 'media'

# Clean up any previous run
pxt.drop_dir('create_clips', force=True)
pxt.create_dir('create_clips')

# --- Halftime show clips ---

halftime = pxt.create_table('create_clips.halftime', {'video': pxt.Video})
halftime.insert([{'video': 'media/vid-lx-halftime-show.mp4'}])

# Clip the first 5 minutes
halftime.add_computed_column(
    clip_5min=halftime.video.clip(start_time=0.0, duration=300.0),
    destination=str(MEDIA_DIR),
)

# Clip 4:20–4:30 (10 seconds)
halftime.add_computed_column(
    clip_10s=halftime.video.clip(start_time=260.0, end_time=270.0),
    destination=str(MEDIA_DIR),
)

result = halftime.select(halftime.clip_5min, halftime.clip_10s).collect()
print(f"Halftime 5-min clip: {result['clip_5min'][0]}")
print(f"Halftime 10s clip:   {result['clip_10s'][0]}")

# --- Violin cover clips ---

violin = pxt.create_table('create_clips.violin', {'video': pxt.Video})
violin.insert([{'video': 'media/vid-violin-cover.mp4'}])

# Video clip 17s–22s (5s to safely exceed TwelveLabs 4s minimum)
violin.add_computed_column(
    clip_5s=violin.video.clip(start_time=17.0, end_time=22.0),
    destination=str(MEDIA_DIR),
)

# Audio extraction from the same 17s–22s clip
violin.add_computed_column(
    audio_5s=violin.clip_5s.extract_audio(format='wav'),
    destination=str(MEDIA_DIR),
)

result = violin.select(violin.clip_5s, violin.audio_5s).collect()
print(f"Violin video clip:   {result['clip_5s'][0]}")
print(f"Violin audio clip:   {result['audio_5s'][0]}")
