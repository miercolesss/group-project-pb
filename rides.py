
class Rides:
    def __init__(self):
        self.total_revenue = 0 #виручка
        
    def calculate_cost(self, bike, time):
        return bike.get_price_per_minute() * time
            
    

    def trip_details(self, client, start_station, end_station, time):

        pass
