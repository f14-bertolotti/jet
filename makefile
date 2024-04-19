PYTHON := /usr/bin/python3

venv/bin/python3: 
	${PYTHON} -m venv venv

build: venv/bin/python3
	venv/bin/python3 -m pip install -r requirements.txt

test: venv/bin/python3
	venv/bin/python3 src/jet.py \
		jet init --shape 2 2 \
		jet line \
			--ax 0 0 \
			--nrows 2 \
			--input-path data/data0.jsonl \
			--input-path data/data1.jsonl \
			--input-path data/data2.jsonl \
			--x step \
			--y message/reward \
			--color $(shell venv/bin/python3 src/jet.py palette --name magma --length 3 --index 0) \
			--label reward \
		jet scatter \
			--ax 0 1 \
			--input-path data/data2.jsonl \
			--x step \
			--y message/loss \
			--label aaa \
		jet mod \
			--ax 0 1 \
			--right-spine False \
			--top-spine False \
			--y-label loss \
			--x-label epoch \
			--title loss \
		jet plot --show True

