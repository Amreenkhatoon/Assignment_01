#odd day

#sample number
numbers = (1,2,3,4,5,6,7,8,9)

#initialize counters for even and odd
even_count = 0
odd_count = 0

#iterate
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("number of even numbers:", even_count)
print("number of even numbers:", odd_count)
