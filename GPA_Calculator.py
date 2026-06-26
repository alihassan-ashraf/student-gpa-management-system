import streamlit as st

class GPACalculator:

    def find_grade(self, marks):
        if marks >= 95:
            return "A+"
        elif marks >= 85:
            return "A"
        elif marks >= 80:
            return "B+"
        elif marks >= 70:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 50:
            return "D"
        else:
            return "F"

    def find_grade_point(self, marks):
        grade_points = {
            100: 4.0, 99: 4.0, 98: 4.0, 97: 4.0, 96: 4.0, 95: 4.0,
            94: 4.0, 93: 4.0, 92: 4.0, 91: 4.0, 90: 4.0,
            89: 4.0, 88: 4.0, 87: 4.0, 86: 4.0, 85: 4.0,
            84: 3.9, 83: 3.9, 82: 3.8, 81: 3.7, 80: 3.7,
            79: 3.6, 78: 3.5, 77: 3.5, 76: 3.4, 75: 3.3,
            74: 3.3, 73: 3.2, 72: 3.1, 71: 3.1, 70: 3.0,
            69: 2.9, 68: 2.8, 67: 2.7, 66: 2.6, 65: 2.5,
            64: 2.4, 63: 2.3, 62: 2.2, 61: 2.1, 60: 2.0,
            59: 1.9, 58: 1.8, 57: 1.7, 56: 1.6, 55: 1.5,
            54: 1.4, 53: 1.3, 52: 1.2, 51: 1.1, 50: 1.0
        }

        return grade_points.get(round(marks), 0.0)

    def find_remarks(self, marks):
        if marks >= 95:
            return "Excellent"
        elif marks >= 85:
            return "Very Good"
        elif marks >= 70:
            return "Good"
        elif marks >= 60:
            return "Satisfactory"
        elif marks >= 50:
            return "Poor"
        else:
            return "Fail"

    def calculate_gpa(self, courses):
        total_quality_points = 0
        total_credit_hours = 0

        for course in courses:
            total_quality_points += course["quality_point"]
            total_credit_hours += course["credit_hours"]

        if total_credit_hours == 0:
            return 0

        return total_quality_points / total_credit_hours


calculator = GPACalculator()

st.set_page_config(page_title="University GPA Calculator", page_icon="🎓")

st.title("🎓 University GPA Calculator")
st.write("Calculate your semester GPA based on marks and credit hours.")

student_name = st.text_input("Student Name")
roll_number = st.text_input("Roll Number")
semester = st.text_input("Semester")

total_courses = st.number_input(
    "Enter total number of courses",
    min_value=1,
    max_value=15,
    value=5
)

courses = []

st.subheader("Course Details")

for i in range(total_courses):
    st.write(f"### Course {i + 1}")

    course_name = st.text_input(f"Course Name {i + 1}", key=f"name_{i}")
    credit_hours = st.number_input(
        f"Credit Hours {i + 1}",
        min_value=1,
        max_value=6,
        value=3,
        key=f"credit_{i}"
    )
    marks = st.number_input(
        f"Marks Obtained {i + 1}",
        min_value=0,
        max_value=100,
        value=80,
        key=f"marks_{i}"
    )

    grade = calculator.find_grade(marks)
    grade_point = calculator.find_grade_point(marks)
    remarks = calculator.find_remarks(marks)
    quality_point = credit_hours * grade_point

    courses.append({
        "course_name": course_name,
        "credit_hours": credit_hours,
        "marks": marks,
        "grade": grade,
        "grade_point": grade_point,
        "quality_point": quality_point,
        "remarks": remarks
    })

if st.button("Calculate GPA"):
    gpa = calculator.calculate_gpa(courses)

    st.success(f"Your Semester GPA is: {gpa:.2f}")

    st.subheader("Result Card")

    st.write("**Student Name:**", student_name)
    st.write("**Roll Number:**", roll_number)
    st.write("**Semester:**", semester)

    st.table(courses)
