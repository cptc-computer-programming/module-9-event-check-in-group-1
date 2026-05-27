"""Capacity Management.

This module is your team's workspace for occupancy and admission decisions.
"""

# Your job:
# Design two functions that produce the required shared outputs described in
# docs/CAPACITY_MANAGEMENT.md.
#
# Before coding:
# 1. Read the business rules and target examples in your team brief.
# 2. Decide on one clear job for each of your two functions.
# 3. Write a data contract for each function.
# 4. Check your shared outputs with the teams that need them.
# 5. Get instructor approval for both contracts.
#
# Data contract template for Function 1:
# Function name: current_capacity
# Purpose: Numeric percentage of event capacity
# Parameters: number_ahead_in_queue, event_capacity
# Returns: float
# Possible return values: 0.0f-100.0f
# Assumptions:
# Example call: current_capacity(13, 20)
# Example result: 65.0
# Who might use this function?
# This could be used in either the checkin_decision module or the wait_time module, 
# as well as just generally informing customers
# 
# Data contract template for Function 2:
# Function name: within_capacity
# Purpose: Decide whether a full reservation can check in
# Parameters: total_guests_in_reservation, number_ahead_in_queue, event_capacity
# Returns: bool
# Possible return values: True, False
# Assumptions:
# Example call: 
# Example result: 
# Who might use this function?
# The function can be used for the checkin_decision module
# TODO: After approval, write your two function definitions below.

# Proposals
# change number_ahead_in_queue -> guests_checked_in

# Numeric percentage of event capacity
def current_capacity(number_ahead_in_queue, event_capacity):
    if event_capacity <= 0:
        return 0
    return number_ahead_in_queue / event_capacity * 100


# Decide whether a full reservation can check in
def within_capacity(total_guests_in_reservation, number_ahead_in_queue, event_capacity):
    if event_capacity <= 0:
        return False
    return total_guests_in_reservation + number_ahead_in_queue <= event_capacity


# Testing
print(f"current_capacity(13, 20): {current_capacity(13, 20)}")
print(f"current_capacity(20, 20): {current_capacity(20, 20)}")

print(f"within_capacity(3, 13, 20): {within_capacity(3, 13, 20)}")
print(f"within_capacity(8, 13, 20): {within_capacity(8, 13, 20)}")
