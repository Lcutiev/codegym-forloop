my_num = input("Enter any number: ")
my_list = [int(fizzbuzz) for fizzbuzz in str(my_num)]

for fizzbuzz in my_list:
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
print(fizzbuzz)