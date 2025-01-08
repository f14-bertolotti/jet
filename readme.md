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

![image](https://github.com/f14-bertolotti/jet/blob/main/images/test.png?raw=true)

## Commands Tree

```bash
jet [OPTIONS] COMMAND [ARGS]...
```

- `--help`: Show help message and exit

Initialize a new plot grid.

```bash
jet init [OPTIONS] COMMAND [ARGS]...
```

Options:
- `--shape <INTEGER INTEGER>`: Set the grid plot size
- `--font-size INTEGER`: Set the font size
- `--font-family TEXT`: Set the font family

Create scatter plots from data.

```bash
jet scatter [OPTIONS] COMMAND [ARGS]...
```

Options:
- `--input-path PATH`: JSONL input data files
- `--samples INTEGER`: Number of lines in the final data
- `--slice <NINT NINT NINT>`: Number of lines to skip
- `--label TEXT`: Label for the legend
- `--x TEXT`: X-axis values
- `--y TEXT`: Y-axis values
- `--ax <INTEGER INTEGER>`: Grid indices for the plot
- `--where WHERE`: Evaluatable condition used as filter
- `--legend TEXT`: Legend type
- `--color <FLOAT FLOAT FLOAT>`: Plot color
- `--linewidth FLOAT`: Line width

Create line plots from data.

```bash
jet line [OPTIONS] COMMAND [ARGS]...
```

Options:
- `--input-path PATH`: JSONL input data files
- `--samples INTEGER`: Number of lines in the final data
- `--slice <NINT NINT NINT>`: Number of lines to skip
- `--label TEXT`: Label for the legend
- `--x TEXT`: X-axis values
- `--y TEXT`: Y-axis values
- `--ax <INTEGER INTEGER>`: Grid indices for the plot
- `--where WHERE`: Evaluatable condition used as filter
- `--legend TEXT`: Legend type
- `--color <FLOAT FLOAT FLOAT>`: Plot color
- `--linewidth FLOAT`: Line width
- `--linestyle TEXT`: Line style

Modify plot attributes and appearance.

```bash
jet mod [OPTIONS] COMMAND [ARGS]...
```

Options:
- `--ax <INTEGER INTEGER>`: Grid indices for the plot
- `--left-spine BOOLEAN`: Controls the visibility of the left spine
- `--right-spine BOOLEAN`: Controls the visibility of the right spine
- `--top-spine BOOLEAN`: Controls the visibility of the top spine
- `--bottom-spine BOOLEAN`: Controls the visibility of the bottom spine
- `--y-label TEXT`: Y axis label name
- `--x-label TEXT`: X axis label name
- `--y-scale TEXT`: Y axis scale (e.g., linear, log, symlog, logit)
- `--x-scale TEXT`: X axis scale (e.g., linear, log, symlog, logit)
- `--y-lim <FLOAT FLOAT>`: Y axis limits
- `--x-lim <FLOAT FLOAT>`: X axis limits
- `--title TEXT`: Plot title

Configure plot legends.

```bash
jet legend [OPTIONS] COMMAND [ARGS]...
```

Options:
- `--line <TEXT FLOAT FLOAT FLOAT FLOAT>`: Add line to legend in the form of (label,color,width)
- `--frameon BOOLEAN`: True if the legend frame should be shown

Control plot output and display.

```bash
jet plot [OPTIONS] COMMAND [ARGS]...
```

Options:
- `--show BOOLEAN`: True if the plot has to be shown
- `--output-path PATH`: Output plot path
- `--figsize <FLOAT FLOAT>`: Figure size
- `--tight BOOLEAN`: Tight layout

Configure color palettes.

```bash
jet palette [OPTIONS] COMMAND [ARGS]...
```

Options:
- `--name TEXT`: Palette name
- `--length INTEGER`: Palette samples
- `--index INTEGER`: Palette index


## Notes
- The tool supports nested commands (e.g., `jet jet scatter`) which provide the same functionality as their top-level counterparts
- All commands support the `--help` option for detailed usage information
