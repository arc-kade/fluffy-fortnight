from abc import ABC, abstractmethod

# ==========================================
# 1. ENCAPSULATION & BASE CLASS
# ==========================================
class FoodItem:
    """Base class for all food items."""
    def __init__(self, food_id, name, category, price):
        # Protected attributes to demonstrate encapsulation
        self._food_id = food_id  
        self._name = name
        self._category = category
        self._price = price

    # Getter methods for safe access
    def get_id(self): return self._food_id
    def get_name(self): return self._name
    def get_category(self): return self._category
    def get_price(self): return self._price

    def display_details(self):
        """Displays common food item details."""
        return f"[{self._food_id}] {self._name} ({self._category}) - ₹{self._price}"

    def calculate_price(self, quantity):
        """Common method to calculate total price for the item."""
        return self._price * quantity


# ==========================================
# 2. INHERITANCE & POLYMORPHISM
# ==========================================
class MainCourse(FoodItem):
    """Child class inheriting from FoodItem."""
    def __init__(self, food_id, name, price, is_veg=True):
        super().__init__(food_id, name, "Main Course", price)
        self.is_veg = is_veg

    def display_details(self):
        """Polymorphism: Overriding display_details differently."""
        veg_nonveg = "Veg" if self.is_veg else "Non-Veg"
        return super().display_details() + f" [{veg_nonveg}]"

class Dessert(FoodItem):
    """Child class inheriting from FoodItem."""
    def __init__(self, food_id, name, price, sugar_free=False):
        super().__init__(food_id, name, "Dessert", price)
        self.sugar_free = sugar_free

    def display_details(self):
        """Polymorphism: Overriding display_details differently."""
        sf = "Sugar-Free" if self.sugar_free else "Regular"
        return super().display_details() + f" [{sf}]"

class Beverage(FoodItem):
    """Child class inheriting from FoodItem."""
    def __init__(self, food_id, name, price, size="Medium"):
        super().__init__(food_id, name, "Beverage", price)
        self.size = size

    def display_details(self):
        """Polymorphism: Overriding display_details differently."""
        return super().display_details() + f" [Size: {self.size}]"


# ==========================================
# 3. ABSTRACTION
# ==========================================
class Payment(ABC):
    """Abstract base class for payments."""
    @abstractmethod
    def make_payment(self, amount):
        pass

class UPIPayment(Payment):
    def make_payment(self, amount):
        print(f"Processing UPI Payment of ₹{amount:.2f}...")
        return True

class CardPayment(Payment):
    def make_payment(self, amount):
        print(f"Processing Card Payment of ₹{amount:.2f}...")
        return True

class CashPayment(Payment):
    def make_payment(self, amount):
        print(f"Processing Cash Payment of ₹{amount:.2f}...")
        return True


# ==========================================
# 4. CUSTOMER & ORDER CLASSES (Encapsulation)
# ==========================================
class Customer:
    """Class to manage customer information."""
    def __init__(self, name, phone):
        self.__name = name      # Private attribute
        self.__phone = phone    # Private attribute

    def get_details(self):
        return f"Customer: {self.__name} | Phone: {self.__phone}"

class Order:
    """Class to manage the shopping cart and billing."""
    def __init__(self):
        self.__cart = {}  # Private dictionary to store {food_id: quantity}

    def add_item(self, food_item, quantity):
        if food_item.get_id() in self.__cart:
            self.__cart[food_item.get_id()] += quantity
        else:
            self.__cart[food_item.get_id()] = quantity
        print(f"Success: Added {quantity}x {food_item.get_name()} to the order.")

    def remove_item(self, food_id):
        if food_id in self.__cart:
            del self.__cart[food_id]
            print("Success: Item removed from the order.")
        else:
            print("Error: Item not found in cart.")

    def view_cart(self, menu):
        if not self.__cart:
            print("Your cart is currently empty.")
            return False
        
        print("\n--- Your Order Cart ---")
        for f_id, qty in self.__cart.items():
            item = menu[f_id]
            print(f"{item.get_name()} x {qty} = ₹{item.calculate_price(qty)}")
        return True

    def calculate_total(self, menu):
        total = 0
        for f_id, qty in self.__cart.items():
            total += menu[f_id].calculate_price(qty)
        return total

    def apply_discount(self, total):
        if total >= 1000:
            print("\nWoohoo! 10% Discount Applied!")
            return total * 0.90
        elif total >= 500:
            print("\nGreat! 5% Discount Applied!")
            return total * 0.95
        return total

    def is_empty(self):
        return len(self.__cart) == 0


