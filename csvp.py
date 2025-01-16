import os
import csv

# Path of folder
folder_path = '/Users/abishekkandel/Desktop/HIT137 Assignment 2 SS 2024/temperature_data'


# Initializing dictionaries to store the totals and counts for each month
monthly_totals = {month: 0 for month in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']}
monthly_counts = {month: 0 for month in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']}

# Initializing dictionaries to store the totals and counts for each season
season_totals = {'Summer': 0, 'Autumn': 0, 'Winter': 0, 'Spring': 0}
season_counts = {'Summer': 0, 'Autumn': 0, 'Winter': 0, 'Spring': 0}

# Initialize variables for finding the warmest, coolest station, and the station with the largest range
station_data = {}

# Iterating through all CSV files in the folder
for year in range(1986, 2006):
    file_name = f"stations_group_{year}.csv"
    file_path = os.path.join(folder_path, file_name)

    if os.path.exists(file_path):
        # Open and read the CSV file
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            # Process monthly data and add totals and counts
            for row in reader:
                for month in monthly_totals.keys():
                    if row[month]:
                        try:
                            temp = float(row[month])
                            monthly_totals[month] += temp
                            monthly_counts[month] += 1
                        except ValueError:
                            print(f"Skipping invalid temperature value in {month} for station {row['STATION_NAME']}")

                # Process seasonal data
                for month, season in [('December', 'Summer'), ('January', 'Summer'), ('February', 'Summer'),
                                      ('March', 'Autumn'), ('April', 'Autumn'), ('May', 'Autumn'),
                                      ('June', 'Winter'), ('July', 'Winter'), ('August', 'Winter'),
                                      ('September', 'Spring'), ('October', 'Spring'), ('November', 'Spring')]:
                    if row[month]:
                        try:
                            temp = float(row[month])
                            season_totals[season] += temp
                            season_counts[season] += 1
                        except ValueError:
                            print(f"Skipping invalid temperature value in {month} for station {row['STATION_NAME']}")

                # Process station data to find temperature range, warmest, and coolest station
                station_name = row['STATION_NAME']
                temperatures = [float(row[month]) for month in row.keys() if month not in ['STATION_NAME', 'STN_ID', 'LAT', 'LON'] and row[month]]
                
                if temperatures:  
                    temp_range = max(temperatures) - min(temperatures)
                    avg_temp = sum(temperatures) / len(temperatures)

                    if station_name not in station_data:
                        station_data[station_name] = {'temp_range': temp_range, 'avg_temp': avg_temp}
                    else:
                        # Keep the largest temperature range for each station
                        station_data[station_name]['temp_range'] = temp_range
                        station_data[station_name]['avg_temp'] = avg_temp

# Calculate the average temperature for each month
monthly_averages = {month: monthly_totals[month] / monthly_counts[month] if monthly_counts[month] > 0 else 0 for month in monthly_totals}

# Calculate the average temperature for each season
season_averages = {season: season_totals[season] / season_counts[season] if season_counts[season] > 0 else 0 for season in season_totals}

# Check if station_data is empty before finding the largest temperature range station
if station_data:
    largest_temp_range_station = max(station_data, key=lambda x: station_data[x]['temp_range'])
    warmest_station = min(station_data, key=lambda x: station_data[x]['avg_temp'])
    coolest_station = max(station_data, key=lambda x: station_data[x]['avg_temp'])
else:
    print("No station data available.")
    largest_temp_range_station = warmest_station = coolest_station = None

# Save the results to the respective files

# Average temperatures for each month
with open('average_temp.txt', 'w') as f:
    for month, avg_temp in monthly_averages.items():
        f.write(f"{month}: {avg_temp:.2f}°C\n")

# Average temperatures for each season
with open('average_temp_season.txt', 'w') as f:
    for season, avg_temp in season_averages.items():
        f.write(f"{season}: {avg_temp:.2f}°C\n")

# Largest temperature range station
with open('largest_temp_range_station.txt', 'w') as f:
    if largest_temp_range_station:
        f.write(f"Station with the largest temperature range: {largest_temp_range_station}\n")
    else:
        f.write("No station data available.\n")

# Warmest and coolest station
with open('warmest_and_coolest_station.txt', 'w') as f:
    if warmest_station and coolest_station:
        f.write(f"Warmest station: {warmest_station}\n")
        f.write(f"Coolest station: {coolest_station}\n")
    else:
        f.write("No station data available.\n")

print("The results have been calculated and saved to the respective file")