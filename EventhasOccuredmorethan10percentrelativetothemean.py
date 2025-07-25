import datetime

daily_event_counts = {}  

def record_event():
    today = datetime.date.today()
    daily_event_counts[today] = daily_event_counts.get(today, 0) + 1  

def get_mean_daily_events(num_days):
    recent_dates = sorted(daily_event_counts.keys(), reverse=True)[:num_days]
    total_events = sum(daily_event_counts[date] for date in recent_dates)  
    return total_events / len(recent_dates) if recent_dates else 0  

def check_and_print_string(threshold_percentage):
    current_day = datetime.date.today()
    current_day_count = daily_event_counts.get(current_day, 0)

    mean_daily_count = get_mean_daily_events(num_days=7)  

    if mean_daily_count > 0 and current_day_count > (mean_daily_count * (1 + threshold_percentage / 100)):
        print(f"Alert! Event count ({current_day_count}) is more than {threshold_percentage}% above the mean daily count ({mean_daily_count:.2f}).")
