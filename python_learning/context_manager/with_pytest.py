import pytest

"""
Test for Exceptions
Unittest to capture if the assertion is raised
"""

with pytest.raises(ZeroDivisionError):
    var = 1 / 0

with pytest.raises(ZeroDivisionError):
    x = 2 / 4
