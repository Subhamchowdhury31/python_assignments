from student import getStudent
from attendence import attends
from marks import mark
from fees import getFee

class Report:

    def generate(self, sid):
        student = getStudent(sid)

        if student is None:
            print("Student not found")
            return

        print("\n========== STUDENT REPORT ==========")
        print("Student ID :", sid)
        print("Name       :", student["Name"])
        print("Course     :", student["Course"])
        print("Attendance :", attends(sid), "days")
        print("Marks      :", mark(sid))
        print("Fees Paid  :", getFee(sid))
        print("===================================\n")

