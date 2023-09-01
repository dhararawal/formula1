import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


circuits = pd.read_csv('/Users/d.r/Desktop/MSc/portfolio/formula1/formula1/circuits.csv')
constructor_result = pd.read_csv('/Users/d.r/Desktop/MSc/portfolio/formula1/formula1/constructor_results.csv')
constructor = pd.read_csv('/Users/d.r/Desktop/MSc/portfolio/formula1/formula1/constructors.csv')
constructor_standing = pd.read_csv('/Users/d.r/Desktop/MSc/portfolio/formula1/formula1/constructor_standings.csv')
driver_standings = pd.read_csv('/Users/d.r/Desktop/MSc/portfolio/formula1/formula1/driver_standings.csv')
drivers = pd.read_csv('/Users/d.r/Desktop/MSc/portfolio/formula1/formula1/drivers.csv')
lap_times = pd.read_csv('/Users/d.r/Desktop/MSc/portfolio/formula1/formula1/lap_times.csv')
pit_stops = pd.read_csv('/Users/d.r/Desktop/MSc/portfolio/formula1/formula1/pit_stops.csv')
status = pd.read_csv('/Users/d.r/Desktop/MSc/portfolio/formula1/formula1/status.csv')
qualifying = pd.read_csv('/Users/d.r/Desktop/MSc/portfolio/formula1/formula1/qualifying.csv')
races = pd.read_csv('/Users/d.r/Desktop/MSc/portfolio/formula1/formula1/races.csv')
results = pd.read_csv('/Users/d.r/Desktop/MSc/portfolio/formula1/formula1/results.csv')
seasons = pd.read_csv('/Users/d.r/Desktop/MSc/portfolio/formula1/formula1/seasons.csv')



driver_column_names = list(drivers.columns)
driver_standings_column_names = list(driver_standings.columns)
print("Driver's column names: ", driver_column_names)
print("Driver Standings column names: ", driver_standings_column_names)

constructor_column_names = list(constructor.columns)
print("Constructor's column names: ", constructor_column_names)
constructor_result_column_names = list(constructor_result.columns)
print("Constructor's Results column names: ", constructor_result_column_names)

merged_data = pd.merge(drivers, driver_standings, on="driverId")
merged_data = pd.merge(merged_data, races, on="raceId")
merged_data = pd.merge(merged_data, circuits, on="circuitId")
merged_data = pd.merge(merged_data, constructor_result, on="raceId")
merged_data_columns = list(merged_data.columns)

print("Merged Data column names: ", merged_data_columns)
merged_data = merged_data.drop(columns=['url', 'url_x', 'driverRef', 'number', 'code', 'forename', 'dob', 'positionText', 'date', 'location', 'url_y', 'time', 'fp1_date', 'fp1_time', 'fp2_date', 'fp2_time', 'fp3_date', 'fp3_time', 'quali_date', 'quali_time', 'lat', 'lng', 'alt', 'sprint_date', 'sprint_time', 'circuitRef', 'country', 'points_y'])
merged_data_columns = list(merged_data.columns)
print("Merged Data column names: ", merged_data_columns)


driver_points = merged_data.groupby("surname")['points_x'].sum()
top_drivers = driver_points.sort_values(ascending=False).head(10)
print(top_drivers)


plt.figure(figsize = (12, 10))
top_drivers.plot(kind = "bar", color="blue")
plt.xlabel("Driver")
plt.ylabel("Points")
plt.title("Top 10 Most Successful Drivers in Formula 1 History")
plt.xticks(rotation=45)
plt.show()

