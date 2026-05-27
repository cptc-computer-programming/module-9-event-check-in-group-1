"""Final Check-In Decision.

This module is your team's workspace for quoted-amount and status-code decisions.
"""

# Your job:
# Design two functions that produce the required shared outputs described in
# docs/CHECKIN_DECISION.md.
#
# Before coding:
# 1. Read the business rules and target examples in your team brief.
# 2. Decide on one clear job for each of your two functions.
# 3. Write a data contract for each function.
# 4. Check your shared outputs with the teams that need them.
# 5. Get instructor approval for both contracts.
#
# Data contract template for Function 1:
# Function name: calculate_final_amount
# Purpose: check the total amount to be paid
# Parameters: subtotal , service fee , discount 
# Returns: final_amount
# Possible return values: subtotal - (discount_amount + service_fee)
# Assumptions:
# Example call:
# Example result:
# Who might use this function? staff
#
# Data contract template for Function 2:
# Function name: determine_permission_status
# Purpose: determine if the user can check in
# Parameters: denied_capacity, ready, long_wait
# Returns: final_status
# Possible return values: checking_permission, ready, long_wait
# Assumptions:
# Example call:
# Example result:
# Who might use this function? customer 
#
# TODO: After approval, write your two function definitions below.



def calculate_total_amount(subtotal, discount , service_fee):
    """This returns the final amount after subtacting the service fee and the discount"""
    final_amount = subtotal - discount + service_fee
    return final_amount


def determine_permission_status(check_in_permitted, wait_time):
    """This determines the final status of if the customer can check in"""
    if not check_in_permitted:
        return("DENIED_CAPACITY")
    
    short_wait = 15

    if wait_time > short_wait:
        return("LONG_WAIT")
    else:
        return("READY")





