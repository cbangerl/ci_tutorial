import numpy as np
from myfun import mysum
from myfun import myprod

def test_myfun():
    testData = np.arange(2,5)
    resultSum = 9
    resultProd = 24

    testSum = mysum(testData)
    assert testSum  == resultSum

    testProd = myprod(testData)
    assert testProd == resultProd