# ==========================================
# 5. MAIN MENU & APPLICATION FLOW
# ==========================================
def main():
    # Initialize a dictionary to store food menu information
    menu = {
        1: MainCourse(1, "Paneer Butter Masala", 300, True),
        2: MainCourse(2, "Chicken Biryani", 400, False),
        3: Dessert(3, "Chocolate Brownie", 150, False),
        4: Dessert(4, "Sugar-Free Rasgulla", 120, True),
        5: Beverage(5, "Cold Coffee", 100, "Large"),
        6: Beverage(6, "Fresh Lime Soda", 80, "Regular")
    }

    print("=== Welcome to the Online Food Ordering System ===")
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    
    # Create required objects
    customer = Customer(name, phone)
    order = Order()

    while True:
        # Clear menu-driven console interface
        print("\n" + "="*40)
        print("1. Display Food Items")
        print("2. Search Food")
        print("3. Add Food to Cart")
        print("4. View Cart")
        print("5. Remove Food from Cart")
        print("6. Calculate Total")
        print("7. Apply Discount")
        print("8. Make Payment")
        print("9. Display Final Bill")
        print("10. Exit")
        print("="*40)

        # Exception handling for invalid user input
        try:
            choice = int(input("Enter your choice (1-10): "))

            if choice == 1:
                print("\n--- Menu ---")
                for item in menu.values():
                    print(item.display_details())

            elif choice == 2:
                keyword = input("Enter food name to search: ").lower()
                found = False
                print("\n--- Search Results ---")
                for item in menu.values():
                    if keyword in item.get_name().lower():
                        print(item.display_details())
                        found = True
                if not found:
                    print("No items found matching your search.")

            elif choice == 3:
                f_id = int(input("Enter Food ID to add: "))
                if f_id in menu:
                    qty = int(input("Enter quantity: "))
                    if qty > 0:
                        order.add_item(menu[f_id], qty)
                    else:
                        print("Error: Quantity must be greater than 0.")
                else:
                    print("Error: Invalid Food ID.")

            elif choice == 4:
                order.view_cart(menu)

            elif choice == 5:
                f_id = int(input("Enter Food ID to remove: "))
                order.remove_item(f_id)

            elif choice == 6:
                total = order.calculate_total(menu)
                print(f"Total Order Amount: ₹{total:.2f}")

            elif choice == 7:
                total = order.calculate_total(menu)
                discounted = order.apply_discount(total)
                print(f"Amount after applicable discount: ₹{discounted:.2f}")

            elif choice == 8:
                if order.is_empty():
                    print("Your cart is empty! Please add items before proceeding to payment.")
                    continue

                total = order.calculate_total(menu)
                final_amount = order.apply_discount(total)
                
                print(f"\nAmount to pay: ₹{final_amount:.2f}")
                print("Payment Methods: [1] UPI  [2] Card  [3] Cash")
                pay_choice = int(input("Select payment method (1/2/3): "))

                payment_gateway = None
                if pay_choice == 1:
                    payment_gateway = UPIPayment()
                elif pay_choice == 2:
                    payment_gateway = CardPayment()
                elif pay_choice == 3:
                    payment_gateway = CashPayment()
                else:
                    print("Error: Invalid payment method selected.")

                if payment_gateway:
                    payment_gateway.make_payment(final_amount)
                    print("Payment Successful!")

            elif choice == 9:
                if order.is_empty():
                    print("Cart is empty. No bill to generate.")
                else:
                    print("\n" + "*"*40)
                    print("               FINAL BILL               ")
                    print("*"*40)
                    print(customer.get_details())
                    print("-" * 40)
                    order.view_cart(menu)
                    print("-" * 40)
                    
                    total = order.calculate_total(menu)
                    final_total = order.apply_discount(total)
                    print(f"Subtotal: ₹{total:.2f}")
                    if total != final_total:
                        print(f"Discount Applied: -₹{total - final_total:.2f}")
                    print(f"Total Paid: ₹{final_total:.2f}")
                    print("*"*40)
                    print("Thank you for your order! Enjoy your food.")
                    
                    # Clear cart after successful billing
                    order = Order()

            elif choice == 10:
                print("Thank you for using the Online Food Ordering System. Goodbye!")
                break

            else:
                print("Invalid choice. Please select a number from 1 to 10.")

        except ValueError:
            print("Invalid input! Please enter numerical values where expected.")

if __name__ == "__main__":
    main()