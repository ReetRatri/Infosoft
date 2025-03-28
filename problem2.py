class FuelStation:
    def __init__(self, diesel: int, petrol: int, electric: int):
        self.spots = {
            "diesel": diesel,
            "petrol": petrol,
            "electric": electric
        }

    def fuel_vehicle(self, fuel_type: str) -> bool:
       
        if self.spots.get(fuel_type, 0) > 0:
          
            self.spots[fuel_type] -= 1
            return True
        return False

    def open_fuel_slot(self, fuel_type: str) -> bool:
        
        if self.spots.get(fuel_type, 0) < 0:
            return False
        self.spots[fuel_type] += 1
        return True
mnkllkm
fuel_station = FuelStation(diesel=2, petrol=2, electric=1)

print(fuel_station.fuel_vehicle("diesel"))    
print(fuel_station.fuel_vehicle("petrol"))    
print(fuel_station.fuel_vehicle("diesel"))    
print(fuel_station.fuel_vehicle("petrol"))    
print(fuel_station.fuel_vehicle("diesel"))    
print(fuel_station.fuel_vehicle("electric"))  
print(fuel_station.fuel_vehicle("diesel"))    


print(fuel_station.open_fuel_slot("diesel"))  
print(fuel_station.fuel_vehicle("diesel"))    
print(fuel_station.open_fuel_slot("electric"))  
print(fuel_station.open_fuel_slot("electric"))  
