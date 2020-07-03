# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import schema_validation


def test_cli_encoding_ok():
    assert schema_validation.ENCODING == "utf-8"


def test_cli_main_nok():
    assert 1 == schema_validation.main(["{}", "{}"], True)
