"""Class integration workspace for the Event Check-In Operations Lab."""

# TODO: After team contracts are approved, import the approved team functions.


def process_reservation(
    age,
    is_student,
    is_veteran,
    total_guests_in_reservation,
    is_online,
    total_checked_in,
    event_capacity,
    people_ahead,
    estimated_minutes_per_person,
    has_priority_pass,
):
    """Process one reservation and return its operations results.

    This is the app-level contract the class tests during integration. It
    accepts the starting information collected by main() and, once completed,
    returns a dictionary with these results:

        ticket_rate
        subtotal
        discount
        service_fee
        capacity_percent
        check_in_permission
        wait_minutes
        lane
        quoted_amount
        status
    """
    # TODO: Call the two approved Ticket Pricing functions.
    # TODO: Call the two approved Discounts and Fees functions.
    # TODO: Call the two approved Capacity Management functions.
    # TODO: Call the two approved Wait Time Estimator functions.
    # TODO: Call the two approved Final Check-In Decision functions.
    # TODO: Return the operations results in a dictionary using the keys above.
    pass


def main():
    """Collect reservation information and display the completed app results."""
    print("Event Check-In Operations")
    print("Enter information for one arriving reservation.")

    # For this lab, assume the user enters valid whole numbers when requested.
    age = int(input("Reservation holder age: "))
    is_student = input("Is the reservation holder a student? (y/n): ").lower() == "y"
    is_veteran = input("Is the reservation holder a veteran? (y/n): ").lower() == "y"
    total_guests_in_reservation = int(input("Number of guests in the reservation: "))
    is_online = input("Was the reservation completed online? (y/n): ").lower() == "y"
    total_checked_in = int(input("Number of guests already checked in: "))
    event_capacity = int(input("Maximum event capacity: "))
    people_ahead = int(input("Number of people ahead in line: "))
    estimated_minutes_per_person = int(input("Estimated seconds to serve one person: "))
    has_priority_pass = input("Does the reservation holder have a priority pass? (y/n): ").lower() == "y"

    results = process_reservation(
        age,
        is_student,
        is_veteran,
        total_guests_in_reservation,
        is_online,
        total_checked_in,
        event_capacity,
        people_ahead,
        estimated_minutes_per_person,
        has_priority_pass,
    )

    if results is None:
        print("Integration is not complete yet.")
        return

    print("\nOperations Summary")
    print("Ticket rate:", results["ticket_rate"])
    print("Subtotal:", results["subtotal"])
    print("Discount:", results["discount"])
    print("Service fee:", results["service_fee"])
    print("Quoted final amount:", results["quoted_amount"])
    print("Current capacity used:", results["capacity_percent"])
    print("Check-in permission:", results["check_in_permission"])
    print("Wait minutes:", results["wait_minutes"])
    print("Lane:", results["lane"])
    print("Status:", results["status"])


if __name__ == "__main__":
    main()
