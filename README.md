# blobchat

![PyPI version](https://img.shields.io/pypi/v/blobchat.svg)

A Python library for processing and analyzing chat data

* [GitHub](https://github.com/p4prince2/blobchat/) | [PyPI](https://pypi.org/project/blobchat/) | [Documentation](https://p4prince2.github.io/blobchat/)
* Created by [Prince Kushwaha](https://github.com/p4prince2) | GitHub [@p4prince2](https://github.com/p4prince2) | PyPI [@p4prince2](https://pypi.org/user/p4prince2/)
* MIT License

## Features

* TODO

## Documentation

Documentation is built with [Zensical](https://zensical.org/) and deployed to GitHub Pages.

* **Live site:** https://p4prince2.github.io/blobchat/
* **Preview locally:** `just docs-serve` (serves at http://localhost:8000)
* **Build:** `just docs-build`

API documentation is auto-generated from docstrings using [mkdocstrings](https://mkdocstrings.github.io/).

Docs deploy automatically on push to `main` via GitHub Actions. To enable this, go to your repo's Settings > Pages and set the source to **GitHub Actions**.

## Development

To set up for local development:

```bash
# Clone your fork
git clone git@github.com:your_username/blobchat.git
cd blobchat

# Install in editable mode with live updates
uv tool install --editable .
```

This installs the CLI globally but with live updates - any changes you make to the source code are immediately available when you run `blobchat`.

Run tests:

```bash
uv run pytest
```

Run quality checks (format, lint, type check, test):

```bash
just qa
```

## Author

blobchat was created in 2026 by Prince Kushwaha.

Built with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) project template.
