import math

price_per_gallon = 3.90
miles_per_gallon = 25.0
trip_miles = 750.0
tank_gallons = 19.5

gallons_needed = trip_miles / miles_per_gallon
total_cost = gallons_needed * price_per_gallon
miles_per_tank = tank_gallons * miles_per_gallon
stops_needed = max(0, math.ceil(trip_miles / miles_per_tank) - 1)

print(f"For a {trip_miles:.0f}-mile trip, gas costs ${total_cost:.2f} and you'll need {stops_needed} stop(s).")