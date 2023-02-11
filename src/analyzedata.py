import math

from database import DataBase


class AnalyzeData:
    ram = []
    price = []
    maxRam = -99
    lowestPrice = math.inf

    def getMaxRam(self):
        """
            Getter for maxRam variable
            Args:

            Returns:
                The value of maxRam variable.
        """
        return AnalyzeData.maxRam

    def setMaxRam(self, value):
        """
            Setter for maxRam to the given `value`.
            Args:
                value: int variable
            Returns:

        """
        AnalyzeData.maxRam = value

    def getLowestPrice(self):
        """
            Getter for LowestPrice variable
            Args:

            Returns:
                The value of LowestPrice variable.
        """
        return AnalyzeData.lowestPrice

    def setLowestPrice(self, value):
        """
            Setter for LowestPrice to the given `value`.
            Args:
                value: int variable
            Returns:

        """
        AnalyzeData.lowestPrice = value

    @classmethod
    def analyzData(cls, hostname, data):
        """
            This function analyzes the data by calculating the ram and price values and storing them in the `ram` and
            `price` attributes, respectively.It also finds the maximum value of ram and the lowest price among the
            products with the maximum ram value.
            Args:
                self: The instance of the class that the function is being called on.This argument provides access to
                the attributes and methods of the class.
            Return:
                ram: list of ram sizes of phones
                price : list of price of phones
        """

        for onePhone in data:
            cls.ram.append(onePhone["ram"])
            cls.price.append(onePhone["price"])
            if onePhone["ram"] > AnalyzeData().getMaxRam():
                AnalyzeData().setMaxRam(onePhone["ram"])
        myquery = {"ram": AnalyzeData().getMaxRam()}

        datas = DataBase(hostname=hostname).collection.find(myquery)

        for onePhone in datas:
            if onePhone["price"] < AnalyzeData().getLowestPrice():
                AnalyzeData().setLowestPrice(onePhone["price"])

        return cls.ram, cls.price
