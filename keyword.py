#keyword arguments
def function(**kwargs):
    print("Keyword arguments passed:", kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

function(name="Alice", age=30)
print("---------")
function(city="New York", country="USA")