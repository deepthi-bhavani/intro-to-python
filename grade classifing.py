grade = float(input("Enter grade /100: "))

if not 0 <= grade <= 100:
    print("Invalid grade")
elif grade >= 80:
    print("Very good")
elif grade >= 60:
    print("Good")
elif grade >= 40:
    print("Fairly good")
elif grade >= 20:
    print("Pass")
else:
    print("Fail")