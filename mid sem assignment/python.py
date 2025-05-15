def collect_data():
    # Predefined data for non-interactive environments
    num_students = 3
    num_subjects = 4
    subjects = ['Math', 'English', 'Science', 'Arts']

    student_inputs = [
        {'name': 'Ali', 'scores': [80, 70, 65, 34]},
        {'name': 'Zara', 'scores': [60, 55, 75, 92]},
        {'name': 'John', 'scores': [90, 85, 88, 93]}
    ]

    return student_inputs, subjects

def calculate_average(scores):
    return sum(scores) / len(scores)

def assign_grade(avg):
    if avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 50:
        return 'D'
    else:
        return 'F'

def generate_remark(grade):
    remarks = {
        'A': "Excellent",
        'B': "Very Good",
        'C': "Good",
        'D': "Fair – Needs Improvement",
        'F': "Poor – Work Harder"
    }
    return remarks.get(grade, "No Remark")

def summarize_students(data):
    print("\n--- Student Summaries ---")
    for student in data:
        avg = calculate_average(student['scores'])
        grade = assign_grade(avg)
        remark = generate_remark(grade)
        print(f"Hi {student['name']}, you scored an average of {avg:.2f}, your grade is {grade}, {remark}.")

def class_statistics(data):
    print("\n--- Class Summary ---")
    averages = [calculate_average(s['scores']) for s in data]
    class_avg = sum(averages) / len(averages)
    top_student = max(data, key=lambda s: calculate_average(s['scores']))
    grade_dist = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

    for avg in averages:
        grade = assign_grade(avg)
        grade_dist[grade] += 1

    print(f"Class Average: {class_avg:.2f}")
    print(f"Top Student: {top_student['name']} ({calculate_average(top_student['scores']):.2f})")
    print("Grade Distribution:", ", ".join([f"{g}-{n}" for g, n in grade_dist.items()]))

# Main Execution
students_data, subjects_list = collect_data()
summarize_students(students_data)
class_statistics(students_data)
