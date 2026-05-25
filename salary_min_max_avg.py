salary = [67000, 45000, 78000, 55000, 28000]
minimum = salary[0]
maximum = salary[0]
total = 0
for i in salary:
    total = total + i

    if i < minimum:
        minimum = i

    if i > maximum:
        maximum = i

average = total / len(salary)

print("Minimum salary:", minimum)
print("Maximum salary:", maximum)
print("Average salary:", average)

'''
output:
Minimum salary: 28000
Maximum salary: 78000
Average salary: 54600.0
'''

