# Predefined subjects
subjects = ["Math", "English", "Science", "History", "Geography"]

# Empty dictionary to store all results
results = {}

# Ask how many students to enter
num_students = int(input("How many students do you want to enter? "))
while num_students <= 0:
    print("Please enter a valid number of students (greater than 0).")
    num_students = int(input("How many students do you want to enter? "))

# Collect input for each student
for _ in range(num_students):
    name = input("\nEnter student name: ").strip().title()
    scores = {}
    
    for subject in subjects:
        while True:
            try:
                score = float(input(f"Enter score for {subject}: "))
                if 0 <= score <= 100:
                    scores[subject] = score
                    break
                else:
                    print("Please enter a score between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    results[name] = scores

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

# Function to calculate total, average, grade, and remark
def calculate_results(data):
    summary = []
    for student, subjects in data.items():
        total = sum(subjects.values())
        average = total / len(subjects)
        grade = assign_grade(average)
        remark = assign_remark(grade)
        student_record = {
            "Student": student,
            "Total": total,
            "Average": round(average, 2),
            "Grade": grade,
            "Remark": remark,
            **subjects
        }
        summary.append(student_record)
    return summary

# Function to display result with rank
def display_results(summary):
    # Sort by average descending
    ranked = sorted(summary, key=lambda x: x["Average"], reverse=True)

    header = f"{'Rank':<5}{'Student':<10}" + "".join([f"{sub:<10}" for sub in subjects]) + f"{'Total':<10}{'Average':<10}{'Grade':<8}{'Remark'}"
    print("\n" + header)
    print("-" * len(header))

    for i, record in enumerate(ranked, start=1):
        row = f"{i:<5}{record['Student']:<10}" + "".join([f"{record[sub]:<10}" for sub in subjects]) + f"{record['Total']:<10}{record['Average']:<10}{record['Grade']:<8}{record['Remark']}"
        print(row)

# Main logic
summary = calculate_results(results)
display_results(summary)
