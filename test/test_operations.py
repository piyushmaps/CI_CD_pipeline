from src.maths_operations import sum,subtract

def test_add():
    assert sum(2,3)==5
    assert sum(-1,1)==0

def test_subtract():
    assert subtract(4,3)==1
    assert subtract(5-9)==-4