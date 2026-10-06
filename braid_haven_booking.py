class Customer:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class VIP(Customer):
    def __init__(self, name, phone_number, vip_benefit):
        super().__init__(name, phone_number)
        self.vip_benefit = vip_benefit

class Booking:
    def __init__(self, customer, hairstyle, price, date, time):
        self.customer = customer
        self.hairstyle = hairstyle
        self.price = price
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

while True:

    print("1. Make a booking")
    print("2. View bookings")
    print("3. Exit")

    option = input("Choose an option: ")

    if option == "1":
        name = input("Enter your name? ")
        number = input("Enter your phone number: ")
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

        available_slots = {
            "October 8": ["10:00AM", "3:30PM"],
            "October 15": ["8:00AM", "1:30PM", "4:00PM"],
            "October 21": ["9:30AM"]
        }

        for date in available_slots:
            print(date)
            print(f"Available times: {available_slots[date]}")

        booking_date = input("Choose a date: ")
        print(available_slots[booking_date])
        booking_time = input("Choose a time: ")

        booking = Booking(client, selected_style, price, booking_date, booking_time)
        bookings.append(booking)
        print("Booking successful!")

    elif option == "2":
        if bookings:
            for book in bookings:
                print("--- Booking Details---")
                print(f"Name: {book.customer.name}")
                print(f"Hairstyle: {book.hairstyle}")
                print(f"Price: {book.price}")
                print(f"Date: {book.date}")
                print(f"Time: {book.time}")


        else:
            print("No booking yet!")

    elif option == "3":
        print("EXIT!")
        break