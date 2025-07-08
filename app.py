from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Global variables to store students data and number of students
students_data = []
num_students = 0

# Route for Page 1 – Enter number of students
@app.route("/", methods=["GET", "POST"])
def page1():
    global num_students, students_data
    if request.method == "POST":
        num_students = int(request.form["num_students"])
        students_data = []  # reset data
        return redirect(url_for("page2"))
    return render_template("pagee.html")

# Route for Page 2 – Enter student details
@app.route("/enter-students", methods=["GET", "POST"])
def page2():
    global students_data, num_students
    if request.method == "POST":
        students_data = []  # reset before appending
        for i in range(num_students):
            student = {
                "ID": request.form[f"student_id_{i}"],
                "First Name": request.form[f"first_name_{i}"],
                "Last Name": request.form[f"last_name_{i}"],
                "Math": float(request.form[f"math_{i}"]),
                "English": float(request.form[f"english_{i}"]),
                "Science": float(request.form[f"science_{i}"]),
            }
            students_data.append(student)
        print("Students Data Collected:", students_data)  # debug print
        return redirect(url_for("page3"))
    return render_template("pagee2.html", num_students=num_students)

# Function to assign grade based on average
def assign_grade(avg):
    if avg >= 70:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

# Function to assign remark based on grade
def assign_remark(grade):
    remarks = {
        "A": "Excellent",
        "B": "Very Good",
        "C": "Good",
        "D": "Fair",
        "F": "Fail"
    }
    return remarks.get(grade, "")

# Route for Page 3 – Display student results
@app.route("/page3")
def page3():
    summary = []
    for record in students_data:
        total = record["Math"] + record["English"] + record["Science"]
        average = total / 3
        grade = assign_grade(average)
        remark = assign_remark(grade)

        student_record = {
            **record,
            "Total": total,
            "Average": round(average, 2),
            "Grade": grade,
            "Remark": remark
        }
        summary.append(student_record)

    # Rank students by average descending
    ranked = sorted(summary, key=lambda x: x["Average"], reverse=True)

    # Calculate class average
    class_avg = round(sum(s["Average"] for s in ranked) / len(ranked), 2) if ranked else 0

    return render_template("pagee3.html", students=ranked, class_avg=class_avg)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
