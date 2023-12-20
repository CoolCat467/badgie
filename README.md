# Badgie Fork

<!-- BADGIE TIME -->

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/CoolCat467/badgie/main.svg)](https://results.pre-commit.ci/latest/github/CoolCat467/badgie/main)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![code style: black](https://img.shields.io/badge/code_style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

<!-- END BADGIE TIME -->

Add all the badges with Badgie!

### This is a fork

The original project can be found here:
https://gitlab.com/brettops/tools/badgie/

## Using Badgie

Install Badgie:

```bash
pip install badgie
```

Add Badgie tags to your README.md:

```md
<!-- BADGIE TIME -->
<!-- END BADGIE TIME -->
```

Add Badgie tags to your README.rst:

```rst
.. <!-- BADGIE TIME -->
.. <!-- END BADGIE TIME -->
```

Run Badgie:

```bash
badgie -w README.md
```

And enjoy magic badges:

```md
<!-- BADGIE TIME -->

[![pipeline status](brettops/containers/verible/badges/main/pipeline.svg)](brettops/containers/verible/-/commits/main)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

<!-- END BADGIE TIME -->
```

### Use as a pre-commit hook

Badgie can be used as a pre-commit hook, so you can get fresh badges on every
commit.

Add the following to your `.pre-commit-config.yaml` file.

```yaml
repos:
  - repo: https://github.com/CoolCat467/badgie
    rev: v0.9.5
    hooks:
      - id: badgie
```

Run `pre-commit autoupdate` to pin to the latest version:

```bash
pre-commit autoupdate
```

Run `pre-commit` directly or install as a hook:

```bash
# directly
pre-commit

# as a Git hook
pre-commit install
git commit -m "..."
```

## Caveats

Badgie makes decisions on the assumption that you do sensible things with your
repository structure. It does not try to work around bad practices. Pull requests that
encourage this will be rejected.
