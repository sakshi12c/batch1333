salary = [25000, 40000, 15000, 60000, 30000, 50000]


min_sal = salary[0]
max_sal = salary[0]

for i in salary:
    if i < min_sal:
        min_sal = i
    if i > max_sal:
        max_sal = i

#  second minimum
second_min = max_sal
for i in salary:
    if i != min_sal and i < second_min:
        second_min = i

#  find second maximum
second_max = min_sal
for i in salary:
    if i != max_sal and i > second_max:
        second_max = i

print("Second Minimum Salary:", second_min)
print("Second Maximum Salary:", second_max)

'''
output:
Second Minimum Salary: 25000
Second Maximum Salary: 50000
'''