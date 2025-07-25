def print_after_n_events(event_count_limit, string_to_print):
    
    event_counter = 0
    while True:  
        event_occurred = True  

        if event_occurred:
            event_counter += 1
            print(f"Event occurred. Current count: {event_counter}")

            if event_counter >= event_count_limit:
                print(string_to_print)
                break  
       
print_after_n_events(5, "The event has occurred 5 times!")
