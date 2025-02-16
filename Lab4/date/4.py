from datetime import datetime

x = input()

y = input()

date1 = datetime.strptime(x , "%Y-%m-%d %H:%M:%S" )

date2 = datetime.strptime(y , "%Y-%m-%d %H:%M:%S" )

difference = abs(date2 - date1)

print(difference.total_seconds())
