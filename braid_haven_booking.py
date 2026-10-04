class Customer:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class VIP(Customer):
    def __init__(self, name, phone_number, vip_benefit):
        super().__init__(name, phone_number)
        self.vip_benefit = vip_benefit
vip1 = VIP("faith", "08056278153", "10% discount")
print(vip1.name)
print(vip1.phone_number)
print(vip1.vip_benefit)

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
option = 1
