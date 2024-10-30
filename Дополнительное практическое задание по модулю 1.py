grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
GPA = {}
grades_gpa = []


for sub in grades:
    gpa = sum(sub)/len(sub)
    grades_gpa.append(gpa)
    

for a, b in enumerate(sorted(list(students))):
    GPA[b]=grades_gpa[a]
    

print(GPA)