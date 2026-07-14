from datetime import datetime


print("S105 Aditya Rana")

date1 = datetime.strptime("2026-06-22","%Y-%m-%d")

date2 = datetime.strptime("2027-01-22","%Y-%m-%d")

if date1 < date2:
    print("2026-06-22 is earlier than 2027-01-22")
elif date1 > date2:
    print("2026-06-22 is later than 2027-01-22")
else:
    print("Both dates are same")
