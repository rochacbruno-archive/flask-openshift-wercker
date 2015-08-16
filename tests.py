import pytest
from flask import jsonify
from app import calc, api


@pytest.fixture
def app():
    return api


def test_sum(app):
    assert calc('sum', 1, 2).data == jsonify({'result': 3}).data


def test_mul(app):
    assert calc('mul', 5, 3).data == jsonify({'result': 15}).data


def test_sub(app):
    assert calc('sub', 10, 5).data == jsonify({'result': 5}).data


def test_div(app):
    assert calc('div', 10, 2).data == jsonify({'result': 5}).data
