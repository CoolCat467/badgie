from setuptools import find_packages, setup

# injected version
__version__ = "0.0.0"

# markdown readme
long_description = open("README.md").read()

# read requirements from requirements.in
install_requires = open("requirements.in").read().splitlines()

setup(
    name="badgie",
    version=__version__,
    author="Brett Weir",
    author_email="brett@brettops.io",
    description="Add all the badges with Badgie!",
    license="MIT",
    url="https://gitlab.com/brettops/tools/badgie",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "badgie = badgie.__main__:main",
        ],
    },
    install_requires=install_requires,
    python_requires=">=3.10",
    keywords="badge template markdown",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Documentation",
    ],
)
