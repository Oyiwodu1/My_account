class Customer:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class VIP(Customer):
    def __init__(self, name, phone_number, vip_benefit):
        super().__init__(name, phone_number)
        self.vip_benefit = vip_benefit

class Booking:
    def __init__(self, customer, hairstyle, date, time):
        self.customer = customer
        self.hairstyle = hairstyle
        self.date = date
        self.time = time

services = {
    "Knotless Braids": 30000,
    "Shuku": 45000,
    "French curls": 50000,
    "Jada wayda": 34000
}

bookings = []
print("Welcome to Braid Haven Booking System!")

print("1. Make a booking")
print("2. View bookings")
print("3. Exit")

option = input("Choose an option: ")

if option == "1":
    name = input("What is your name? ")
    number = input("Your phone number: ")
    vip = input("Are you a VIP customer? ")

    if vip == "yes":
        vip_benefit = input("what vip benefit do you have? ")
        client = VIP(name, number, vip_benefit)

    else:
        client = Customer(name, number)

    for styles in services:
        print(styles)
    selected_style = input("Choose a style: ")
    price = services[selected_style]
    print(price)