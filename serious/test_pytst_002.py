import pytest


def test_true():
    assert "alpha" == "alpha"


@pytest.mark.skip("Test will not run")
def test_false():
    assert False


def test_key_four():
    a = ['a', 'b']
    b = ['b']
    assert a == b


@pytest.mark.squirrel
def test_key_five():
    a = ['a', 'b']
    b = ['a', 'b']
    assert a == b


@pytest.mark.squirrel
def test_key_six():
    x = [1, 2, 3]
    y = [1, 2, 3]
    assert x == y


def test_skip_runtime_again():
    if True:
        pytest.skip("Finally I don't want to run it")
