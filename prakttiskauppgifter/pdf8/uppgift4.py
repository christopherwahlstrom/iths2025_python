from datetime import datetime, timedelta
import calendar

def add_months(source_date, months):
    """
    Hjälpfunktion för att lägga till månader korrekt.
    Hanterar årsskiften och olika antal dagar i månader.
    """
    month = source_date.month - 1 + months
    year = source_date.year + month // 12
    month = month % 12 + 1
    day = min(source_date.day, calendar.monthrange(year, month)[1])
    
    return source_date.replace(year=year, month=month, day=day)

def time_travel_calculator():
    print("--- Time Travelers Calculator ---")
    print("Ange startdatum och tid för resan.")
    
    date_input = input("Startdatum (YYYY-MM-DD HH:MM): ")
    
    try:
        start_date = datetime.strptime(date_input, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Felaktigt format! Använd YYYY-MM-DD HH:MM (t.ex. 2023-10-25 14:30)")
        return

    print("\nHur långt vill du resa?")
    try:
        years = int(input("År: "))
        months = int(input("Månader: "))
        days = int(input("Dagar: "))
        hours = int(input("Timmar: "))
        minutes = int(input("Minuter: "))
    except ValueError:
        print("Fel: Vänligen ange endast heltal för tidsenheterna.")
        return

    # Beräkna nytt datum
    # 1. Lägg till år och månader (kräver specialhantering)
    # Vi lägger till år genom att konvertera till månader först för enkelhetens skull,
    # eller bara addera år direkt om vi litar på add_months logiken.
    # Låt oss använda add_months för totala antalet månader (år * 12 + månader)
    
    total_months_to_add = (years * 12) + months
    temp_date = add_months(start_date, total_months_to_add)
    
    # 2. Lägg till dagar, timmar, minuter (kan göras med timedelta)
    final_date = temp_date + timedelta(days=days, hours=hours, minutes=minutes)

    print("\n" + "="*30)
    print(f"Startdatum: {start_date}")
    print(f"Resa: {years} år, {months} mån, {days} dagar, {hours} tim, {minutes} min")
    print("-" * 30)
    print(f"Du kommer att anlända den: {final_date.strftime('%Y-%m-%d kl. %H:%M')}")
    print("="*30)

if __name__ == "__main__":
    time_travel_calculator()
