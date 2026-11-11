
def print_report(stations, rides):
    print("Звіт адміністратора")
    for station in stations:
        print("Станція", station.name, "-", station.get_bikes_count(), "велосипедів")
    print("Загальна виручка:", rides.total_revenue, "грн")


def main():
    station_a = Station("A")
    station_b = Station("B")

    

if __name__ == "__main__":
    main()
