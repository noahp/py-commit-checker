#!/usr/bin/env python
"""
Setup package.
"""
import io

from setuptools import setup

# Get long description from readme
with io.open("README.md", "rt", encoding="utf8") as readmefile:
    README = readmefile.read()


def get_version():
    """Get version spec from module"""
    from py_commit_checker.__version__ import (  # pylint: disable=bad-option-value,import-outside-toplevel
        __version__,
    )

    return __version__


setup(
    name="py-commit-checker",
    version=get_version(),
    description="Basic commit checker, with optional emoji check",
    author="Noah Pendleton",
    author_email="2538614+noahp@users.noreply.github.com",
    url="https://github.com/noahp/py-commit-checker",
    project_urls={
        "Code": "https://github.com/noahp/py-commit-checker",
        "Issue tracker": "https://github.com/noahp/py-commit-checker/issues",
    },
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=["py_commit_checker"],
    # yolo non-precise specifiers, probably break eventually
    install_requires=["click>=6.5", "emoji==1.2.*", "gitpython>=2.1.11"],
    entry_points={
        "console_scripts": [
            "py-commit-checker=py_commit_checker.py_commit_checker:main"
        ]
    },
    scripts=["py-commit-checker-branch"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
)
