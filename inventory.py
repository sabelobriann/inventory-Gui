import tkinter as tk
from tkinter import messagebox

class Inventory:
    def __init__(self):
        self.items = {}
 
    def add_item(self, item_name, quantity, price_per_unit):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'quantity': quantity, 'price_per_unit': price_per_unit}
        return f"Added {quantity} units of {item_name} at R {price_per_unit:.2f} each."
  
    def update_stock(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
            if self.items[item_name]['quantity'] < 0:
                self.items[item_name]['quantity'] = 0
            return f"Updated {item_name} stock by {quantity} units."
        else:
            return f"Error: {item_name} not found in inventory."
        
    def view_inventory(self):
        inventory_list = "Current Inventory:\n"
        for item_name, details in self.items.items():
            inventory_list += f"{item_name}: {details['quantity']} units available at R{details['price_per_unit']:.2f} each\n"
        return inventory_list

    def check_stock(self, item_name):
        if item_name in self.items:
            quantity = self.items[item_name]['quantity']
            return f"{item_name} has {quantity} units in stock."
        else:
            return f"Error: {item_name} not found in inventory."

class InventoryGUI:
    def __init__(self, root):
        self.inventory = Inventory()
        self.root = root
        self.root.title("Inventory Management System")
        
        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Add Item Section
        tk.Label(self.root, text="Add Item",fg="darkblue").grid(row=0, column=0, columnspan=2)
        tk.Label(self.root, text="Item Name",bg="orange",fg="darkblue").grid(row=1, column=0)
        tk.Label(self.root, text="Quantity",bg="orange",fg="darkblue").grid(row=3, column=0)
        tk.Label(self.root, text="Price per Unit",bg="orange",fg="darkblue").grid(row=5, column=0)
        
        self.add_item_name = tk.Entry(self.root)
        self.add_item_quantity = tk.Entry(self.root)
        self.add_item_price = tk.Entry(self.root)
        
        self.add_item_name.grid(row=1, column=1)
        self.add_item_quantity.grid(row=3, column=1)
        self.add_item_price.grid(row=5, column=1)
        
        tk.Button(self.root, text="Add Item",bg="purple",border=15, command=self.add_item).grid(row=6, column=0, columnspan=2)

        # Update Stock Section
        tk.Label(self.root, text="Update Stock",fg="darkblue").grid(row=7, column=0, columnspan=2)
        tk.Label(self.root, text="Item Name",bg="green").grid(row=9, column=0)
        tk.Label(self.root, text="Quantity Change",bg="green").grid(row=11, column=0)
        
        self.update_item_name = tk.Entry(self.root)
        self.update_quantity = tk.Entry(self.root)
        
        self.update_item_name.grid(row=9, column=1)
        self.update_quantity.grid(row=11, column=1)
        
        tk.Button(self.root, text="Update Stock",bg="olive",border=15, command=self.update_stock).grid(row=12, column=0, columnspan=2)
        
        # View Inventory Section
        tk.Label(self.root, text="View Inventory",fg="darkblue").grid(row=13, column=0, columnspan=2)
        tk.Button(self.root, text="View Inventory",bg="tan",border=15, command=self.view_inventory).grid(row=14, column=0, columnspan=2)
        
        # Check Stock Section
        tk.Label(self.root, text="Check Stock",fg="darkblue").grid(row=15, column=0, columnspan=2)
        tk.Label(self.root, text="Item Name",bg="red").grid(row=16, column=0)
        
        self.check_item_name = tk.Entry(self.root)
        self.check_item_name.grid(row=16, column=1)
        
        tk.Button(self.root, text="Check Stock",bg="aqua",border=15, command=self.check_stock).grid(row=17, column=0, columnspan=2)
        
        # Text area for output
        self.output_text = tk.Text(self.root, height=10, width=50)
        self.output_text.grid(row=20, column=0, columnspan=2)

    def add_item(self):
        item_name = self.add_item_name.get()
        quantity = int(self.add_item_quantity.get())
        price_per_unit = float(self.add_item_price.get())
        message = self.inventory.add_item(item_name, quantity, price_per_unit)
        self.show_message(message)

    def update_stock(self):
        item_name = self.update_item_name.get()
        quantity = int(self.update_quantity.get())
        message = self.inventory.update_stock(item_name, quantity)
        self.show_message(message)

    def view_inventory(self):
        message = self.inventory.view_inventory()
        self.show_message(message)

    def check_stock(self):
        item_name = self.check_item_name.get()
        message = self.inventory.check_stock(item_name)
        self.show_message(message)

    def show_message(self, message):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, message + "\n")
                           

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryGUI(root)
    root.mainloop()
