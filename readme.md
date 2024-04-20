<img align="left" width="80px" src="https://github.com/f14-bertolotti/jet/blob/main/images/jet.png?raw=true" />

# Jet

**Note:** Jet is currently in its early stages of development and may be highly unstable.

## Description

Jet is a simple command-line utility designed to generate plots from JSON-line files.

## Requirements

- `python3`
- `make`

## Installation

```bash
    make venv/bin/activate
```
and put the jet repo inside `$PATH`

## Example

- The following command displays a line plot of the `loss` value against the `step`:
  
  ```bash
  jet line --input-path data/data.jsonl --x step --y loss jet plot --show True
  ```

- The following command displays a line plot of the `loss` value against the `step` and `reward` against the `step`:
  
  ```bash
    jet init --shape 1 2 \
		jet line \
			--ax 0 0 \
			--input-path data/data0.jsonl \
			--input-path data/data1.jsonl \
			--x step \
			--y message/reward \
			--label "reward" \
		jet scatter \
			--ax 0 1 \
			--input-path data/data2.jsonl \
			--x step \
			--y message/loss \
			--label "loss" \
		jet mod \
			--right-spine False \
			--top-spine False \
			--y-label "reward" \
			--x-label "step" \
			--ax 0 0 \
		jet mod \
			--right-spine False \
			--top-spine False \
			--y-label "reward" \
			--x-label "step" \
			--ax 0 0 \
        jet plot --show False --output-path images/test.png
  ```

The result is the following

<img align="left" width="480px" src="https://github.com/f14-bertolotti/jet/blob/main/images/test.png?raw=true" />
