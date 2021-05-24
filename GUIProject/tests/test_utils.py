import string
from pathlib import Path

import pytest
from guiproject.utils import splitted_line, get_index

PATH = Path(__file__).parent


@pytest.fixture
def example_text():
    with open(PATH / "text.txt") as file:
        yield file.read()


def test_get_index():

    indices = get_index([8, 10, 12, 15, 18], 14)

    assert indices == 12

    indices = get_index([8, 10, 12, 15, 18], 7)

    assert indices == 8

    indices = get_index([], 7)

    assert indices is None




@pytest.mark.parametrize("width", [8])
def test_splitting_lines(example_text, width):
    formatted_text = splitted_line(example_text, width)

    print()
    print(formatted_text)

    for line in formatted_text.splitlines():

        if string.whitespace in line:
            pass
        else:
            assert len(line) <= width