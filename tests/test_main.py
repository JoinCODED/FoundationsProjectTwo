from io import StringIO
import sys
import unittest
from mock import patch
from components import Store, Product, Cart

class TestStoreMethods(unittest.TestCase):

    def test_init(self):
        # test fail messages
        products_msg = "\n\nThe __init__() method of the Store class must initialize the store with an empty list of products."
        name_msg = "\n\nThe __init__() method of the Store class must initialize the store with the name it receives as an argument."
        
        # initializing test data
        test_store_name = "test"
        store = Store(test_store_name)
        
        # performing test
        self.assertEqual(store.name, test_store_name, msg=name_msg)
        self.assertEqual(store.products, [], msg=products_msg)
    
    def test_add_product(self):
        # test fail messages
        init_msg = "\n\nThe __init__() method of the Store class must initialize the store with an empty list of products."
        append_msg = "\n\nThe add_product() method of the Store class must append the product it receives as an argument to the store's list of products."
        append_not_replace_msg = "\n\nThe add_product() method of the Store class must not remove existing products, instead it should add the new product to the list of existing products."
        append_at_end_msg = "\n\nThe add_product() method of the Store class should append the new product it receives as an argument to the end of the existing list of products."

        # initializing test data
        test_store_name = "test"
        name1 = "Test Product 1"
        description1 = "Test Description 1"
        price1 = 3

        name2 = "Test Product 2"
        description2 = "Test Description 2"
        price2 = 5

        prod1 = Product(name1, description1, price1)
        prod2 = Product(name2, description2, price2)

        store = Store(test_store_name)

        # performing test
        self.assertEqual(store.products, [], msg=init_msg)

        store.add_product(prod1)
        self.assertEqual(len(store.products), 1, msg=append_msg)
        self.assertEqual(store.products[0], prod1, msg=append_msg)

        store.add_product(prod2)
        self.assertEqual(len(store.products), 2, msg=append_not_replace_msg)
        self.assertEqual(store.products[1], prod2, msg=append_at_end_msg)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_products(self, mock_stdout):
        # test fail messages
        name_msg = "\n\nThe print_products() method in the Store class should print the names of all the store's products."
        description_msg = "\n\nThe print_products() method in the Store class should print the descriptions of all the store's products."
        price_msg = "\n\nThe print_products() method in the Store class should print the prices of all the store's products."

        # initializing test data
        test_store_name = "test"
        name1 = "Test Product 1"
        description1 = "Test Description 1"
        price1 = 3

        name2 = "Test Product 2"
        description2 = "Test Description 2"
        price2 = 5

        prod1 = Product(name1, description1, price1)
        prod2 = Product(name2, description2, price2)

        store = Store(test_store_name)
        store.add_product(prod1)
        store.add_product(prod2)

        # executing function and capturing output
        store.print_products()
        output = mock_stdout.getvalue()

        # performing test
        for prod in store.products:
            self.assertIn(prod.name, output, msg=name_msg)
            self.assertIn(prod.description, output, msg=description_msg)
            self.assertIn(str(prod.price), output, msg=price_msg)

class TestProductMethods(unittest.TestCase):

    def test_init(self):
        # fail test messages
        name_msg = "\n\nThe __init__() method of the Product class must initialize the product with the name it receives as an argument."
        description_msg = "\n\nThe __init__() method of the Product class must initialize the product with the description it receives as an argument."
        price_msg = "\n\nThe __init__() method of the Product class must initialize the product with the price it receives as an argument."

        # initializing test data
        name = "Test"
        description = "This is a testing product"
        price = 5.5

        # performing test
        product = Product(name, description, price)
        self.assertEqual(product.name, name, msg=name_msg)
        self.assertEqual(product.description, description, msg=description_msg)
        self.assertEqual(product.price, price, msg=price_msg)
    
    def test_str(self):
        # fail test messages
        name_msg = "\n\nThe __str__() method of the Product class must return the name of the product."
        description_msg = "\n\nThe __str__() method of the Product class must return the description of the product."
        price_msg = "\n\nThe __str__() method of the Product class must return the price of the product."

        # initializing test data
        name = "Test"
        description = "This is a testing product"
        price = 5.5
        product = Product(name, description, price)

        # performing test
        output = "%s" % product
        self.assertIn(product.name, output, msg=name_msg)
        self.assertIn(product.description, output, msg=description_msg)
        self.assertIn(str(product.price), output, msg=price_msg)
    
