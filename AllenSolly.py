import time
import datetime
import random
class Allen_Solly_Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.cart = []
        self.users = {}

    def display_menu(self):
        print(f"Welcome to {self.store_name}!")
        print("1. Clothing")
        print("2. Accessories")
        print("3. Makeup")
        print("4. Perfumes")

    def display_clothing_menu(self):
        print("Clothing Options:")
        print("1. T-shirts - $10")
        print("2. Blouses - $20")
        print("3. Sweaters - $30")
        print("4. Hoodies - $25")
        # Add more clothing options as needed

    def display_accessories_menu(self):
        print("Accessories Options:")
        print("1. Hats - $15")
        print("2. Necklaces - $25")
        print("3. Bracelets - $18")
        print("4. Earrings - $12")
        # Add more accessories options as needed

    def display_makeup_menu(self):
        print("Makeup Options:")
        print("1. Foundation - $30")
        print("2. Lipstick - $15")
        print("3. Eyeshadow Palette - $25")
        print("4. Mascara - $12")
        # Add more makeup options as needed

    def display_perfumes_menu(self):
        print("Perfumes Options:")
        print("1. Floral Eau de Parfum - $50")
        print("2. Citrus Eau de Toilette - $40")
        print("3. Woody Eau de Cologne - $45")
        print("4. Oriental Eau de Parfum - $55")
        # Add more perfume options as needed

    def add_to_cart(self, item, price, quantity, size=None):
        self.cart.append((item, price, quantity, size))

    def display_cart(self):
        print("\nYour Shopping Cart:")
        for item, price, quantity, size in self.cart:
            print(f"{item} (Size: {size}, Quantity: {quantity}): ${price * quantity}")
        total_price_allensolly = sum(price * quantity for _, price, quantity, _ in self.cart)
        print(f"\nTotal Price: ${total_price_allensolly}")
        return total_price_allensolly, self.cart

    # def login(self, username, password):
    #     # Simple login mechanism for demonstration purposes
    #     if username in self.users and self.users[username] == password:
    #         print(f"Welcome, {username}!")
    #         return True
    #     else:
    #         print("Invalid username or password. Please try again.")
    #         return False

    # def register(self, username, password):
    #     # Simple registration mechanism for demonstration purposes
    #     if username not in self.users:
    #         self.users[username] = password
    #         print(f"User {username} registered successfully!")
    #     else:
    #         print("Username already exists. Please choose a different username.")
            
    
#main

# def display_feedback():
#     print("\n=========================")
#     print("Feedback:")
#     print("Thank you for shopping with us!")
#     print("We value your feedback. Please leave a review.")
#     feedback = input("Enter your feedback: ")
#     print("Feedback submitted successfully!")
#     print("=========================")

# def main():
#     allen_dolly_store = Allen_Solly_Store("Allen Solly Store")

#     # Simple login/register system
#     while True:
#         action = input("Do you want to login or register? (login/register): ").lower()
#         if action == "login":
#             username = input("Enter your username: ")
#             password = input("Enter your password: ")
#             if allen_dolly_store.login(username, password):
#                 break
#         elif action == "register":
#             username = input("Enter a new username: ")
#             password = input("Enter a new password: ")
#             allen_dolly_store.register(username, password)

#     while True:
#         allen_dolly_store.display_menu()
#         category_choice = input("Select a category (1-4) or 'q' to quit: ")

#         if category_choice == 'q':
#             break

#         if category_choice == '1':
#             allen_dolly_store.display_clothing_menu()
#             clothing_choice = input("Select a clothing item (1-4): ")
#             size = input("Enter size (optional): ")
#             quantity = int(input("Enter quantity: "))
#             allen_dolly_store.add_to_cart("Clothing", 10, quantity, size)  # Assuming a standard price for clothing

#         elif category_choice == '2':
#             allen_dolly_store.display_accessories_menu()
#             accessories_choice = input("Select an accessories item (1-4): ")
#             quantity = int(input("Enter quantity: "))
#             allen_dolly_store.add_to_cart("Accessories", 15, quantity)  # Assuming a standard price for accessories

#         elif category_choice == '3':
#             allen_dolly_store.display_makeup_menu()
#             makeup_choice = input("Select a makeup item (1-4): ")
#             quantity = int(input("Enter quantity: "))
#             allen_dolly_store.add_to_cart("Makeup", 20, quantity)  # Assuming a standard price for makeup

#         elif category_choice == '4':
#             allen_dolly_store.display_perfumes_menu()
#             perfume_choice = input("Select a perfume item (1-4): ")
#             quantity = int(input("Enter quantity: "))
#             allen_dolly_store.add_to_cart("Perfumes", 50, quantity)  # Assuming a standard price for perfumes

#     total_price_allensolly, cart = allen_dolly_store.display_cart()

#     # Display detailed bill
#     print("\n\n=========================")
#     print("Detailed Bill:")
#     for item, price, quantity, size in cart:
#         print(f"{item} (Size: {size}, Quantity: {quantity}): ${price * quantity}")

#     print("\nTotal Price: ${total_price_allensolly}")
#     print("=========================")

#     # Display feedback
#     display_feedback()

# if __name__ == "__main__":
#     main()
