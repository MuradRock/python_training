from datetime import datetime, timedelta

original_date = datetime(2020, 3, 22, 10, 0, 0)
new_date = original_date + timedelta(weeks=1, hours=12)

print("Original datetime:", original_date)
print("New datetime:", new_date)


#today, yersterday, tomorrow
from datetime import datetime, timedelta

today = datetime.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.date())
print("Today:", today.date())
print("Tomorrow:", tomorrow.date())

##cwd
import os

# Current working directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# Create folder
os.mkdir("test")
print("Folder 'test' created.")

# List all files/folders
print("Directory Contents:", os.listdir(cwd))

# Remove folder
os.rmdir("test")
print("Folder 'test' removed.")

##rename file
import os

os.rename("output.txt", "new_name.txt")
print("File renamed successfully!")


##size of file
import os

size = os.path.getsize("sample.txt")
print("File size (bytes):", size)

## convert string to datetime
from datetime import datetime

dt = datetime.strptime("Feb 25 2020 4:20PM", "%b %d %Y %I:%M%p")
print(dt)

##subtract days from date

from datetime import datetime, timedelta

date_val = datetime(2025, 2, 25)
new_date = date_val - timedelta(days=7)

print("New date:", new_date.date())

##format datetime
from datetime import datetime

d = datetime(2020, 2, 25)
formatted = d.strftime("%A %d %B %Y")
print(formatted)







