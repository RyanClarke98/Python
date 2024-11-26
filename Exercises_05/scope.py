my_string = "global"

def my_function():
    my_string = "enclosing"
    def nested_function():
        my_string = "local"
        print(my_string)
    nested_function()
    return my_string

# Print the variable my_string
print(my_string)
# Print the output of the function, my_function
print(my_function())


"""
the global mystring is never changed :
First, it prints "global" (the global my_string).
Then it prints "local" (from nested_function).
Finally, it prints "enclosing" (from my_function).
"""