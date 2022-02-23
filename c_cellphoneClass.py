#The CellPhone Class holds data about a cell phone

class CellPhone:

    # The __init__ method intitialized the attributres --> self = acting only on the instance attribute.
    # First method that is called when you create an object through the init method:
    # Three values from the user.

    def __init__(self, manufact, model, price):
        self.__manufact = manufact
        self.__model = model 
        self.__retail_price = price

    # The set_manufact method accepts an argument for 
    # the phone's manufacturer.

    def set_manufact(self, manufact):
        self.__manufact = manufact

    # The set_model method accepts an argument for 
    # the phone's model number.

    def set_model(self, model):
        self.model = model

    # The set_retail_price method accepts an argument
    # for the phone's retail price.

    def set_retail_price(self, price):
        self.__retail_price = price

    # The get_manufact method returns the 
    # phone's manufacturer.

    def get_manufact(self):
        return self.__manufact

    # The get_model moethod returns the 
    # phone's model number.

    def get_model(self):
        return self.__model

    # The get_retail_price method returns the 
    # phone's retail price.

    def get_retail_price(self):
        return self.__retail_price

