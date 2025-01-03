SRC=servitor/__init__.py

all: run

check: ${SRC}
	ruff check ${SRC}
	ruff format ${SRC}

run: check
	uv run ${SRC}
