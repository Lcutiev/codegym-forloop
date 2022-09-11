# import sys
# from pprint import pprint

# pprint(sys.path)

# sys.path.insert(0, "/Users/vai1hc/ocuments/Codegym/Module")
# pprint(sys.path)

# import importlib.util       
# spec = importlib.util.spec_from_file_location("a", "/Users/vai1hc/Documents/Codegym/Module/delete/note.py")   
# a = importlib.util.module_from_spec(spec)       
# spec.loader.exec_module(a)
# a.delete()

# def print_helloword():
#     print("\nHello Word!"*3)

# print_helloword()

# def input_info():
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))

# input_info()

# def count_sum(a,b):
#     print("1st number: ", a)
#     print("2nd number: ", b)
#     print("The sum of",a,"+", b,"=", a+b)

# count_sum(2, 5)
# Fin prime numbers from 1 to N
# num = int(input("Enter any number: "))
# print("Prime numbers from 1 to", num)
# for primeNum in range (1, num+1):
#     if primeNum > 1:
#         for i in range (2, primeNum):
#             if primeNum % i == 0:
#                 break
#         print(primeNum, end = " ")


# num = int(input("Enter any number: "))
# isPrime = True
# for i in range (2, num+1):
#     if num % i == 0:
#         isPrime = False
#         break
# if isPrime:
#     print(num, end = " ")

a = 1
b = 10
for number in range(a, b + 1):
    is_so_nguyen_to = True
    if number < 2:
        continue
    for i in range(2, number):
        if number % i == 0:
            is_so_nguyen_to = False
            break
    if is_so_nguyen_to:
        print(str(number) + " " + "đây là số nguyên tố")