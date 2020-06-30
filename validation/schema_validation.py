#! /usr/bin/env python
# encoding: utf-8
# pylint: disable=line-too-long
"""Minimal JSON schema validation."""
import json
import sys

from jsonschema import draft7_format_checker, validate

ENCODING = "utf-8"


def document(file_path):
    """Create JSON object from file."""
    with open(file_path, "rt", encoding=ENCODING) as handle:
        return json.load(handle)


def main(argv=None):
    """Drive the validation."""
    argv = argv if argv else sys.argv[1:]
    if len(argv) != 2:
        print("Validation requires two positional arguments: schema.json document.json")
        return 2

    json_schema_path, json_document_path = argv[0], argv[1]
    validate(document(json_document_path), document(json_schema_path), format_checker=draft7_format_checker)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
