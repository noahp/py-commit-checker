[![Code style:
black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)](https://github.com/ambv/black)
[![GitHub Workflow
Status](https://img.shields.io/github/workflow/status/noahp/py-commit-checker/main-ci?style=for-the-badge)](https://github.com/noahp/py-commit-checker/actions)
[![PyPI
version](https://img.shields.io/pypi/v/py-commit-checker.svg?style=for-the-badge)](https://pypi.org/project/py-commit-checker/)
[![PyPI
pyversions](https://img.shields.io/pypi/pyversions/py-commit-checker.svg?style=for-the-badge)](https://pypi.python.org/pypi/py-commit-checker/)
[![License:
MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

# 📝 py-commit-checker

A basic git commit message format checker.

_Note: check out https://github.com/jorisroovers/gitlint for a much better,
more featureful, and actually tested implementation! the only unique feature in
`py-commit-checker` is the built in leading emoji check... 😀_

# Checkers

Small set of mandatory (cannot be disabled) and optional (opt in or out) checkers.

## Always enabled

These checks are always enabled:

1. mandatory blank second line (delimiting title + body of message)

## Optional

These checks can be set to on or off using command line args:

1. [50/72](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)
   rule checking (configurable lengths)
2. [leading emoji](https://gitmoji.carloscuesta.me/) check

Returns non-zero in case of any violation

# Install

```bash
pip install py-commit-checker
# note: you'll need git installed for the gitpython dependency to work!
```

# Usage

```bash
# check top commit for 50/72 + emoji compliance on HEAD
py-commit-checker --emojis

# check a specific commit
py-commit-checker --emojis --commit HEAD~2

# check a repo at a path other than cwd
py-commit-checker --repo-path ../openbsd

# check a range of commits; py-commit-checker-branch helper script (installed
# alongside py-commit-checker)
PY_COMMIT_CHECKER_ARGS='--emojis' py-commit-checker-branch origin/master
```

# Why is this not just a single regex

Because I was too lazy to figure out how to exclude URI elements from the body
line length check in regex 🐸☕.

Also distributing with pypi is pretty convenient 😀

# Tests

This package uses tox. To run the tests locally:

```bash
pip install tox==3.7.0  # minimum supported version

tox --parallel auto  # run tox in parallel
```

This is a py2+3 universal package; it's recommended you install python3.6 with
whatever your system package manager is, if it isn't already installed, so tox
can run the checks for that too.

Tox will enforce 100% [pylint](https://www.pylint.org/) compliance, and
[black](https://github.com/ambv/black) formatting compliance.

# License

MIT.
