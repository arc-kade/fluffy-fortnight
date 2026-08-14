food_menu = {
    # Main Dishes
    101: {"name": "Margherita pizza", "price": 350},
    102: {"name": "Cheeseburger", "price": 250},
    103: {"name": "Shawarma", "price": 270},
    104: {"name": "Biriyani", "price": 350},
    # Desserts (2xx)
    201: {"name": "Sizzling Brownie", "price": 220},
    202: {"name": "Gulab Jamun (3 pcs)", "price": 120},
    203: {"name": "New York Cheesecake", "price": 260},
    204: {"name": "Tiramisu", "price": 240},
    # Beverages (3xx)
    301: {"name": "Cold Coffee", "price": 150},
    302: {"name": "Fresh Lime Soda", "price": 90},
    303: {"name": "Mango Lassi", "price": 130},
    304: {"name": "Iced Peach Tea", "price": 140},
}
for i in food_menu:
    print(f"ID : {i}   , NAME :{food_menu[i]['name']}")
class FoodItem:
    def __init__(self,fid):
        self.fid=fid
    def menu():
        pass