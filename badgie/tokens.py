ANSIBLE = "ansible"
ANSIBLE_COLLECTION = "ansible_collection"
ANSIBLE_GALAXY = "ansible_galaxy"
ANSIBLE_LINT = "ansible_lint"
ANSIBLE_ROLE = "ansible_role"

BRETTOPS = "brettops"
BRETTOPS_CONTAINER = "brettops_container"
BRETTOPS_PACKAGE = "brettops_package"
BRETTOPS_PIPELINE = "brettops_pipeline"
BRETTOPS_ROLE = "brettops_role"
BRETTOPS_TOOL = "brettops_tool"

DETECT_SECRETS = "detect_secrets"  # pragma: allowlist secret

GIT = "git"

GITHUB = "github"
GITHUB_ACTIONS = "github_actions"

GITLAB = "gitlab"
GITLAB_CI_FILE = "gitlab_ci_file"
GITLAB_COVERAGE = "gitlab_coverage"
GITLAB_ENVIRONMENT = "gitlab_environment"
GITLAB_LICENSE = "gitlab_license"
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
PYTHON_BANDIT = "python_bandit"
PYTHON_BLACK = "python_black"
PYTHON_DOCFORMATTER = "python_docformatter"
PYTHON_IMPLEMENTATION = "python_implementation"
PYTHON_ISORT = "python_isort"
PYTHON_MYPY = "python_mypy"
PYTHON_PYPROJECT_TOML = "python_pyproject_toml"
PYTHON_SETUP_CFG = "python_setup_cfg"
PYTHON_SETUPTOOLS = "python_setuptools"

SHELL_SHFMT = "shell_shfmt"

TERRAFORM = "terraform"
TERRAFORM_MODULE = "terraform_module"
TERRAFORM_PROVIDER = "terraform_provider"
TERRAFORM_WORKSPACE = "terraform_workspace"

# full list of tokens

TOKENS = [token for token in dict(globals()).items() if not token[0].startswith("_")]
