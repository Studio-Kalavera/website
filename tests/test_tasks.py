"""Tasks tests."""

import pytest

from tasks import pelican_run


@pytest.fixture(name="pelican_main")
def pelican_main_fixture(mocker):
    """Pelican main mock."""
    return mocker.patch("tasks.pelican_main", autospec=True)


@pytest.fixture(name="program")
def program_fixture(mocker):
    """Invoke program mock."""
    program = mocker.patch("tasks.program")
    program.core.remainder = ""


def test_pelican_run(pelican_main, program):
    """Test pelican_run."""
    pelican_run("-s publishconf.py")
    pelican_main.assert_called_once_with(["-s", "publishconf.py"])
