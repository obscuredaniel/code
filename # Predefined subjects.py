# Predefined subjects
subjects = ["Math", "English", "Science"]

# Dictionary to store student data using ID as key
results = {}

# Ask how many students to enter
num_students = int(input("How many students do you want to enter? "))

# Collect input for each student
for _ in range(num_students):
    while True:
        student_id = input("\nEnter unique Student ID (e.g., 202501): ").strip()
        if student_id in results:
            print("This ID already exists. Please enter a unique ID.")
        else:
            break

    name = input("Enter student name: ").strip().title()
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

    results[student_id] = {"Name": name, **scores}

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

# Function to calculate total, average, grade, remark
def calculate_results(data):
    summary = []
    for student_id, record in data.items():
        subject_scores = {sub: record[sub] for sub in subjects}
        total = sum(subject_scores.values())
        average = total / len(subjects)
        grade = assign_grade(average)
        remark = assign_remark(grade)

        student_record = {
            "ID": student_id,
            "Name": record["Name"],
            **subject_scores,
            "Total": total,
            "Average": round(average, 2),
            "Grade": grade,
            "Remark": remark
        }
        summary.append(student_record)
    return summary

# Function to display the ranked result table
def display_results(summary):
    ranked = sorted(summary, key=lambda x: x["Average"], reverse=True)

    header = f"{'Rank':<7}{'ID':<12}{'Name':<15}" + "".join([f"{sub:<10}" for sub in subjects]) + f"{'Total':<10}{'Average':<10}{'Grade':<8}{'Remark'}"
    print("\n" + header)
    print("-" * len(header))

    for i, record in enumerate(ranked, start=1):
        row = f"{i:<7}{record['ID']:<12}{record['Name']:<15}" + "".join([f"{record[sub]:<10}" for sub in subjects]) + f"{record['Total']:<10}{record['Average']:<10}{record['Grade']:<8}{record['Remark']}"
        print(row)

# Run the logic
summary = calculate_results(results)
display_results(summary)
