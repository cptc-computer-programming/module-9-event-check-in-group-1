# Final Check-In Decision

## Your Assignment

Your team must create **two functions**:

- One function calculates and returns the numeric quoted final amount for the
  reservation.
- One function chooses and returns the final check-in status for event staff.

You decide the function names and the parameters needed for each function.

## Required Shared Outputs

- A numeric quoted final amount for the reservation.
- A status code that tells staff the next action for check-in.

## Available Inputs

Other teams will produce a reservation subtotal, a discount, a service fee, a
boolean check-in permission decision, and a wait-time estimate.

## Business Rules

- Quoted final amount is subtotal minus discount plus service fee.
- Never return a negative quoted amount; return `0` if the calculation is
  below `0`.
- Calculate the quoted amount regardless of capacity. If the reservation
  cannot check in, staff should follow the denied status instead of collecting
  payment.
- If check-in permission is `False`, the status is `DENIED_CAPACITY`.
- Otherwise, if payment is due and wait time is more than 15 minutes, the
  status is `PAY_AND_WAIT`.
- Otherwise, if payment is due, the status is `PAYMENT_REQUIRED`.
- Otherwise, if wait time is more than 15 minutes, the status is `LONG_WAIT`.
- Otherwise, the status is `READY`.

## Who Uses Your Outputs?

`app.py` will display the quoted final amount and final check-in status for
event staff.

## Examples To Discuss

```text
Subtotal 100.00, discount 10.00, fee 5.00 -> 95.00 quoted amount
Subtotal 50.00, discount 60.00, fee 0.00 -> 0.00 quoted amount
No check-in permission, quoted amount 95.00, wait 8 -> DENIED_CAPACITY
Check-in permission, quoted amount 95.00, wait 20 -> PAY_AND_WAIT
Check-in permission, quoted amount 95.00, wait 8 -> PAYMENT_REQUIRED
Check-in permission, quoted amount 0.00, wait 20 -> LONG_WAIT
Check-in permission, quoted amount 0.00, wait 8 -> READY
```

## Create Two Data Contracts

You must create **two data contracts** before writing function code. Decide
your function names, parameters, and return values, post the contracts for the
class, and get approval before coding.

```text
Function name:
Purpose:
Parameters:
Returns:
Possible return values:
Assumptions:
Example call:
Example result:
Who might use this function?
```
