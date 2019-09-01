import os
import pytest


@pytest.fixture(autouse=True)
def change_user_env():
    current_user = os.environ.get("USER")
    os.environ["USER"] = "foobar"
    yield
    os.environ["USER"] = current_user


@pytest.mark.squirrel
def test_user():
    assert os.getenv("USER") == "foobar"
