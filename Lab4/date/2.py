from datetime import datetime, timedelta 

x = datetime.now() # today

y = x - timedelta(days=1) #yesterday

z = y = x + timedelta(days=1) #tomorrow