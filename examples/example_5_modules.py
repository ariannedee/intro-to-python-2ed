import time  # Import a module

from datetime import datetime as dt
from random import randint, choice  # Import functions from a module

# RANDOM MODULE
print(randint(1, 100))
print(choice('ABCD'))


# TIME MODULE
start_time = time.time()  # Elapsed seconds since the Unix epoch
print(f"Seconds since Jan 1, 1970 UTC: {start_time}")

time.sleep(2)

end_time = time.time()
print(f"Elapsed time: {round(end_time - start_time, 2)}s")

as_gmt = time.gmtime(start_time)  # Convert Unix timestamp to a GMT (Greenwich Mean Time) data structure
print(f"Today is {as_gmt.tm_mday}/{as_gmt.tm_mon}/{as_gmt.tm_year}")

# DATETIME MODULE
a_date_time = dt.fromtimestamp(start_time)  # Convert timestamp to a datetime
print(a_date_time)

now = dt.now()  # Get the current datetime (without converting from epoch timestamp)

# Format a datetime for printing. See https://strftime.org/ for codes.
print(f"It is {now.strftime('%b %-d, %Y')} at {now.strftime('%-I:%M %p')}")
