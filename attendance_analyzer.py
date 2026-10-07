total_days = int(input("Enter total working days: "))
present_days = int(input("Enter present days: "))

absent_days = total_days - present_days
attendance_percentage = (present_days / total_days) * 100

print("present_days:", present_days)
print("absent_days:", absent_days)
print("attendance_percentage:", attendance_percentage)

if attendance_percentage >= 15:
    print("Employee is eligible for bonus.")
else:
    print("Employee is not eligible for bonus.")