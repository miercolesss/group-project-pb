from station import Bike, Station
from customer import Client
from rides import Trip


def print_report(stations, trip):
    print("Звіт адміністратора")
    for station in stations:
        print("Станція", station.name, "-", station.get_bikes_count(), "велосипедів")
    print("Загальна виручка:", trip.total_revenue, "грн")


def main():
    station_a = Station("A")
    station_b = Station("B")

    station_a.add_bike(Bike(1))
    station_a.add_bike(Bike(2, True))
    station_b.add_bike(Bike(3))
    station_b.add_bike(Bike(4, True))

    olya = Client("Оля", 100)
    taras = Client("Тарас", 40)

    trip = Trip()

    result = trip.process_trip(olya, station_a, station_b, 20)
    if result == "ok":
        print("Оля поїхала")
    else:
        print("Не вдалося:", result)

    result = trip.process_trip(taras, station_b, station_a, 10)
    if result == "ok":
        print("Тарас поїхав")
    else:
        print("Не вдалося:", result)

    result = trip.process_trip(olya, station_a, station_b, 5)
    if result == "ok":
        print("Оля поїхала ще раз")
    else:
        print("Не вдалося:", result)

    print("Баланс Олі:", olya.balance)
    print("Баланс Тараса:", taras.balance)

    print_report([station_a, station_b], trip)

    assert station_a.get_bikes_count() + station_b.get_bikes_count() == 4
    assert trip.total_revenue > 0


if __name__ == "__main__":
    main()
