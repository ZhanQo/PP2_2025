from datetime import datetime, timedelta

x = datetime.now()
y = x - timedelta(days=5)
print(y.strftime('%Y-%m-%d'))
print(x.strftime('%Y-%m-%d'))
