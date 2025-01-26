import csv
from datetime import datetime

from matplotlib import pyplot as plt
import sys


filename = 'sitka_weather_2018_simple.csv'

def read_weather_data():
    
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        low = int(row[8])
        highs.append(high)
        lows.append(low)
    return dates, highs, lows

def plot_temperatures(dates, temperatures, title, color):
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, c=color)
    
# Format plot.
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    
#Display plot
plt.show()

def main():
#main function for program
print("Welcome to the Sitka Weather Program")
print("Options: ")
print("1. View high temperatures")
print("2. View low temperat
print("3. Exit the program")

#Read the weather data, get user input, and create loop
dates, highs, lows = read_weather_data()
      
while True:
        user_choice = input(f"Please select an option from (1-3): ")

        if user_choice == '1':
#Display high temperatures
            plot_temperatures(dates, highs, "Daily High Temperatures - 2018", 'red')

        elif user_choice == '2':
#Display low temperatures in blue
            plot_temperatures(dates, lows, "Daily Low Temperatures - 2018", 'blue')

        elif user_choice == '3':
#Exit the program
            print("Thank you for using the Sitka Weather Program, Goodbye!")
            sys.exit()  #Exit the program

        else:
            print("Invalid option. Please choose a valid option (1-3).")

# Call the main function
if __name__ == '__main__':
    main()      

      
    
