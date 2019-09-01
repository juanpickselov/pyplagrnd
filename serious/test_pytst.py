import pytest


@pytest.mark.skip("If this runs it's pointless")
def test_true():
    assert True


@pytest.mark.skip("Test will not run")
def test_false():
    assert False


def test_key():
    a = ['a', 'b']
    b = ['b']
    assert a == b


@pytest.mark.squirrel
def test_key_two():
    a = ['a', 'b']
    b = ['a', 'b']
    assert a == b


@pytest.mark.squirrel
def test_key_three():
    x = [1, 2, 3]
    y = [1, 2, 3]
    assert x == y


def test_skip_at_runtime():
    if True:
        pytest.skip("Finally I don't want to run it")
