def print_report(stations, trip):
    print("Звіт адміністратора")
    for station in stations:
        print("Станція", station.name, "-", station.get_bikes_count(), "велосипедів")
    print("Загальна виручка:", trip.total_revenue, "грн")
