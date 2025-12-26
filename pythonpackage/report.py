from student import getStudent
from attendence import attends
from marks import mark
from fees import getFee
from utils import percentage

class Report:

    def generate(self, sid):
        student = getStudent(sid)

        if student is None:
            print("Student not found")
            return
        
        marks_dict = mark(sid)
        total_marks = sum(marks_dict.values()) if marks_dict else 0
        percent = percentage(total_marks, 300) 

        print("\n========== STUDENT REPORT ==========")
        print("Student ID :", sid)
        print("Name       :", student["Name"])
        print("Course     :", student["Course"])
        print("Attendance :", attends(sid), "days")
        print("Marks      :", mark(sid))
        print("Fees Paid  :", getFee(sid))
        print("percentage :",percent,"%")
        print("===================================\n")

