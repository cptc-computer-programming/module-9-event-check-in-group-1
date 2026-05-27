"""Discounts and Fees.

This module is your team's workspace for discount and service-fee calculations.
"""

# Your job:
# Design two functions that produce the required shared outputs described in
# docs/DISCOUNTS_FEES.md.
#
# Before coding:
# 1. Read the business rules and target examples in your team brief.
# 2. Decide on one clear job for each of your two functions.
# 3. Write a data contract for each function.
# 4. Check your shared outputs with the teams that need them.
# 5. Get instructor approval for both contracts.
#
# Data contract template for Function 1:
# Function name: service_fee
# Purpose: To determine the total fees for the the reservation.
# Parameters: total_guests_in_reservation, is_online, subtotal
# Returns: returned_service_fee
# Possible return values: 0 (0$) or maybe 5 (5$)
# Assumptions:
# Example call:
# Example result:
# Who might use this function? The team for Final Check-In Decision
#


def service_fee(total_guests_in_reservation, is_online, subtotal):

    IS_ONLINE_FEE = 5

    service_fee_percent = 0
    returned_service_fee = 0

    if is_online:
       service_fee_percent = IS_ONLINE_FEE
       returned_service_fee = subtotal * service_fee_percent
    else:
        returned_service_fee = subtotal * service_fee_percent


    return(returned_service_fee)


# Data contract template for Function 2:
# Function name: discount_amount
# Purpose: To determine the total discounts for the reservation.
# Parameters: total_guests_in_reservation, is_online, subtotal
# Returns: discount_amount
# Possible return values: 0 (0$) or maybe -15 (-15$)
# Assumptions:
# Example call:
# Example result:
# Who might use this function? The team for Final Check-In Decision
#





# TODO: After approval, write your two function definitions under each funtion comment above here.
