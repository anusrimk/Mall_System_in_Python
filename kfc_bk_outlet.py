import time
import datetime
import random

class FoodOutlet:
    def __init__(self, name, menu, special_offers=None):
        self.name = name
        self.menu = menu
        self.special_offers = special_offers or {}
        self.user = None

    def create_account(self):
        print("\nCreate Your Account:")
        name = input("Enter your name: ")
        acc_number = input("Enter your account number: ")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        return {"name": name, "acc_number": acc_number, "username": username, "password": password}

    def welcome_user(self):
        current_time = datetime.datetime.now().time()
        greeting = "\033[92mGood morning\033[0m"
        if current_time >= datetime.time(12, 0) and current_time < datetime.time(17, 0):
            greeting = "\033[93mGood afternoon\033[0m"
        elif current_time >= datetime.time(17, 0):
            greeting = "\033[91mGood evening\033[0m"

        print(f"{greeting}, {self.user['name']}! Welcome to {self.name}.")

    def display_menu(self):
        print(f"\n{self.name} Menu:")
        for item, price in self.menu.items():
            print(f"{item}: ₹{price}")
        
        if self.special_offers:
            print("\nSpecial Offers:")
            for offer, discount in self.special_offers.items():
                print(f"{offer}: {discount}% off")

    def take_order(self):
        order = {}
        while True:
            item = input("Enter the item you want to order (or type 'done' to finish): ")
            if item.lower() == 'done':
                break
            elif item in self.menu:
                quantity = int(input(f"How many {item}s do you want? "))
                order[item] = quantity
            else:
                print("Invalid item. Please choose from the menu.")
        return order

    def calculate_total(self, order):
        total = sum(self.menu[item] * quantity for item, quantity in order.items())
        return total

    def generate_bill(self, order, total):
        print("\nCalculating your bill...", end='', flush=True)
        for _ in range(3):
            time.sleep(0.5)
            print(".", end='', flush=True)
        print("\n\033[94mOrder Summary:\033[0m")
        for item, quantity in order.items():
            print(f"{item}: {quantity} x ₹{self.menu[item]} = ₹{quantity * self.menu[item]}")
        print(f"\033[94mTotal: ₹{total}\033[0m")
        print("\033[92mThank you for ordering with us!\033[0m")

    def feedback(self):
        feedback_responses = [
            "Thank you for your feedback! You rated us {rating} stars.",
            "We appreciate your input! Your rating: {rating} stars.",
            "Your feedback is important to us. You gave us {rating} stars. Thank you!",
        ]

        rating = input("Please rate your experience (1 to 5 stars): ")
        if rating.isdigit() and 1 <= int(rating) <= 5:
            response = random.choice(feedback_responses).format(rating=rating)
            print(response)
        else:
            print("Invalid rating. Feedback not submitted.")

# # def main():
#     # Define menus for Burger King and KFC
#     burger_king_menu = {"Whopper": 220, "Cheeseburger": 199, "Fries": 69, "BK Grill Chicken": 280,
#                         "BK Veggie": 150, "King Jr. Meals (For Kids)": 350, "Veg Chilli Cheese Melt": 219,
#                         "Veggie Strips": 119, "Brownie Sundaes": 129, "Iced Tea": 100, "Coffee": 150}
    
#     kfc_menu = {"Chicken Buckets": 400, "Burgers": 200, "Chicken Tenders": 270, "Rice Bowlz": 220,
#                 "Wraps": 120, "Hot Wings": 170, "Sides": 100, "Desserts": 90, "Beverages": 150}

#     # Example of special offers
#     burger_king_special_offers = {"Family Bundle": 15, "Student Discount": 10}
#     kfc_special_offers = {"Super Saver Combo": 20, "Happy Hour": 15}

#     # Create instances of FoodOutlet
#     burger_king = FoodOutlet("Burger King", burger_king_menu, burger_king_special_offers)
#     kfc = FoodOutlet("KFC", kfc_menu, kfc_special_offers)

#     # Create user account
#     user_account = burger_king.create_account()

#     # Set user account in the FoodOutlet instances
#     burger_king.user = user_account
#     kfc.user = user_account

#     # Display the user's information
#     print("\nUser Information:")
#     print(f"Name: {user_account['name']}")
#     print(f"Account Number: {user_account['acc_number']}")
#     print(f"Username: {user_account['username']}")

#     # Offer a choice for ordering
#     print("\nSelect a food outlet to order from:")
#     print("1. Burger King")
#     print("2. KFC")

#     outlet_choice = input("Enter the number of your chosen food outlet: ")

#     if outlet_choice == "1":
#         food_outlet = burger_king
#     elif outlet_choice == "2":
#         food_outlet = kfc
#     else:
#         print("Invalid choice. Exiting.")
        

#     # Welcome user to the selected food outlet
#     food_outlet.welcome_user()

#     # Display menu and take orders
#     food_outlet.display_menu()
#     order = food_outlet.take_order()

#     # Introduce a fun loading animation
#     time.sleep(1)
#     print("\nGenerating your bill", end='', flush=True)
#     for _ in range(3):
#         time.sleep(0.5)
#         print(".", end='', flush=True)

#     total = food_outlet.calculate_total(order)
#     food_outlet.generate_bill(order, total)

#     # Ask for feedback
#     time.sleep(1)  # Add a delay for a better user experience
#     food_outlet.feedback()

# # if __name__ == "__main__":
# #     main()