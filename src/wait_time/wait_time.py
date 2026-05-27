"""Wait Time Estimator.

This module is your team's workspace for wait-time and check-in lane decisions.
"""

# Your job:
# Design two functions that produce the required shared outputs described in
# docs/WAIT_TIME.md.
#
# Before coding:
# 1. Read the business rules and target examples in your team brief.
# 2. Decide on one clear job for each of your two functions.
# 3. Write a data contract for each function.
# 4. Check your shared outputs with the teams that need them.
# 5. Get instructor approval for both contracts.
#
# Data contract template for Function 1:
# Function name: calculate_estimated_wait_time
# Purpose: Calculate the wait time in whole minutes
# Parameters: people_ahead_in_line
# Returns: estimated_wait_time_in_minutes
# Possible return values: 10 people = 8 minutes 
# Assumptions:
# Example call:
# Example result:
# Who might use this function?
#
# Data contract template for Function 2:
# Function name: determine_check_in_lane
# Purpose: Get the check in lane the reservation should use
# Parameters: priority_status, line_limit (20)
# Returns: check_in_lane
# Possible return values: Priority Lane, Standard Lane
# Assumptions:
# Example call:
# Example result:
# Who might use this function?
#
# TODO: After approval, write your two function definitions below.

estimated_seconds_per_person = 45

line_limit = 20

def calculate_estimated_wait_time(people_ahead_in_line):
    total_seconds = people_ahead_in_line * estimated_seconds_per_person
    minutes = total_seconds // 60
    remainder = total_seconds % 60

    if remainder > 0:
        minutes += 1

    return minutes

def determine_check_in_lane(priority_status, people_ahead_in_line):
    if priority_status or people_ahead_in_line > line_limit:
        return "Priority Lane"
    else:
        return "Standard Lane"
