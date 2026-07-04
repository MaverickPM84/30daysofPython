# GIF Maker 🎞️

A small Python script that stitches a sequence of images together into an animated GIF, using the [`imageio`](https://imageio.readthedocs.io/) library.

This is the final project for my **30 Days of Python** journey.

## What it does

`gif.py` reads a list of image files, loads them in order, and writes them out as a single looping GIF where each frame is shown for half a second.

## Requirements

- Python 3
- [`imageio`](https://pypi.org/project/imageio/) (installs `numpy` and `pillow` as dependencies)

Install into your virtual environment:

```powershell
& .venv/Scripts/python.exe -m pip install imageio
```

## Usage

1. Place your image files in this folder.
2. Edit the `filenames` list in `gif.py` to point at your images, in the order you want them to appear:

   ```python
   filenames = ['aditya-1.jpeg', 'aditya-2.jpeg', 'aditya-3.jpeg']
   ```

3. Run the script:

   ```powershell
   & .venv/Scripts/python.exe gif.py
   ```

4. The GIF is saved to this folder (e.g. `spiderman.gif`).

## Customizing the output

The GIF is created by `iio.imwrite()`, which takes:

| Argument     | Meaning                                                        |
| ------------ | -------------------------------------------------------------- |
| `'name.gif'` | Output filename for the GIF.                                   |
| `images`     | The list of loaded image frames.                              |
| `duration`   | How long each frame shows, in **milliseconds** (`500` = 0.5s). |
| `loop`       | How many times to repeat (`0` = loop forever).                |

Tweak `duration` for faster/slower playback, or add more files to `filenames` for a longer animation.
