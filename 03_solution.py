score = int(input("Enter the student garde: "))

if score >=101:
    print("Please verify your grade again")
    exit()
    
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >= 50:
    grade = "E"
else :
    grade = "F"

print(grade)