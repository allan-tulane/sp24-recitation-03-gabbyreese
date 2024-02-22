from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(7), BinaryNumber(4)) == 7*4
    assert quadratic_multiply(BinaryNumber(5), BinaryNumber(2)) == 5*2
    assert quadratic_multiply(BinaryNumber(1), BinaryNumber(5)) == 1*5
    assert quadratic_multiply(BinaryNumber(6), BinaryNumber(4)) == 6*4
