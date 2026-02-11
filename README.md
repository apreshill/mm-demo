# mm-demo

Multimodal search demos using [Pixeltable](https://github.com/pixeltable/pixeltable) and [TwelveLabs](https://twelvelabs.io/).

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- A [TwelveLabs API key](https://playground.twelvelabs.io/)

## Setup

```bash
git clone https://github.com/apreshill/mm-demo.git
cd mm-demo
uv sync
```

Set your TwelveLabs API key in `~/.pixeltable/config.toml`:

```toml
[twelvelabs]
api_key = "tlk_YOUR_KEY_HERE"
```

## Usage

Open any notebook with your preferred editor (VS Code, JupyterLab, etc.):

- `halftime.ipynb` — Cross-modal video search with TwelveLabs embeddings

### Helper scripts

```bash
# Create video clips from the full halftime show source video
uv run create_clips.py
```