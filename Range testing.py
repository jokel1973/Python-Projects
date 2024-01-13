






from datetime import datetime, timedelta
import pytz  # You may need to install the 'pytz' library if not already installed

# Define time zones for each branch
portland_tz = pytz.timezone('America/Los_Angeles')  # Portland is in the Pacific Time Zone
nyc_tz = pytz.timezone('America/New_York')  # NYC is in the Eastern Time Zone
london_tz = pytz.timezone('Europe/London')  # London is in the Greenwich Mean Time (GMT) Zone

# Get the current time for each branch
current_time_portland = datetime.now(portland_tz)
current_time_nyc = datetime.now(nyc_tz)
current_time_london = datetime.now(london_tz)

# Define opening and closing hours for each branch
opening_hour = 9
closing_hour = 17

# Check if each branch is open or closed
def is_branch_open(current_time, opening_hour, closing_hour):
    return opening_hour <= current_time.hour < closing_hour

# Determine the status of each branch
status_portland = "Open" if is_branch_open(current_time_portland, opening_hour, closing_hour) else "Closed"
status_nyc = "Open" if is_branch_open(current_time_nyc, opening_hour, closing_hour) else "Closed"
status_london = "Open" if is_branch_open(current_time_london, opening_hour, closing_hour) else "Closed"

# Print out the results
print(f"Portland HQ is {status_portland}")
print(f"NYC branch is {status_nyc}")
print(f"London branch is {status_london}")

