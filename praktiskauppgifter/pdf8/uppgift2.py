from datetime import datetime, timedelta

def date_range(start_date, end_date, interval_days):
    """
    En generator som yieldar datum från start_date till end_date
    med ett givet intervall i dagar.
    """
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        print(f"Beräknar nästa datum efter {current_date.strftime('%Y-%m-%d')}")
        current_date += timedelta(days=interval_days)

if __name__ == "__main__":
    # Definiera start- och slutdatum
    start = datetime(2024, 1, 1)
    end = datetime(2024, 1, 15)
    interval = 1

    print(f"Datum mellan {start.date()} och {end.date()} med {interval} dagars intervall:\n")

    # Använd generatorn i en loop
    for date in date_range(start, end, interval):
        print(date.strftime("%Y-%m-%d"))
