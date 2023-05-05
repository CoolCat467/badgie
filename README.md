# Badgie

<!-- BADGIE TIME -->

[![brettops tool](https://img.shields.io/badge/brettops-tool-209cdf?labelColor=162d50)](https://brettops.io)
[![pipeline status](https://img.shields.io/gitlab/pipeline-status/brettops/tools/badgie?branch=main)](https://gitlab.com/brettops/tools/badgie/-/commits/main)
[![coverage report](https://img.shields.io/gitlab/pipeline-coverage/brettops/tools/badgie?branch=main)](https://gitlab.com/brettops/tools/badgie/-/commits/main)
[![latest release](https://img.shields.io/gitlab/v/release/brettops/tools/badgie)](https://gitlab.com/brettops/tools/badgie/-/releases)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![code style: black](https://img.shields.io/badge/code_style-black-000000.svg)](https://github.com/psf/black)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg)](https://github.com/prettier/prettier)

<!-- END BADGIE TIME -->

Add all the badges with Badgie!

## Using Badgie

Install Badgie:

```bash
pip install badgie
```

Add Badgie tags to your README:

```md
<!-- BADGIE TIME -->
<!-- END BADGIE TIME -->
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

Add the following to a `.pre-commit-config.yaml` file. Note the empty
`rev` tag:

```yaml
repos:
  - repo: https://gitlab.com/brettops/tools/badgie
    rev: ""
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
repository structure. It does not try to work around bad practices. MRs that
encourage this will be rejected.
