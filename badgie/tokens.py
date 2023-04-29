ANSIBLE = "ansible"
ANSIBLE_COLLECTION = "ansible_collection"
ANSIBLE_GALAXY = "ansible_galaxy"
ANSIBLE_ROLE = "ansible_role"

DETECT_SECRETS = "detect_secrets"  # pragma: allowlist secret

GIT = "git"
GITLAB = "gitlab"
GITLAB_CI = "gitlab_ci"
GITLAB_COVERAGE = "gitlab_coverage"
GITLAB_PAGES = "gitlab_pages"
GITLAB_PIPELINE = "gitlab_pipeline"
GITLAB_RELEASE = "gitlab_release"

PRE_COMMIT = "pre_commit"
PRE_COMMIT_CONFIG = "pre_commit_config"
PRE_COMMIT_HOOKS = "pre_commit_hooks"

PRETTIER = "prettier"

PYPI_DOWNLOADS = "pypi_downloads"
PYPI_FORMAT = "pypi_format"
PYPI_LICENSE = "pypi_license"
PYPI_PYTHON_VERSION = "pypi_python_version"
PYPI_STATUS = "pypi_status"
PYPI_VERSION = "pypi_version"
PYPI_WHEEL = "pypi_wheel"

PYTHON = "python"
PYTHON_BLACK = "python_black"
PYTHON_IMPLEMENTATION = "python_implementation"
PYTHON_ISORT = "python_isort"
PYTHON_PYPROJECT_TOML = "python_pyproject_toml"
PYTHON_SETUP_CFG = "python_setup_cfg"
PYTHON_SETUPTOOLS = "python_setuptools"

TERRAFORM = "terraform"

# full list of tokens

TOKENS = [token for token in dict(globals()).items() if not token[0].startswith("_")]
