SRC=servitor/__init__.py

all: run

check: ${SRC} init
	ruff check $<
	ruff format $<

run: check
	uv run ${SRC}

push: check
	git push origin main

init: resume.pdf config.ini

resume.pdf: resume.md
	pandoc -fcommonmark_x -thtml -i $< -o - | pandoc -fhtml -tpdf -i - -o $@

resume.md: resume.md.example
	cp $< $@

config.ini: config.ini.example
	cp $< $@
