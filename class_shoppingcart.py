

class ShoppingCart():
    def __init__(self, cart = []):    
        self.cart = cart 
       
    def add_to_cart(self):
        added_item = input('What would you like to add?\n')
        self.cart.append(added_item) 
        print(f'{added_item} are added to your cart')

    def run(self):
        while True:
            selection = input('What would you like to do? Use \'+\' to add, \'-\' to delete, \'p\' to print current cart and \'q\' to quit.\n').lower()
            if selection != 'q':
                if selection == '+':
                    self.add_to_cart()
                elif selection == '-':
                    self.remove_from_cart()
                elif selection =='p':
                    self.print_current_cart()
            else:
                print('Thank you for shopping with us. Your final cart is below.')
                self.print_current_cart()
                break

    def remove_from_cart(self):
        removed_items = input('What would you like to remove?\n')
        if removed_items in self.cart:
            print(f'{removed_items} was removed from the cart')
            self.cart.remove(removed_items)
        else:
            print('Item is not in your cart')

    def print_current_cart(self):
        print(f'Current items in your shopping cart ')
        for current_items in self.cart:
            print(current_items)

my_program_example = ShoppingCart().run() 
