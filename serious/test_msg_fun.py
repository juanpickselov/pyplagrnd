import pytest


@pytest.fixture(params=["hello", "bonjour"])
def say_it(request):
    the_msg = request.param
    yield the_msg


@pytest.mark.squirrel
def test_msg(say_it):
    assert type(say_it) == str
