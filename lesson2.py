input = input()

if input.isdigit():
    seconds = int(input)
    print("seconds:" + str(seconds))
    minutes = seconds / 60
    print("minutes: " + str(minutes))
    hour = minutes / 60
    print("hour: " + str(hour))
else:
    print(input + " не число")
