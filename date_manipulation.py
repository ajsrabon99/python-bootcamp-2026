from datetime import datetime, timedelta

now = datetime.now()
print(now.strftime("%d/%m/%y %H:%M"))

day = datetime.strptime("2026/10/20", "%Y/%m/%d")
print((day + timedelta(days=31)).strftime("%Y-%m-%d"))