import datetime

current_date = datetime.datetime.today().date()
current_time = datetime.datetime.today().time()
current_today = datetime.datetime.today()
print(current_date)
print(current_time)
print(current_today)

# Formatting Datetime Objects:format datetime objects into strings using strftime().
# Format the current datetime as a string
formatedTime = current_today.strftime("%Y-%m-%d-%H-%M-%S-%f")
print(formatedTime)

# Parsing Strings to Datetime Objects: convert strings to datetime objects using strptime()
parsed_datetime = datetime.datetime.strptime("2023-12-25 08:30:00", "%Y-%m-%d %H:%M:%S")
print("Parsed Datetime", parsed_datetime)
