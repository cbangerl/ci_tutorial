import numpy as np
from myfun import mysum


def test_mysum():
    testData = np.arange(2,5)
    resultSum = 9


    testSum = mysum(testData)
    assert testSum  == resultSum