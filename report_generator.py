import csv

students = []

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) == 3:
            name = row[1]
            marks = int(row[2])
            students.append((name, marks))

marks = [m[1] for m in students]

def grade(m):
    if m >= 90: return "A"
    elif m >= 75: return "B"
    elif m >= 60: return "C"
    else: return "D"

topper = max(students, key=lambda x: x[1])
passed = len([m for m in marks if m >= 40])
failed = len(marks) - passed
avg = sum(marks) / len(marks)

if avg >= 75:
    performance = "Excellent"
elif avg >= 60:
    performance = "Good"
else:
    performance = "Needs Improvement"

print("\n--- Student Report ---")
print("Total Students:", len(students))
print("Average Marks:", avg)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print(f"Topper: {topper[0]} ({topper[1]})")
print("Passed:", passed)
print("Failed:", failed)
print("Class Performance:", performance)

# Export report
with open("final_report.txt", "w") as f:
    f.write("Student Report Summary\n")
    f.write(f"Total Students: {len(students)}\n")
    f.write(f"Average Marks: {avg}\n")
    f.write(f"Topper: {topper[0]} ({topper[1]})\n")
    f.write(f"Passed: {passed}, Failed: {failed}\n")
    f.write(f"Class Performance: {performance}\n")
