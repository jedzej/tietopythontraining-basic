import pytest
from regex_version_of_strip import strip_regex


@pytest.mark.parametrize("work_string, chars_to_delete", [
    ("match beginning", "ma"),
    ("match ending", "ng"),
    (" space at the beginning", ""),
    (" space at the end", ""),
    (" spaces around me ", ""),
    ("ABCCBA", "AB"),
    ("ABCCBA", "BA"),
    ("ABABCCCBABA", "BA"),
    ("some some random some", "some"),
    ("function works very well, so much fun", "nuf"),
])
def test_eval(work_string, chars_to_delete):
    assert strip_regex(work_string, chars_to_delete) \
        == work_string.strip(chars_to_delete)
