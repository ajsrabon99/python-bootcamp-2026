fname = "AJ"
lname = "Srabon "
fullname = "%s %s"%(fname, lname)
print(fullname.lower())
print(fullname.swapcase())
print(fullname.title())

#replace 

name = "hello python"
new = name.replace("python", "srabon")
print(new)

#string to list (split)
h = "hello python"
print(h.split())

#count
tedxt = "aj "


numbers = [1, 2,3,5,10]
max_num = max(numbers)
print(max_num)

#linear search
abcd = [1, 2, 3, 4, 5, 10, 12, 29, 33]
max_ = float('-inf')
for n in abcd:
    if n > max_:
        max_ = n
print(max_)


