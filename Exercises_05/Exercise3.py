def even_number(number_list:list) -> bool:
    for number in number_list:
        if number % 2 == 0: # check if number is even
            return True
        else:
            return False
        
number = [2, 3, 5, 7, 8]
result = even_number(number)
print(result)  # Result = True because 2 and 8 are even numbers

# change numbers [1 ,3 ,5, 7,] will result False 


# Lambda function to calculate the volume of a cylinder
cylinder_volume = lambda r, h: 3.141592653589793 * r**2 * h  

# Example usage
radius = 3
height = 5
volume = cylinder_volume(radius, height)
print(volume)  # This will print the volume of the cylinder
