count = 0
print("The odd numbers from 1 to 10 are ")
while count < 10:
    count += 1
    if count % 2 == 1:
        continue
    print(count)
