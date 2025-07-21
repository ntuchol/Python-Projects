import datetime

daily_event_counts = {}  # Store daily event counts

def record_event():
    today = datetime.date.today()
    daily_event_counts[today] = daily_event_counts.get(today, 0) + 1  # Increment the event count for the current day

def get_mean_daily_events(num_days):
    # Calculate the average daily event count over the past 'num_days'
    recent_dates = sorted(daily_event_counts.keys(), reverse=True)[:num_days]
    total_events = sum(daily_event_counts[date] for date in recent_dates)  # Calculate total events in the window
    return total_events / len(recent_dates) if recent_dates else 0  # Avoid division by zero

def check_and_print_string(threshold_percentage):
    current_day = datetime.date.today()
    current_day_count = daily_event_counts.get(current_day, 0)

    mean_daily_count = get_mean_daily_events(num_days=7)  # Use the last 7 days for the mean, for example

    if mean_daily_count > 0 and current_day_count > (mean_daily_count * (1 + threshold_percentage / 100)):
        print(f"Alert! Event count ({current_day_count}) is more than {threshold_percentage}% above the mean daily count ({mean_daily_count:.2f}).")