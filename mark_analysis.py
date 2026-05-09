import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Student Marks Analysis System")

# Lists to store data
student_names = []
genders = []
marks_list = []

# Input for 3 students
for i in range(3):

    st.header(f"Student {i+1}")

    name = st.text_input(f"Enter Student Name {i+1}")

    gender = st.radio(
        f"Select Gender {i+1}",
        ("Male", "Female"),
        key=i
    )

    marks = st.number_input(
        f"Enter Marks {i+1}",
        min_value=0,
        max_value=100,
        step=1,
        key=str(i)
    )

    submit = st.button(f"Submit Student {i+1}")

    if submit:

        try:

            # Exception handling
            if name == "":
                raise ValueError("Student name cannot be empty!")

            student_names.append(name)
            genders.append(gender)
            marks_list.append(marks)

            st.success("Student data added successfully!")

        except ValueError as e:
            st.error(e)


# Process when 3 students entered
if len(marks_list) == 3:

    # NumPy Array
    marks_array = np.array(marks_list)

    # Analysis
    mean_marks = np.mean(marks_array)
    max_marks = np.max(marks_array)

    st.subheader("Marks Analysis")
    st.write("Mean Marks :", round(mean_marks, 2))
    st.write("Maximum Marks :", max_marks)

    # Result classification
    results = []

    for mark in marks_list:

        if mark >= 50:
            results.append("Pass")
        else:
            results.append("Fail")

    # Pandas DataFrame
    data = {
        "Student Name": student_names,
        "Gender": genders,
        "Marks": marks_list,
        "Result": results
    }

    df = pd.DataFrame(data)

    # Sorting ascending order
    df = df.sort_values(by="Marks")

    st.subheader("Student Records")
    st.dataframe(df)

    # Graph
    st.subheader("Marks Graph")

    fig, ax = plt.subplots()

    ax.bar(student_names, marks_list)

    ax.set_xlabel("Student Name")
    ax.set_ylabel("Marks")
    ax.set_title("Student Marks")

    st.pyplot(fig)
