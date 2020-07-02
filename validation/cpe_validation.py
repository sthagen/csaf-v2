#! /usr/bin/env python
# encoding: utf-8
# pylint: disable=line-too-long
"""Minimal CPE preferred URI schema.

The current REGEX is nearly meaningless, maybe like many CPE URI strings out for real ;-)

It matches all 1001 ABNF derived (positive) test cases ...
"""
import re
import sys

ENCODING = "utf-8"

CPE_URI = re.compile(r"^cpe:/[^:]*:?[^:]*:?[^:]*:?[^:]*:?[^:]*:?[^:]*:?[^:]*$", re.I)


def load(file_path):
    """Load CPE URI string from file."""
    with open(file_path, "rt", encoding=ENCODING) as handle:
        return handle.read()


def validate(text):
    """Return the boolean match result of the CPE URI candidate given as text.

    Implementation Notes:

    * Supports the URI binding representation of the WFN
    * Does not support the formatted string binding (FSB) representation

    Examples:

    * WFN: wfn:[part="a",vendor="v",product="p",version="2020\\.01\\.23",update="alpha"]
    * URI: cpe:/a:v:p:2020.01.23:alpha
    * FSB: cpe:2.3:a:v:p:2020.01.23:alpha:*:*:*:*:*:*
    """
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
