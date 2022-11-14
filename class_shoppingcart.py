

class Cart():
    def __init__(self,added_items,removed_items,current_items):
        self.shopping = {}
        self.added_items = added_items
        self.removed_items = removed_items
        self.current_items = current_items
   
    def add_to_cart(self):
        added_items = input('What would you like to add?')
        self.shopping = added_items
        print(f'{added_items} are added to your cart')
        

    def remove_from_cart(self):
        removed_items = input('What would you like to remove?')
        if removed_items in self.shopping:
            print(f'{removed_items} was removed from the cart')
            del self.shopping
        else:
            print('Item is not in your cart')

    def print_current_cart(self):
        print(f'Current items in your shopping cart ')
        for current_items in self.shopping():
            print(current_items)

items = Cart()

items.add_to_cart()
items.remove_from_cart()
items.print_current_cart()
        
