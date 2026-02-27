print("Geometric Progression Tracker")

a = int(input("Enter first term: "))
r = int(input("Enter ratio: "))
n = int(input("Enter terms: "))

i = 1
sum_total = 0

while i <= n:
    term = a * (r ** (i - 1))
    sum_total = sum_total + term

    if term % 2 == 0:
        print("Even term:", term)
    else:
        print("Odd term:", term)

    i = i + 1

print("Total sum:", sum_total)

if r == 1:
    print("Constant series")
else:
    print("Changing series")