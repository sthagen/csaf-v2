#! /usr/bin/env python
# encoding: utf-8
# pylint: disable=line-too-long
"""Derivation of strict variant from JSON schema."""
import json
import sys

import jsonpath_rw  # type: ignore

ENCODING = "utf-8"


def load(file_path):
    """Create JSON object from file."""
    with open(file_path, "rt", encoding=ENCODING) as handle:
        return json.load(handle)


def main(argv=None):
    """Drive the validation."""
    argv = argv if argv else sys.argv[1:]
    if len(argv) != 1:
        print("Derivation requires one positional argument: schema.json")
        return 2

    json_schema_path = argv[0]
    schema = load(json_schema_path)
    for place in jsonpath_rw.parse("$..* where properties").find(schema):
        place.value["additionalProperties"] = False

    sys.stdout.write(json.dumps(schema, sort_keys=True, indent=2))
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
