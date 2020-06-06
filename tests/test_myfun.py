import numpy as np
from myfun import mysum
from myfun import myprod
import re



def test_mysum():
    testFile = open("./tests/testData.txt", "r")
    fileString = testFile.readlines()
    numbersString = fileString[0]
    testString = re.sub("[^0-9,.]","",numbersString).split(",")
    testData=[float(item) for item in testString]
    testData = np.array(testData)
    resultSum = float(re.sub("[^0-9.,]","",fileString[1]))


    testSum = mysum(testData)
    assert testSum  == resultSum

