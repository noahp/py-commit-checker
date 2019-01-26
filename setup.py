#!/usr/bin/env python
"""
Setup package.
"""
import sys
import os
from setuptools import setup


def get_long_description():
    """Fetch long description from README.md adjacent to this file"""
    readme_file_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "README.md"
    )
    if sys.version_info < (3, 4):
        with open(readme_file_path, "r") as readmefile:
            desc = readmefile.read()
    else:
        with open(readme_file_path, encoding="utf-8") as readmefile:
            desc = readmefile.read()
    return desc


setup(
    name="py-commit-checker",
    version="0.0.0",
    description="Basic commit checker, with optional emoji check",
    author="Noah Pendleton",
    author_email="2538614+noahp@users.noreply.github.com",
    url="https://github.com/noahp/py-commit-checker",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    packages=["py_commit_checker"],
    install_requires=["click==7.*", "emoji==0.5.*", "gitpython==2.*"],
    entry_points={
        "console_scripts": [
            "py-commit-checker=py_commit_checker.py_commit_checker:main"
        ]
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ],
)
