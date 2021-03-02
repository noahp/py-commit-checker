#!/usr/bin/env python
"""
Simple commit checker.
"""

from __future__ import print_function, absolute_import

import re
import sys

import click
import emoji

import git
from py_commit_checker.__version__ import __version__

# Regex pattern used to locate the emoji character in a title line
EMOJI_REGEX_PLACEHOLDER = "(?P<emoji>.)"


def checker_msg(condition, msg):
    """Print error message and exit non-zero if condition is truthy-false"""
    if not condition:
        click.echo(click.style(msg, fg="red", bold=True))
        sys.exit(-1)


def get_commit_msg_lines(repo, commit):
    """Return iterator of commit message lines for given repo path and commit"""
    commit_msg = repo.commit(commit).message
    return commit_msg.splitlines()


def check_line_lengths(
    commit_msg_lines, yes_check_line_lengths, line_length_title, line_length_body
):
    """Validate line lengths. Returns (True, "") for pass, (False, "error msg") for failure"""

    # manually check each line instead of single-pass regex, so we can exclude
    # URI strings in body lines from the line length check.

    # check that second line in the message is blank
    if len(commit_msg_lines) > 1 and commit_msg_lines[1]:
        return (False, "Second line is not blank")

    if yes_check_line_lengths:
        # check title line length
        if len(commit_msg_lines[0]) > line_length_title:
            return (
                False,
                "Title line too long, {} > {}".format(
                    len(commit_msg_lines[0]), line_length_title
                ),
            )

        if len(commit_msg_lines) > 2:
            # check body line lengths
            uri_re = re.compile(r"\w+:[^\s]+$")
            for line in commit_msg_lines[2:]:
                if len(line) > line_length_body:
                    # uri's that exceed the body line length are exceptions to the max-len check
                    uri = uri_re.match(line)
                    if not uri or len(uri.group(0)) < line_length_body:
                        return (
                            False,
                            u"Body line too long, {} > {}\n  > {}".format(
                                len(line), line_length_body, line
                            ),
                        )

    return (True, "")


def check_emoji(line, emoji_regex):
    """Validate emoji position. Returns True for pass, False for failure"""
    emoji_char = re.match(emoji_regex, line)

    if not (emoji_char and emoji_char.group("emoji")):
        checker_msg(
            False,
            (
                u"Error matching emoji with:\n regex= '{}'\n line= '{}'\n"
                u"Make sure you have {} in your expression"
            ).format(emoji_regex, line, EMOJI_REGEX_PLACEHOLDER),
        )
        raise AssertionError(
            "Error matching for emoji, check your regex: '{}'".format(emoji_regex)
        )

    return emoji_char.group("emoji") in emoji.UNICODE_EMOJI["en"]


# pylint: disable=too-many-arguments
@click.command()
@click.version_option()
@click.option(
    "--commit", "-c", help="Commit-ish to check", type=click.STRING, default="HEAD"
)
@click.option(
    "--repo-path", "-r", help="Path to the repo", type=click.STRING, default="./"
)
@click.option("--emojis", "-e", help="Enable check for leading emoji", is_flag=True)
@click.option(
    "--emoji-regex",
    "-m",
    help=(
        """(Python) regex specifying how the emoji should be positioned in the title line. \
Use '{placeholder}' as the placeholder for the emoji character. Examples:
\b
 'JIRA-1234: <emoji>' : '^[A-Z]+-[0-9]+: {placeholder}'
 'docs: <emoji>' : '^\\w+: {placeholder}'
\b
"""
    ).format(placeholder=EMOJI_REGEX_PLACEHOLDER),
    type=click.STRING,
    default="^{}".format(EMOJI_REGEX_PLACEHOLDER),
    show_default=True,
)
@click.option(
    "--line-length/--no-line-length",
    "-l",
    help="Control check for line length",
    default=True,
    show_default=True,
)
@click.option(
    "--line-length-title",
    "-t",
    help="First line length setting",
    type=click.INT,
    default=50,
    show_default=True,
)
@click.option(
    "--line-length-body",
    "-b",
    help="Commit body line length setting",
    type=click.INT,
    default=72,
    show_default=True,
)
@click.option(
    "--check-merge-commits",
    help="Also check commits with multiple parents",
    is_flag=True,
)
def main(
    commit,
    repo_path,
    emojis,
    emoji_regex,
    line_length,
    line_length_title,
    line_length_body,
    check_merge_commits,
):
    """Basic git commit checker written in python."""

    # open the repo
    repo = git.Repo(repo_path)
    commit_obj = repo.commit(commit)

    # if the specified commit is a merge commit, exit
    if not check_merge_commits and len(commit_obj.parents) > 1:
        click.echo(
            click.style("Not checking merge commit {}".format(commit), bold=True)
        )
        sys.exit(0)

    # get the commit message lines
    commit_msg_lines = commit_obj.message.splitlines()

    checker_msg(
        *check_line_lengths(
            commit_msg_lines, line_length, line_length_title, line_length_body
        )
    )

    if emojis:
        # enforce leading emoji
        checker_msg(
            check_emoji(commit_msg_lines[0], emoji_regex),
            u"No emoji in title line matching '{}':\n  > {}".format(
                emoji_regex, commit_msg_lines[0]
            ),
        )

    # checkers passed!
    click.echo(click.style("All good!", fg="green", bold=True))


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
