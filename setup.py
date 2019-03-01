#!/usr/bin/env python
"""
Setup package.
"""
import io
import os
from setuptools import setup

# Get long description from readme
with io.open("README.md", "rt", encoding="utf8") as readmefile:
    readme = readmefile.read()

setup(
    name="py-commit-checker",
    version="0.2.1",
    description="Basic commit checker, with optional emoji check",
    author="Noah Pendleton",
    author_email="2538614+noahp@users.noreply.github.com",
    url="https://github.com/noahp/py-commit-checker",
    project_urls={
        "Code": "https://github.com/noahp/py-commit-checker",
        "Issue tracker": "https://github.com/noahp/py-commit-checker/issues",
    },
    long_description=readme,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=["py_commit_checker"],
    # yolo least specifiers, probably break eventually
    install_requires=["click>=6.5", "emoji>=0.5.1", "gitpython>=2.1.11"],
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
