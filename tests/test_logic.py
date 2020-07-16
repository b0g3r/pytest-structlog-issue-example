import pytest

from example import logic


@pytest.mark.parametrize(
    'a',
    [
        # ok
        1,
        # events is empty
        2,
        # events is empty
        3,
    ],
)
def test_hard_work(a, log):
    logic.hard_work(a)
    assert log.events
    assert log.has('very_important_event')