

class ShoppingCart():
    def __init__(self, cart = []): 
        # ITEM ONE
        # added_items, removed_items, and current_items are parameters
        # that will require "positional arguments" when you
        # "instantiate" the class. This means you will need to incldue 
        # the added items, removed_items, current_items, etc.

        # One way to address this would be to include default arguments.
        # For example:

#   def __init__(self, added_items = [], removed_items = [], current_items = []): 
        # '[]' is treated as a default argument for added_items, removed_items, and
        # current_items. That way, you are instantiated each object from the Cart() 
        # class with a default argument of empty lists that you can then add items to.

        # ITEM TWO
        # It is important to choose an appropriate data structure for your project.
        # In this case, the project is simple enough that you could justifiably
        # use a simple list, '[]'. You might call it 'Your cart' or something.
        # For example, please see below.

        self.cart = cart 
        # set self.cart equal to the parameter cart from __init__().
   
    def add_to_cart(self):
        # ITEM THREE
        added_item = input('What would you like to add?\n')
        self.cart.append(added_item) # This is one example of how to modify an 
        # existing class attribute.
        print(f'{added_item} are added to your cart')

    # ITEM FOUR
    # The way your program is current written, it does not have a user interface of any kind.
    # You can add a method to run the UI if you would like.

    def run(self):
        while True:
            selection = input('What would you like to do? Use \'+\' to add, \'-\' to delete, \'p\' to print current cart and \'q\' to quit.\n').lower()
            if selection != 'q':
                if selection == '+':
                    self.add_to_cart()
                elif selection == '-':
                    self.remove_from_cart()
            else:
                print('Thank you for shopping with us. Your cart is below.')
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
# This instantiates the Cart() class, calls the run method, 
# and sets the results of the run method equal to a variable.