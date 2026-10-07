#variable length arguments 
def function(*args):
    print("Arguments passed:", args)
    print("Number of arguments:", len(args))
    print("---------")
    function(1, 2, 3)
    print("---------")
    function('a', 'b', 'c', 'd')