"""Assignment 1 - MCS253
Creating Python Objects ~ Lists, Tuples, Dictionaries"""

#Due Date - Submit no later than 4:10 pm on Thursday (3rd April 2025)

#Please type in your name in the next line by way of commenting

#Name: Jonah ALBERT


#----------------------------------------------------------------

#Quesiton 1

"""Create a python object to store all the courses you are taking this semester.
You may be required to change a course next week."""

courses_this_semester = ["MA 241","MA 211","MA 221","MCS 253","MCS 251"]

#Question 2

"""Store all MCS 253 students ID in a python object. These IDs will be
used for 4 years thus do not change IDs."""

mcs_253_student_ids = ("202412245","202412236","202412232","202412253","2023314233","2023314260")

#Question 3
"""Since students IDs are a unique identifying number for each student, 

use it as a reference to point to students records. The students records
should consist of full names, gender, DOB,Province of origin & email addresses."""

student_records = {202412245:{'Name':'Margreth KURI','Gender':'Female','DOB':'18-12-1998','Province':'Jiwaka','Email':'kurimargreth@gmail.com'},202412236:
                  {'Name':'Natasha RICKY','Gender':'Female','DOB':'05-07-1998','Province':'Eastern Highlands','Email':'natashajricky@gmail.com'},202412232:
                  {'Name':'Dahan TIMINAI','Gender':'Male','DOB':'11-11-2001','Province':'Western','Email':'timinaidahan@gmail.com'},202412253:
                  {'Name':'Junior ROBERT','Gender':'Male','DOB':'12-10-2000','Province':'Jiwaka','Email':'juniorwalrob127@gmail.com'},2023314233:
                  {'Name':'Rophie NOMORU','Gender':'Male','DOB':'19-10-2002','Province':'Morobe','Email':'rophiejosephnomoru191002@gmail.com'},2023314260:
                  {'Name':'Jonah ALBERT','Gender':'Male','DOB':'09-05-2004','Province':'Central','Email':'albertjonah84@gmail.com'}}


#Question 4
"""Using indexing, print out your favorite course for the sem (refer to Q1)"""

print(courses_this_semester[3])

#Question 5
"""Print out only your student ID from Q2"""

print(mcs_253_student_ids[5])

#Question 6
"""Print out all students records (exclude the IDs)"""

for record in student_records.values():
 print(record)

#Question 7
"""Print out only your student record"""

print(student_records[2023314260])


#Question 8
"""Update the student ID in Q2.
What is the error here?
WHy do you think this happened"""

mcs_253_student_ids[0,1,2,3,4,5] = ("2000","2001","2002","2003","2004","2004")
print(mcs_253_student_ids[0,1,2,3,4,5])

"""There is a TYPE ERROR because TUPLES are immutable,which means their contents cannot be changed once defined."""

#Question 9
"""Print out the data types for all the objects you have created so far"""

print(type(courses_this_semester))
print(type(mcs_253_student_ids))
print(type(student_records))


#------end of Assignment
#UPLOAD your completed A1 to your GitHub account. Only share the link with me. 