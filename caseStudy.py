def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"


def getStudent():
    student = {}
    print("you have to enter 5 students name")
    for i in range(5):
        name = input(f'enter the {i+1} name: ')
        marks = []
        for j in range(3):
            mark = int(input(f'enter the {j+1} marks: '))
            marks.append(mark)
        average = sum(marks) / 3
        grade = get_grade(average)
        student[name] = {
            "average": average,
            "grade": grade
        }
    return student


studentData = getStudent()

for name in studentData:
    print("name", name, "average is", studentData[name]["average"], "grade", studentData[name]["grade"])
