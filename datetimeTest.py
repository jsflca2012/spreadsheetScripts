from datetime import datetime
import dateparser


date_string = "2019-03-21"
try:
    datetime.strptime(date_string, '%m/%d/%Y')
    print("sdf")
except ValueError:
    print("asd")
