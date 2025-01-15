SRC=servitor/__init__.py

all: run

check: ${SRC} init
	ruff check $<
	ruff format $<

run: check
	uv run ${SRC}

push: check
	git push origin main
