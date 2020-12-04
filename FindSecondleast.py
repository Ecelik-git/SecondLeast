'''dictionary sorting
codingwithec'''
student_count= int(input("How many students do you need to enter? "))
grade_list={}
for i in range(0, student_count):
    name=input("Please enter student name: ")
    grade=float(input("Please enter student grade: "))
    grade_list[name]=grade
sorted_grades =sorted(grade_list, value=grade_list.get, reverse=True)
print(sorted_grades)
print(grade_list)#printing dictionary
print(sorted_grades[-2])#printing the last second element
