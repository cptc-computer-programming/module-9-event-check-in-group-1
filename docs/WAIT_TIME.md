# Wait Time Estimator

## Your Assignment

Your team must create **two functions**:

- One function calculates and returns the estimated wait time in whole
  minutes.
- One function chooses and returns the check-in lane the reservation should
  use.

You decide the function names and the parameters needed for each function.

## Required Shared Outputs

- A whole-number estimate of wait time in minutes.
- A lane choice of `Priority` or `Standard`.

## Available Inputs

The starting app has the number of people already ahead in line, the estimated
seconds needed to serve one person, and whether the reservation holder has a
priority pass.

## Business Rules

- Estimate the wait before this reservation reaches the check-in desk. The
  number of guests in the arriving reservation does not change this estimate.
- Each person ahead takes the given number of seconds to serve.
- Practice using a loop by adding the seconds once for each person ahead.
- Convert total seconds to minutes and round up to a whole minute without
  importing `math`.
- One technique is to use integer division by `60`, then add `1` if there is a
  remainder.
- If no people are ahead, the wait is `0`.
- Choose `Priority` if the reservation holder has a priority pass.
- Event policy also uses the `Priority` lane when more than 20 people are
  ahead.
- Otherwise choose `Standard`.

## Who Uses Your Outputs?

The Final Check-In Decision team needs the wait estimate. `app.py` will display
both the wait time and the lane.

## Examples To Discuss

```text
0 people ahead at 45 seconds each -> 0 minutes
10 people ahead at 45 seconds each -> 8 minutes
4 people ahead at 30 seconds each -> 2 minutes
10 people ahead with a priority pass -> Priority
25 people ahead without a priority pass -> Priority
5 people ahead without a priority pass -> Standard
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
