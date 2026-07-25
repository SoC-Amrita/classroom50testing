import pytest
import test as testImport
def grade():
  for i in range(100):
    assert(testImport.squareOfn(i) == i**2)
  
