Scores = [75, 70, 95, 60, 45, 22]

highest = max(Scores)
lowest = min(Scores)

for score in Scores:
    if score >= 90:
        print("Excellent")
    elif score >= 75:
        print("Good")
    elif score >= 60:
        print("Average")
    else:
        print("Poor")

print("Highest Score:", highest)
print("Lowest Score:", lowest)