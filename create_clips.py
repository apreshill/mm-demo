"""Create video clips from the full halftime show video using Pixeltable."""

from pathlib import Path
import pixeltable as pxt

MEDIA_DIR = Path(__file__).parent / 'media'
SOURCE_VIDEO = 'media/vid-lx-halftime-show.mp4'

# Clean up any previous run
pxt.drop_dir('create_clips', force=True)
pxt.create_dir('create_clips')

# Create a table and insert the full video
videos = pxt.create_table('create_clips.videos', {'video': pxt.Video})
videos.insert([{'video': SOURCE_VIDEO}])

# Clip the first 5 minutes
videos.add_computed_column(
    clip_5min=videos.video.clip(start_time=0.0, duration=300.0),
    destination=str(MEDIA_DIR),
)

# Clip 4:20–4:30 (10 seconds)
videos.add_computed_column(
    clip_10s=videos.video.clip(start_time=260.0, end_time=270.0),
    destination=str(MEDIA_DIR),
)

# Show results
result = videos.select(videos.clip_5min, videos.clip_10s).collect()
print(f"5-min clip: {result['clip_5min'][0]}")
print(f"10s clip:   {result['clip_10s'][0]}")
