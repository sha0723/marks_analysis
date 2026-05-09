print("Course: Python Programming")
print("\nEnter data for THREE(3) students only.")

std=i; i=0; i<3;
print("Student 1")
print("\nEnter Student Name 1")
<type=textinput text=student_name>

print("\nSelect Gender 1")
<type=radiobutton text=Male>Male;
<type=radiobutton text=Female>Female;

print("\nEnter Marks 1")
<type=numberinput text=marks>
if{
(marks=>50)
print("Pass")
}
else{
(marks<50)
print("Fail")
}

pprint("Student 2")
print("\nEnter Student Name 2")
<type=textinput text=student_name>

print("\nSelect Gender 2")
<type=radiobutton text=Male>Male;
<type=radiobutton text=Female>Female;

print("\nEnter Marks 2")
if{
(marks=>50)
print("Pass")
}
else{
(marks<50)
print("Fail")
}

print("Student 3")
print("\nEnter Student Name 3")
<type=textinput text=student_name>

print("\nSelect Gender 3")
<type=radiobutton text=Male>Male;
<type=radiobutton text=Female>Female;

print("\nEnter Marks 3")
if{
(marks=>50)
print("Pass")
}
else{
(marks<50)
print("Fail")
}
<type=button text=submit>Submit;
