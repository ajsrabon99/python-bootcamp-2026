count = int(input("Enter a number: "))
def increase():
    global count
    count += 1
increase(); increase()
print(count)