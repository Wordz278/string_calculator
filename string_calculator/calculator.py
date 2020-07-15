import re
import pytest

def add(numberString):
    if not numberString:
        return 0
    if numberString.isdigit() and int(numberString) > 0:
        return int(numberString)
    input_list = delimeters(numberString)
    return negatives_not_allowed(input_list)

def negatives_not_allowed(numberString):
    total = 0
    negatives = []
    for num in numberString:
        num = int(num)
        if num < 0:
            negatives.append(num)
        if num > 1000 or num < 0:
            continue
        total += int(num)
    if len(negatives) > 0:
        raise ValueError("Negatives not allowed " + str(negatives))
    return total

def delimeters(numberString):
    if numberString[0:2] == "//":
        numberString = numberString.split("\n")[1]
    return re.split("[^0-9-]+", numberString)


if __name__ == '__main__':
    try:
        print(add(""))
        print(add("1,1"))
        print(add("1,2,3,4"))
        print(add("1\n2,3" ))
        print(add("//;\n1;2"))
        print(add("-1,-2,3,4"))
    except(ValueError) as error:
        print(error)