class TestCartMethods(unittest.TestCase):

    def test_init(self):
        # fail test messages
        fail_msg = "\n\nThe __init__() method of the Cart class must initialize a cart with an empty list of products."

        # initializing test data
        cart = Cart()

        # performing test
        self.assertEqual(cart.products, [], msg=fail_msg)

    def test_add_to_cart(self):
        # fail test messages
        add_msg = "\n\nThe add_to_cart() method of the Cart class must add the product it receives as an argument to the cart's list of products."
        append_not_replace_msg = "\n\nThe add_to_cart() method of the Cart class must not remove existing products, instead it should add the new product to the list of existing products."
        append_at_end_msg = "\n\nThe add_to_cart() method of the Cart class should append the new product it receives as an argument to the end of the existing list of products."

        # initializing test data
        name1 = "Test Product 1"
        description1 = "Test Description 1"
        price1 = 3

        name2 = "Test Product 2"
        description2 = "Test Description 2"
        price2 = 5

        prod1 = Product(name1, description1, price1)
        prod2 = Product(name2, description2, price2)

        cart = Cart()

        # performing test
        cart.add_to_cart(prod1)
        self.assertEqual(len(cart.products), 1, msg=add_msg)
        self.assertEqual(cart.products[0], prod1, msg=add_msg)

        cart.add_to_cart(prod2)
        self.assertEqual(len(cart.products), 2, msg=append_not_replace_msg)
        self.assertEqual(cart.products[1], prod2, msg=append_at_end_msg)

    def test_get_total_price(self):
        # fail test messages
        price_fail_msg = "\n\nThe get_total_price() method of the Cart class must return the total price of the products in the cart."

        # initializing test data
        name1 = "Test Product 1"
        description1 = "Test Description 1"
        price1 = 3

        name2 = "Test Product 2"
        description2 = "Test Description 2"
        price2 = 5

        name3 = "Test Product 3"
        description3 = "Test Description 3"
        price3 = 15.3

        actual_price = price1 + price2 + price3

        prod1 = Product(name1, description1, price1)
        prod2 = Product(name2, description2, price2)
        prod3 = Product(name3, description3, price3)

        cart = Cart()
        cart.add_to_cart(prod1)
        cart.add_to_cart(prod2)
        cart.add_to_cart(prod3)

        # performing test
        total_price = cart.get_total_price()
        self.assertEqual(total_price, actual_price, msg=price_fail_msg)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_receipt(self, mock_stdout):
        # fail test messages
        name_msg = "\n\nThe print_receipt() method in the Cart class must print the names of all the products in the cart."
        description_msg = "\n\nThe print_receipt() method in the Cart class must print the descriptions of all the products in the cart."
        price_msg = "\n\nThe print_receipt() method in the Cart class must print the prices of all the products in the cart."
        total_price_msg = "\n\nThe print_receipt() method in the Cart class must print the total price of the products in the cart."

        # initializing test data
        name1 = "Test Product 1"
        description1 = "Test Description 1"
        price1 = 3

        name2 = "Test Product 2"
        description2 = "Test Description 2"
        price2 = 5

        name3 = "Test Product 3"
        description3 = "Test Description 3"
        price3 = 15.3

        total_price = price1 + price2 + price3

        prod1 = Product(name1, description1, price1)
        prod2 = Product(name2, description2, price2)
        prod3 = Product(name3, description3, price3)

        cart = Cart()
        cart.add_to_cart(prod1)
        cart.add_to_cart(prod2)
        cart.add_to_cart(prod3)

        # executing function and capturing output
        cart.print_receipt()
        output = mock_stdout.getvalue()

        # performing test
        for product in cart.products:
            self.assertIn(product.name, output, msg=name_msg)
            self.assertIn(product.description, output, msg=description_msg)
            self.assertIn(str(product.price), output, msg=price_msg)
        
        self.assertIn(str(total_price), output, msg=total_price_msg)

    @patch('sys.stdout', new_callable=StringIO)
    def test_checkout(self, mock_stdout):
        # fail test messages
        print_receipt_msg = "\n\nThe checkout() method in the Cart class must call the print_receipt() method to print the receipt to the user, whether they confirm to checkout or not."
        different_output_msg = "\n\nThe checkout() method in the Cart class must display a different message when the user confirms the checkout and when the user doesn't confirm the checkout (types yes or no)."
        
        # initializing test data
        user_input = ['yes']
        name1 = "Test Product 1"
        description1 = "Test Description 1"
        price1 = 3

        name2 = "Test Product 2"
        description2 = "Test Description 2"
        price2 = 5

        name3 = "Test Product 3"
        description3 = "Test Description 3"
        price3 = 15.3

        total_price = price1 + price2 + price3

        prod1 = Product(name1, description1, price1)
        prod2 = Product(name2, description2, price2)
        prod3 = Product(name3, description3, price3)

        cart = Cart()
        cart.add_to_cart(prod1)
        cart.add_to_cart(prod2)
        cart.add_to_cart(prod3)

        # executing function and capturing output
        with patch('builtins.input', side_effect=user_input):
            cart.checkout()

        output_yes = mock_stdout.getvalue()

        user_input = ['no']
        # executing function and capturing output
        with patch('builtins.input', side_effect=user_input):
            cart.checkout()

        output_no = mock_stdout.getvalue()

        # performing test
        for product in cart.products:
            self.assertIn(product.name, output_yes, msg=print_receipt_msg)
            self.assertIn(product.description, output_yes, msg=print_receipt_msg)
            self.assertIn(str(product.price), output_yes, msg=print_receipt_msg)
            self.assertIn(product.name, output_no, msg=print_receipt_msg)
            self.assertIn(product.description, output_no, msg=print_receipt_msg)
            self.assertIn(str(product.price), output_no, msg=print_receipt_msg)
        
        self.assertIn(str(total_price), output_yes, msg=print_receipt_msg)
        self.assertIn(str(total_price), output_no, msg=print_receipt_msg)

        self.assertNotEqual(output_yes, output_no, msg=different_output_msg)
