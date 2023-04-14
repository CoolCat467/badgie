# Badgie

<!-- BADGIE TIME -->

[![brettops tool](https://img.shields.io/badge/brettops-tool-209cdf?labelColor=162d50)](https://brettops.io)
[![latest release](https://img.shields.io/gitlab/v/release/brettops/tools/badgie)](https://gitlab.com/brettops/tools/badgie/-/releases)
[![pipeline status](https://gitlab.com/brettops/tools/badgie/badges/main/pipeline.svg)](https://gitlab.com/brettops/tools/badgie/-/commits/main)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

<!-- END BADGIE TIME -->

Add all the badges with Badgie!

---

**Badgie is experimental and should not be used by anyone ever!**

---

## tl;dr

Install Badgie:

```bash
pip install badgie
```

Add Badgie tags:

```md
<!-- BADGIE TIME -->
<!-- END BADGIE TIME -->
```

Run Badgie:

```bash
badgie -w README.md
```

## Why Badgie

Adding badges to repositories is frustrating. I spend so much time fiddling with
setup and achieve little consistency across repos without even more fiddling.

Without Badgie, there's a good chance that:

- Most repos just don't have badges.

- If they have badges, they look different or show different info between repos.

- Updating them is not fun.

The thing is, the whole internet WANTS you to have badges:

- Badges convey authority and stewardship while occupying little real estate.

- Many services have badges to make discovering info about your project easier.

- You just gotta know where to find 'em!

## About Badgie

Badgie is different because Badgie doesn't like asking for anything.

Starting with the Git remote URL of your checked out repo, Badgie attempts to
reconstruct what your repository is, where it came from, and what information is
interesting about it.

## Supported features

Here's what Badgie supports currently:

**Almost nothing!**

Here's a more exhaustive list:

- Interfacing with GitLab (barely)

- Generated badges:

  - GitLab CI pipeline status

  - Pre-commit

Badgie is used to manage the badges on this README.

## Using Badgie

Add the following tags wherever and Badgie will do its thing.

```md
<!-- BADGIE TIME -->
<!-- END BADGIE TIME -->
```

Then run Badgie:

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

## Caveats

Badgie makes decisions on the assumption that you do sensible things with your
repository structure. It does not try to work around bad practices. MRs that
encourage this will be rejected.
