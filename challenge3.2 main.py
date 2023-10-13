'''
Implement a function called sort_student that takes a list of student objects as input and sort the
list based on their CGPA(cumulative Grade point average)in descending order.Each student object 
has the following attribute:name(string),roll_number(string),and cgpa(float).Test the function 
with different input lists of students.
'''

class student:

  def_init_(self, name, roll_number,cgpa):
  self. name=name 
self. roll_number=roll_number
self. cgpa=cgpa


def sort_students(student_list):
  sor the list of students in descending order of CPGA 
sorted_student=sorted(student_list:
                     key=lambda student:student cpga
                     reverse=true)
#syntax lambda arg:exp 
return sorted_student


#Example Usage:
students =[
  student("Hari","A123",7.8),
  students("Srikanth","A124",8.9),
  students("Sawmya","A125",9.1),
  students("Mahidhar","A126",9.9),
]

sorted_students=sort_students(students) 

    #print the sorted list of students 
for students in sorted_student:
  print("Name:{},RollNumber:{},CGPA:{}",format(student.name,
                                              student. roll_number,
                                              student.cgpa)) 
