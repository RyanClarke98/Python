a = "Greetings!"
print(a[0:4:1]) ## 0 = First letter = G, Print first 4 letters 

a = "Greetings!"
print(a[-1:-5:-1]) ## print a slicing of the latst letters 

a = "Greetings!"
print (a[5]) ## printing a single character 

a = "Ryan"
first_letters = a[0:2:1]
last_letter = a[-1]
insert_letter = "a"
b = first_letters + insert_letter + last_letter
print(b)