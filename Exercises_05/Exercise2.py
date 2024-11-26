def find_num(number_list: list, number: int)->bool:
    for iterate_number in number_list:
        if iterate_number == number:
            return True
        else:
            return False

result = find_num([1,2,3,4,5,6,7,8],9)
print(result)

# The reason for value of None is when the number is not found in the list 
# The result will be true when the number outside the number_list is whithin the function 
# example if number 8 was outside it would result in true
