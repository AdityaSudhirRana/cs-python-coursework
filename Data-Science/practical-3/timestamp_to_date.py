from datetime import datetime

timestamp = 1824642487

print("S105 Aditya Rana")

date = datetime.fromtimestamp(timestamp)

print(date.strftime("%Y-%m-%d %H:%M:%S"))
