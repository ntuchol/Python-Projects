def print_after_n_events(event_count_limit, string_to_print):
    """
    Prints a string after a specific event has occurred N number of times.

    Args:
        event_count_limit (int): The number of times the event must occur before printing.
        string_to_print (str): The string to print after the event count is reached.
    """
    event_counter = 0
    while True:  # Simulate a continuous stream of events
        # Simulate an event occurring
        # In a real application, this would be triggered by an actual event
        # (e.g., a button click, a data packet received, a file read)
        event_occurred = True  # Replace with actual event detection logic

        if event_occurred:
            event_counter += 1
            print(f"Event occurred. Current count: {event_counter}")

            if event_counter >= event_count_limit:
                print(string_to_print)
                break  # Stop after printing
        # Add a small delay in a real-world scenario to avoid busy-waiting
        # import time
        # time.sleep(0.1)

# Example usage:
print_after_n_events(5, "The event has occurred 5 times!")