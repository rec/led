#binaryGrayConvert.py
#two functions to convert to and from gray codes

import functools

def fill(b, width=0):
    return b if len(b) >= width else '0' * (width - len(b)) + b

def to_bin(x):
    return bin(x)[2:]

def from_bin(s):
    return int(s, 2)

def bin_wrapper(f):
    @functools.wraps(f)
    def wrapper(x):
        return from_bin(f(to_bin(x)))
    return wrapper

# http://joshuac.com/margins/gray_code_conversion.html
def grayToBinary(gray):
    """converts a given gray code to its binary number"""
    binary = gray[0]
    i = 0
    while( len(gray) > i + 1 ):
        binary += `int(binary[i]) ^ int(gray[i + 1])`
        i += 1
    return binary

def binaryToGray(binary):
    """converts a given binary number to is gray code"""
    gray= ""
    i = -1
    while( len(binary) > -i ):
        gray = `int(binary[i - 1]) ^ int(binary[i])` + gray
        i -= 1
    gray = binary[0] + gray
    return gray

gray_to_binary = bin_wrapper(grayToBinary)
binary_to_gray = bin_wrapper(binaryToGray)

BIT_NUMBER = 10
INT_MAX = 2 ** 10
BINARY_REV = [fill(to_bin(i), BIT_NUMBER) for i in xrange(INT_MAX)]
GRAY_REV = [binaryToGray(b) for b in BINARY]

BINARY = [b[::-1] for b in BINARY_REV]
GRAY = [b[::-1] for b in GRAY_REV]
