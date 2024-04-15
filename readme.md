<img align="left" width="80px" src="https://github.com/f14-bertolotti/jet/blob/main/images/jet.png?raw=true" />

# Jet

**Note:** Jet is currently in its early stages of development and may be highly unstable.

## Description

Jet is a simple command-line utility designed to generate plots from JSON-line files.

## Requirements

Jet relies on the following libraries:
- Matplotlib
- Seaborn
- Pandas
- Click

## Usage

Data files should be formatted with a single JSON object per line, as shown in the example below:

```json
{"step": 0, "loss": -0.03763704001903534, "reward": 0.04284941032528877}
{"step": 1, "loss": -0.02104765921831131, "reward": 0.02155069075524807}
{"step": 2, "loss": -0.00058268022257834, "reward": -0.0063234698027372}
{"step": 3, "loss": 0.014676971361041069, "reward": -0.0204243808984756}
```

The command-line interface is generated using [Click](https://click.palletsprojects.com/en/8.1.x/), so you can explore it using `--help`.

### Example

- The following command displays a line plot of the `loss` value against the `step`:
  
  ```bash
  python3 jet.py line --input-path data/data.jsonl --x step --y loss jet plot --show True
  ```

- The following command displays a line plot of the `loss` value against the `step` and `reward` against the `step`:
  
  ```bash
    python3 jet.py \
        jet line --input-path data/data.jsonl --x step --y loss \
        jet line --input-path data/data.jsonl --x step --y reward \
        jet plot --show True
  ```
