PRICE_REGULAR_BIKE = 2
PRICE_ELECTRIC_BIKE = 5

class Rides:
    def __init__(self):
        pass
    def calculate_cost(self, bike, time):
        if bike.is_electric:
            price = PRICE_ELECTRIC_BIKE
        else:
            price = PRICE_REGULAR_BIKE
        return price * time
            
    

    def trip_details(self, client, start_station, end_station, time, bike):

        pass
