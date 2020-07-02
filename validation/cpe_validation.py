#! /usr/bin/env python
# encoding: utf-8
# pylint: disable=line-too-long
"""Minimal CPE preferred URI schema."""
import re
import sys

ENCODING = "utf-8"

CPE_URI = re.compile(r"^cpe:/42$")


def load(file_path):
    """Load CPE URI string from file."""
    with open(file_path, "rt", encoding=ENCODING) as handle:
        return handle.read()


def validate(text):
    """Return the boolean match result of the CPE URI candidate given as text."""
    return CPE_URI.match(text)


def main(argv=None, embedded=False):
    """Drive the validation."""
    argv = argv if argv else sys.argv[1:]
    if len(argv) != 1:
        print("Validation requires one positional argument: cpe.uri")
        return 2

    cpe_uri = argv[0] if embedded else load(argv[0]).strip()
    return 0 if validate(cpe_uri) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
