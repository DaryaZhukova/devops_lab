students = []
for x in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])
rate = []
for student in students:
    rate.append (student[1])
second = sorted(list(set(rate)))[1]
seconds = []
for student in students:
    if student[1] == second:
        seconds.append(student[0])
print (*sorted(seconds), sep='\n')