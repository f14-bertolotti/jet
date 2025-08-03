PYTHON = /usr/bin/python3

install: pyproject.toml
	uv sync

images/test.png: venv/bin/activate
		venv/bin/python3 jet/jet.py init --shape 1 2 \
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
			--ax 0 1 \
        jet plot --show False --output-path images/test.png

clean:
	rm -rf venv
