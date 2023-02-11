from abc import ABC, abstractmethod

import requests
from bs4 import BeautifulSoup


class Scrape(ABC):
    def __init__(self, url, url2):
        """
            This is the constructor for the `Amazon` class. It sets up the headers for the HTTP request, the URL to
            scrape, and initializes the BeautifulSoup object for parsing the HTML content. It also sets the page number
            and list of scraped smartphones to 0 and an empty list respectively.
            Args:
                self: The instance of the class that the function is being called on.This argument provides access to
                the attributes and methods of the class,
            Returns:

        """
        self.phoneinfo = None
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 '
                          'Safari/537.36'}
        req = requests.get(url, headers=self.headers)
        self.soup = BeautifulSoup(req.content, 'html.parser')
        self.page = 1
        self.listPhone = []
        self.phoneinfo = []
        self.url2 = url2

    def getData(self):
        """
            This function returns the information about smartphones scraped from the Amazon.in website.
            Args:
                self: The instance of the class that the function is being called on.This argument provides access to
                the attributes and methods of the class,
            Returns:
                list: A list of dictionaries containing the information about smartphones. Each dictionary contains the
                        following keys:
                        _id (int): An identifier for the smartphone.
                        name (str): The name of the smartphone.
                        price (float): The price of the smartphone.
                        ram (int): The amount of RAM in the smartphone.
        """
        return self.phoneinfo

    @abstractmethod
    def formatData(self, data):
        """
            Format the data
            This is an abstract method and must be implemented by subclasses.
            Args:
                data: The data to be formatted, specific to the implementation of the method in the subclass.
            Returns:
                The formatted data, specific to the implementation of the method in the subclass.
        """
        pass

    @abstractmethod
    def scrape(self, hostname):
        """
            Scrape data from a website or other source.
            This is an abstract method and must be implemented by subclasses.
            Args:
                hostname (str): The hostname the Database.
            Returns:
                The scraped data, specific to the implementation of the method in the subclass.
        """
        pass
