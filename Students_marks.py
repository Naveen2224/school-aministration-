import csv
def write_into_csv(marks_list):
	with open('students_marks.csv','a',newline='')as csv_file:
		writer=csv.writer(csv_file)
		if csv_file.tell()==0:
			writer.writerow(["Name","Marks","Grade"])
		writer.writerow(marks_list)

if __name__=='__main__':
	condition=True
	student_num=1
	while(condition):
		students_marks=input('enter the student name and marks for student #{} in following format(name marks): '.format(student_num))
		students_marks_list=students_marks.split(' ')
		print("\nentered info is:\nname: {} \nmarks: {} \n".format(students_marks_list[0],students_marks_list[1]))
		check=input("Is entered marks of student is crct: ")
		if check=='yes':
			if int(students_marks_list[1])>90:
				students_marks_list.append('A+')
			elif int(students_marks_list[1])>80:
				students_marks_list.append('A')
			elif int(students_marks_list[1])>70:
				students_marks_list.append('B+')
			elif int(students_marks_list[1])>60:
				students_marks_list.append('B')
			elif int(students_marks_list[1])>50:
				students_marks_list.append('C')
			elif int(students_marks_list[1])>35:
				students_marks_list.append('D')
			elif int(students_marks_list[1])<=30:
				students_marks_list.append('fail')
			write_into_csv(students_marks_list)
			condition_check=input('enter(yes/no)if u wanted to enter other student marks: ')
			if condition_check=='yes':
				condition=True
				student_num+=1
			elif condition_check=='no':
				condition=False
		elif check=='no':
			print("\nplease enter the crct info:\n ")
print('\n')
f=open('students_marks.csv','r')
print(f.read())	






#output:
enter the student name and marks for student #1 in following format(name marks): Naveen 50

entered info is:
name: Naveen
marks: 50

Is entered marks of student is crct: yes
enter(yes/no)if u wanted to enter other student marks: yes
enter the student name and marks for student #2 in following format(name marks): Mani 85

entered info is:
name: Mani
marks: 85

Is entered marks of student is crct: yes
enter(yes/no)if u wanted to enter other student marks: yes
enter the student name and marks for student #3 in following format(name marks): sharath 95

entered info is:
name: sharath
marks: 95

Is entered marks of student is crct: yes
enter(yes/no)if u wanted to enter other student marks: no


Name,Marks,Grade
Naveen,50,D
Mani,85,A
sharath,95,A+



