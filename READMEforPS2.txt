##Files for PS2 in this Repo: Reset.py, Function.py, Arol.py, READMEforPS2.txt
##In the very beginning, run the Reset.py file to set the sample data and create the data files
##To run code, tun Arol.py
##To check the sample usernames, check the Student.txt and Admin.txt file
##Default password of every account in sample data is "abc"
##Sample Data contains: Course Already Set, some admin accounts, some student accounts and grades of some students entered.
##To exit code anytime, type "exit" in any of the input
##Run the Reset.py file to remove or add the sample data, or to only remove the course set status and students grades 
>Files: Arol.py, Function.py, Reset.py, Student.txt, Admin.txt, Course.txt, Grades.bin
>The main menu shows options to login as well as to create new user
>New user options enables to create new admin or new student and provides them a new username
>After the student login, they can access their grade sheet (if grades of that student entered)
>After the admin login, 
--they can set the course(if not set, only once)
--they can manage the grades of students (Enter grades or modify already entered grades
--they can view grade sheet of students
>Arol.py: It contains the main runnable block of code
>Function.py: It contains all the functions defined
>Reset.py: As mentioned above, it can be used to remove or add the sample data, or to only remove the course set status and students grades.
           It must also be used in the very beginning to initialize the data
>Student.txt, Admin.txt: It contains the Name, Username, Password of the user in the format of "<Name>$<Username>$<Password>" respectively for
                         for the students and admins respectively (in each line)
>Course.txt: The first line contains "Y" if the courses for the semester is set, else "N"
             The following lines contain "Y" if that course is selected, else "N", followed by the name and code of that course (in each line)
>Grades.bin: It contains the student grades in the form of [Name, Branch, Roll, Dictionary of Coursename:Grades pairs]
             The dictionary is empty if the grades of that student is not entered
>To change password, edit the password or the required user in the required file (Student.txt,Admin.txt) manually
>To add or remove a course manually enter/remove the course name in the Course.txt file

