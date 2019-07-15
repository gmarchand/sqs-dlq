import pytest
import retry


def test_handler(mocker):
    retry.handler({}, None)
