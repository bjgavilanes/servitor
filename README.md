# Servitor, Job Hunting Side-Kick

Servitor is an automated job applier for all your job hunting needs. As of now, 2025-01-14, is a prototype, and we are handling one use-case -- a popular professional networkign site --, but we do intent to provide a local-first web automation scheme and AI worker using ollama.

## Usage

There's a `config.ini.example` provided at the root directory of this repository. You should copy that to `config.ini` and then modify it accordingly.

We intend to write a `init` makefile target. It is not yet implemented.

## Feats

- Support C.V. / Resume generation
- An extendable codebase to support every job hunting site out there -- even the more manual ones!
- A setup using POSIX-compatible `make` -- maybe even `m4`
- A local-first, containerized, performant developer experience

## Developer Experience

We are using `uv` as a project and dependency manager. Our linter and formatter, is `ruff`. We use nix, throught `nix-shell` to manage this project high-level dependencies; using `npings` to pin nixpkgs to latest stable.

To simplify our development, we use `By.CSS_SELECTOR` as our method to get HTML components.

## Roadmap

- Authentication routine `(DONE)`
- Job applying
	- Get a list of every job listed in current page, excluding already postulated.
	- Handle edge-cases -- such a "beware of this uncomfirmed job poster" prompt `(CURRENT)`
	- Loop a set of actions for every job listed in the current page, excluding already postulated.
		- Wait for user to finish answer form questions
			- In the future, this would be handled by an AI Worker using ollama python bindings
		- Confirm and send information

As this is a prototype, we are currently supporting one use-case. We intent to indirectly support more, by abstracting `authentication` and `job_applying` routine into more general and modifiable procedure.

- C.V. / Resume generation
	- Use a commonmark plus extensions -- according to pandoc -- to generate a .pdf to upload when required.
	- Provide an example of a OCR-compatible of a .md resume
- This would make better sense as a shell-script; especially as we are using nix for dependency management.
	- Although I love to use pandoc, it's a big dependency; specially exporting to pdf, as it uses TeX.
	- Maybe m4dc?

If / when the AI worker is implemented:

- Ask the worker if job posting is compatible with provided resume
	- Return a boolean accordingly
	- We may need to implement a database solution -- SQLite, most probably -- in order to get:
		- JOB_URL
		- JOB_DESCRIPTION
		- JOB_MAIL, if it happens to be.
- Search for an email on job's description
	- Write a cover letter using provided resume, in commonmark_x
	- Generate a pdf
		- We may consider python bindings for our commonmark_x to pdf generator for this one
		- Or use xonsh. I don't know if I want a fullblown shell environtment in this project, tho.
	- If we are that bold, generate an email with provided information, attach said cover_letter, send them to job's description email.
		- We can use a smpt server pointing to a mail server and an mail agent.
