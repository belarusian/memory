# Micromegas Procedural Lab

This package provides seeded procedural object-family generators inspired by *Micromégas*.

## Generators

- `generators/great_microscope.py`
- `generators/empty_book.py`
- `generators/sirian_instrument.py`
- `generators/cosmic_necklace.py`
- `generators/alien_measure.py`
- `generators/scale_reliquary.py`

All generators accept the same headless CLI:

```bash
python generators/great_microscope.py --seed 1847 --output outputs/micromegas/json/great_microscope.json --style sample --complexity 4
```

Blender-compatible execution:

```bash
blender -b --python generators/great_microscope.py -- --seed 1847 --output outputs/micromegas/blend/great_microscope.blend --style sample --complexity 4
```

## Batch sample generation

Run one sample per generator family:

```bash
./generators/run_samples.sh
```

- Always writes JSON artifacts and a manifest to `outputs/micromegas/`.
- If `blender` is available in PATH, also writes one rendered PNG per generator.

## HTML visualizer

Open:

- `micromegas/visualizer.html`

Then click **Load default manifest** after running `./generators/run_samples.sh`.

## Seed sweep validation

```bash
python generators/validate_seed_sweep.py
```

This checks geometric variation across many seeds and validates the `empty_book` blank-page invariant.
