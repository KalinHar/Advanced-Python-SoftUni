def entry_list(n):
    lines = []
    for _ in range(n):
        lines.append(input())
    return lines


count = int(input())
students_grades = entry_list(count)

students ={}
for line in students_grades:
    name, grade = line.split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for st, grades in students.items():
    grades_str = " ".join(map(lambda gr: f"{gr:.2f}", grades))
    avg_gr = sum(grades) / len(grades)
    print(f'{st} -> {grades_str} (avg: {avg_gr:.2f})')
