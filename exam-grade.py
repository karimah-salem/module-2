while True:
    mark = int(input("Enter exam mark: "))
    if 1 <= mark <= 100:
        break
    else:
        print("Invalid number. Mark must be between 1 and 100.")


if mark < 50:
    print("fail")

elif 50 <= mark <= 60:
    print("pass")

elif 61 <= mark <= 70:
    print("merit")

elif 71 <= mark <= 100:
    print("distinction")

