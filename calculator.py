"""
A calculator library.
"""
# original
# def add(value1, value2):
#     # return 6: this would give us an error
#     return value1 + value2

def add(*args):
    answer = 0
    for value in args:
        answer += value
    return answer
