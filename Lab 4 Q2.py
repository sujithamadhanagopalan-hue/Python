'''
Create a Python program that simulates a parking
facility for an entire day. Using loops, process vehicle entries and
exits, calculate parking charges based on duration, track occupancy
levels, identify peak usage periods, and generate end-of-day statistics
such as total revenue and average parking time.

'''
parking_capacity = 100
hourly_rate = 10.00  #Rs. 10 per hour
current_occupancy = 0
total_revenue = 00.0
total_vehicles_served = 0
total_parking_hours = 0

occupancy_history = []
revenue_history = []

print("Parking Fascility Tracker")

for hour in range(1, 6):
    print(f"\n Hour{hour}:00")
    print(f"Current vehicles in lot: {current_occupancy}/{parking_capacity}")
    
    exiting_vehicles = int(input("How many vehicles are Exiting this hour? "))
    
    for i in range(exiting_vehicles):
        if current_occupancy > 0:
            duration = int(input(f"  How many hours did exiting vehicle {i+1} stay? "))
            
            charge = duration * hourly_rate
            total_revenue += charge
            total_parking_hours += duration
            total_vehicles_served += 1
            
            current_occupancy -= 1
        else:
            print("  parking is already empty! No more vehicles can exit.")
            break

    entering_vehicles = int(input("How many vehicles are entering this hour? "))
    
    for i in range(entering_vehicles):
        if current_occupancy < parking_capacity:
            current_occupancy += 1
        else:
            print(f" parking is FULL! Vehicle {i+1} was turned away.")
            
    occupancy_history.append(current_occupancy)

peak_occupancy = occupancy_history[0]
peak_hour = 1
for index, count in enumerate(occupancy_history):
    if count > peak_occupancy:
        peak_occupancy = count
        peak_hour = index + 1

if total_vehicles_served > 0:
    avg_stay = total_parking_hours / total_vehicles_served
else:
    avg_stay = 0

#Summary Report
print("\n" + "="*40)
print("summary")
print("="*40)
print(f"Total Revenue Generated : Rs.{total_revenue:.2f}")
print(f"Total Vehicles Served   : {total_vehicles_served}")
print(f"Average Parking Time    : {avg_stay:.1f} hours")
print(f"Peak Occupancy Level    : {peak_occupancy}/{parking_capacity} (at Hour {peak_hour}:00)")
print("="*40)
