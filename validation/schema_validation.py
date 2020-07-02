#! /usr/bin/env python
# encoding: utf-8
# pylint: disable=line-too-long
"""Minimal JSON schema validation."""
import json
import sys

import jsonschema  # type: ignore

ENCODING = "utf-8"


def load(file_path):
    """Create JSON object from file."""
    with open(file_path, "rt", encoding=ENCODING) as handle:
        return json.load(handle)


def validate(document, schema, conformance=None):
    """Validate the document against the schema."""
    conformance = conformance if conformance else jsonschema.draft7_format_checker
    return jsonschema.validate(document, schema, format_checker=conformance)


def main(argv=None, embedded=False):
    """Drive the validation."""
    argv = argv if argv else sys.argv[1:]
    if len(argv) != 2:
        print("Validation requires two positional arguments: schema.json document.json")
        return 2

    schema = json.loads(argv[0]) if embedded else load(argv[0])
    document = json.loads(argv[1]) if embedded else load(argv[1])

    return 0 if validate(document, schema) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
