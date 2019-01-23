
"""
An example test module.
Steps to tdd:
1. Create a tests folder
2. Create an init file
3. Create a file
"""
def test_the_truth():
    """Assert the turh!"""
    # pass
    assert False

def test_the_math():
    num = 3
    if num > 0:
        raise Exception("Nope")
