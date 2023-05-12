class Product:

    def __init__(self, productName:str, productID:int):
        self.productName = productName
        self.productID = productID

    def setProductName(self, productName:str):
        self.productName = productName

    def getProductName(self):
        return productName

    def setProductID(self, productID:int):
        self.productID = productID

    def getProductID(self):
        return productID


class Vendor(Product):

    def __init__(self, vendorName:str, vendorID:int):
        self.vendorName = vendorName
        self.vendorID = vendorID

    def setVendorName(self, vendorName:str):
        self.vendorName = vendorName

    def getVendorName(self):
        return vendorName

    def setVendorID(self, vendorID):
        self.vendorID = vendorID

    def getVendorID(self):
        return vendorID

class Price(Vendor):

    def __init__(self, product:int, vendor:int, price:int):
        self.product = product
        self.vendor = vendor
        self.price = price

    def setProduct(self, product:int):
        self.product = product

    def getProduct(self):
        return product

    def setVendor(self, vendor):
        self.vendor = vendor

    def getVendor(self):
        return vendor

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return price


class crudProduct(Product):

    product_table = []

    def __init__(self):
        pass

    def add_product(self):
        prodID = int(input("Enter ProductID: "))
        prodName = input("Enter Your ProductName: ")
        self.product_table.append(Product(prodName, prodID))

    def get_product(self):
        prodID = int(input("Enter ProductID: "))
        prodName = input("Enter Your ProductName: ")
        for product in self.product_table:
            if product.getProductID == prodID:
                print(product.getProductID(), product.getProductName())

    def delete_product(self):
        prodID = int(input("Enter ProductID: "))
        prodName = input("Enter Your ProductName: ")
        for product in self.product_table:
            if product.getProductID == prodID:
                self.product_table.remove(product)

    def edit_product(self):
        prodID = int(input("Enter ProductID: "))
        for product in self.product_table:
            if product.getProductID == prodID:
                prodID = int(input("Enter Update ProductID: "))
                prodName = input("Enter Update ProductName: ")
                self.product_table[self.product_table.index(product)] = Product(prodName, prodID)

    def controller(self):
        while True:
            print("**********************************")
            print(" Welcome Product Inventry System  ")
            print("==================================")
            print("          Product Data            ")
            print("**********************************")
            print("    1. Press A for Add Product    ")
            print("    2. Press B for Get Product    ")
            print("    3. Press C for Del Product    ")
            print("    4. Press D for Edit Product   ")
            print("    5. Press Q for Exit           ")
            print("**********************************")
            choice = input("Enter Your Choice: ")
            match choice:
                case "A":
                    self.add_product()
                case "B":
                    self.get_product()
                case "C":
                    self.delete_product()
                case "D":
                    self.edit_product()
                case "Q":
                    break





crudProductInterface = crudProduct()
crudProductInterface.controller()
        
