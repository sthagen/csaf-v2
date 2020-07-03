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


def derive(schema):
    """Derive the strict schema."""
    for place in jsonpath_rw.parse("$..* where properties").find(schema):
        place.value["additionalProperties"] = False
    return schema


def main(argv=None, embedded=False):
    """Drive the validation."""
    argv = argv if argv is not None else sys.argv[1:]
    if len(argv) != 1:
        print("Derivation requires one positional argument: schema.json")
        return 2

    schema = json.loads(argv[0]) if embedded else load(argv[0])

    strict = derive(schema)

    sys.stdout.write(json.dumps(strict, sort_keys=True, indent=2))
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
