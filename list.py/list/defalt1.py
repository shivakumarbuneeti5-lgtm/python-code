def dispstudent(stno,stname,stmarks,course="PYTHON",dept="ECE"):
    print("{}\t{}\t{}\t{}\t{}".format(stno,stname,stmarks,course,dept))
# Main Program
print("-"*60)
print("student information:")
print("-"*60)
print("stno\tname\tmarks\tcourse\tdepartment")
print("-"*60) 
dispstudent(10,"shiva",39.39) 
dispstudent(20,"gopi",23.45)
dispstudent(30,"hari",49.40)
dispstudent(40,"rohit",30.39,"java")
dispstudent(50,"deva",93.49,"PYTHON","ECE")
dispstudent(60,"varun",87.90,"PYTHON","ECE")