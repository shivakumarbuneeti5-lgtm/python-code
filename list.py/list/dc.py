students=["shiva","harish","vamshi"]
marks=["90,58,79"]
marks_dict= {student:mark for student, mark in zip(students,marks)if marks > 90 } 
print(marks_dict) 
marks_dict= {student:mark for student, mark in zip(students,marks) if marks < 90 }
print(marks_dict) 