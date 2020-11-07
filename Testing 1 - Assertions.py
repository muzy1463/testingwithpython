"""We make simple assertions with assert
assert accepts an expression
Returns None if the expression is true
Raises an AssertionError if it is falsy
Accepts an optional error message as a second argument
"""



def eat_junk(food):
    assert food in ["pizza", "ice cream", "candy", "fried butter"], "It is not a Junk food!"
    return f"NOM NOM NOM I'M EATIN"


print(eat_junk("O"))

def add_positive_numbers(x,y):
    assert x>0 and y>0, "Both numbers must be positive!"
    return x+y



print(add_positive_numbers(1,6))
add_positive_numbers(1, -5)

assert 4 == 4
assert 4 == 7


#if assert is true, nothing happens. if false, it gives error.

