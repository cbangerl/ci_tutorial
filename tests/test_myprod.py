import numpy as np
from myfun import myprod


def test_myprod():
    testData = np.arange(2, 5)
    resultProd = 24

    testProd = myprod(testData)
    assert testProd == resultProd