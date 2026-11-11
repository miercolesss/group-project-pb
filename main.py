
def print_report(stations, rides):
    print("Звіт адміністратора")
    for station in stations:
        print("Станція", station.name, "-", station.get_bikes_count(), "велосипедів")
    print("Загальна виручка:", rides.total_revenue, "грн")


def main():
    station_a = Station("A")
    station_b = Station("B")
    station_a.add_bike(Bike(1))
    station_a.add_bike(Bike(2, True))
    station_a.add_bike(Bike(3))
    station_b.add_bike(Bike(4, True))

    olya = Client("Оля", 100)
    taras = Client("Тарас", 100)

    

    

if __name__ == "__main__":
    main()
