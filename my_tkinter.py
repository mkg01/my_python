import requests
import tkinter as tk

# Create object
root = tk.Tk()

# add text/greeting
greeting = tk.Label(text="Welcome to our Weather App GUI!")
today_temp = tk.Label(text="Today's temp. is: ")

greeting.pack()
today_temp.pack()

# Create a Button
btn = tk.Button(root, text='Click me !', bd='10', command=lambda:display_data(today_temp))
def get_data():
    x = requests.get("https://api.weather.gov/gridpoints/EWX/156,96/forecast")
    decoded_data = x.json()  # decode our data with the .json() method
    data_for_each_day = decoded_data['properties']['periods'][0]['temperature']
    return data_for_each_day
def display_data(label_to_update):
    data = get_data()
    label_to_update.config(text = data)


# Set the position of button on the top of window.
btn.pack(side='top')

# Adjust size
root.geometry("400x400")

# Execute tkinter
root.mainloop()










x = requests.get("https://api.weather.gov/gridpoints/EWX/156,96/forecast")

decoded_data = x.json()  # decode our data with the .json() method

data_for_each_day = decoded_data['properties']['periods'][0]
# print(data_for_each_day['windSpeed'])
# print(data_for_each_day['name'],data_for_each_day['temperature'])
# for each in data_for_each_day:
#    print(each)
# print(data_for_each_day)
# we can now access this JSON file, bound to decoded_data, w/ indexingrint("Hello")