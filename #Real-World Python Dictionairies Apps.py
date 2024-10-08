#Real-World Python Dictionairies Apps
#Task 1:Restaurant Menu update

restaurant_menu = {"Starters": {"Soup": 5.99, "Bruschetta": 6.50}, 
                "Main Course": {"Steak": 15.99, "Salmon": 13.99},
                "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}}

restaurant_menu.update({"Beverages": {"Water": 2.99, "Sprite": 3.99}})
#print(restaurant_menu)

restaurant_menu.update({"Main Course": {"Steak": 17.99}})
#print(restaurant_menu)

restaurant_menu.update({"Starters": {"Soup": 5.99}})
print(restaurant_menu)