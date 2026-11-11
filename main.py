from bikes import Bike, Station
from clients import Client
from trips import Rides


def show_result(client, success, info):
    if success:
        print(client.name + ": поїздка успішна, вартість", info, "грн")
    else:
        print(client.name + ": помилка -", info)


def print_report(stations, rides):
    print("Звіт адміністратора")
    for station in stations:
        print("Станція", station.name, "-", station.get_bikes_count(), "велосипедів")
    print("Загальна виручка:", rides.total_revenue, "грн")

    print("Електровелосипеди з низьким зарядом:")
    for station in stations:
        for bike in station.get_low_charge_bikes():
            print(f"  №{bike.number}, станція {station.name}, заряд {bike.charge}%")


def main():
    station_a = Station("A")
    station_b = Station("B")

    station_a.add_bike(Bike(1))
    station_a.add_bike(Bike(2, True))
    station_a.add_bike(Bike(3))
    station_b.add_bike(Bike(4, is_electric=True, charge=10))  

    olya = Client("Оля", 100)
    taras = Client("Тарас", 100)

    rides = Rides()

    
    success, info = rides.trip_details(taras, station_b, station_a, 5)
    show_result(taras, success, info)
    assert not success

    success, info = rides.trip_details(olya, station_a, station_b, 20)
    show_result(olya, success, info)

    success, info = rides.trip_details(taras, station_a, station_b, 10)
    show_result(taras, success, info)

    print("Баланс Олі:", olya.balance)
    print("Баланс Тараса:", taras.balance)

    print_report([station_a, station_b], rides)

    assert station_a.get_bikes_count() + station_b.get_bikes_count() == 4
    assert rides.total_revenue == 90
    assert olya.balance == 60
    assert taras.balance == 50


if __name__ == "__main__":
    main()
