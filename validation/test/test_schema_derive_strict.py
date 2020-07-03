# -*- coding: utf-8 -*-
# pylint: disable=import-error,missing-docstring,unused-import,reimported
import json
import pytest  # type: ignore
import schema_derive_strict


def test_cli_encoding_ok():
    assert schema_derive_strict.ENCODING == "utf-8"


def test_cli_main_ok():
    assert 0 == schema_derive_strict.main(["{}"], True)


def test_cli_main_nok_user():
    assert 2 == schema_derive_strict.main([], True)


def test_cli_main_nok_data():
    message = "'Expecting property name enclosed in double quotes: line 1 column 2 (char 1)'"
    with pytest.raises(json.decoder.JSONDecodeError):  #, match=message):
        schema_derive_strict.main(["{"], True)


def test_cli_main_nok_file():
    message = r"\[Errno 2\] No such file or directory: '{'"
    with pytest.raises(FileNotFoundError, match=message):
        schema_derive_strict.main(["{"], False)
