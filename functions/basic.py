
# taking multiple parameters using *args
def multiple_item(*args):
    print(args)
    print(type(args))

multiple_item("Dave", "John", "sara")
# the input we give in *args are stured as a tuple 
print("\n")
def multi_named_item(**kwargs): # known for "Key word arguments"
    print(kwargs)
    print(type(kwargs))

multi_named_item(first = "Dave", second = "John",third = "sara")