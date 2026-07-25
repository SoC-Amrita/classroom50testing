import test as testImport
import pytest
@pytest.mark.parametrize("n", range(100))
def test_answer(n):
    assert testImport.squareOfn(n) ==n * n
