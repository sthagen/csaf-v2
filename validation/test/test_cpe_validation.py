# -*- coding: utf-8 -*-
# pylint: disable=import-error,missing-docstring,unused-import,reimported
import json
import pytest  # type: ignore
import cpe_validation


def test_cli_encoding_ok():
    assert cpe_validation.ENCODING == "utf-8"


def test_cli_main_uri_ok():
    assert 0 == cpe_validation.main(["cpe:/"], True)


def test_cli_main_sfb_ok():
    assert 0 == cpe_validation.main(["cpe:2.3"], True)


def test_cli_main_nok_user():
    assert 2 == cpe_validation.main([], True)


def test_cli_main_nok_data():
    assert 1 == cpe_validation.main(["{"], True)


def test_cli_main_nok_file():
    message = r"\[Errno 2\] No such file or directory: '{'"
    with pytest.raises(FileNotFoundError, match=message):
        cpe_validation.main(["{"], False)
