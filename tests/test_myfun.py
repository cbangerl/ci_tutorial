import numpy as np
from myfun import mysum
from myfun import myprod

def test_mysum():
    testData = np.arange(2,6)
    resultSum = 14


    testSum = mysum(testData)
    assert testSum  == resultSum

def test_myprod():
    testData = np.arange(2, 5)
    resultProd = 24

    testProd = myprod(testData)
    assert testProd == resultProd