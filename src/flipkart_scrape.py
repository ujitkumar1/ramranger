import requests
from bs4 import BeautifulSoup

from database import DataBase
from log import log
from scrape import Scrape


class Flipkart(Scrape):
    def formatData(self, soupText):
        """
            This function extracts specific information from the `soupText` object and returns it in a formatted manner.
            Args:
                soupText (bs4.BeautifulSoup): An object of the BeautifulSoup class.
            Returns:
                tuple: A tuple containing the following information in the following order:
                    - phone (str): The phone name, extracted from the `soupText` object.
                    - price (str): The price of the phone, extracted from the `soupText` object.
                    - ramD (str): The amount of RAM in the phone, extracted from the `soupText` object.

        """
        phone = soupText.find("div", class_="_4rR01T")

        price = soupText.find("div", class_="_30jeq3 _1_WHN1")

        ram = soupText.find_all("li", class_="rgWa7D")
        ramD = 0

        # formatting the phone and price variable and extracting the Ram value
        if price is not None:
            price = price.text
            price = price.replace(",", "")
            price = price.replace("₹", "")

        if price is None:
            price = 0

        if phone is not None:
            phone = phone.text

        # formatting the Ram value
        for oneRam in ram:
            if "RAM" in oneRam.text:
                ramList = oneRam.text.split("|")
                for one in ramList:
                    if "RAM" in one:
                        ramD = one
                        ramD = ramD.replace("GB", "")
                        ramD = ramD.replace("RAM", "")
                        ramD = ramD.replace(" ", "")
                        ramD = ramD.replace("MB", "")
        return phone, price, ramD

    def scrape(self, hostname):
        """
            This function scrapes information about smartphones from the Amazon.in website and stores the information
            in a collection.
            Args:
                self: The instance of the class that the function is being called on.This argument provides access to
                      the attributes and methods of the class,
                hostname: The Database host name
            Returns:

        """
        self.item = DataBase(hostname).getIndex()
        while self.soup.find('a', class_='_1LKTO3'):
            log.info("Scrapping flipkart.com website, page no. :" + str(self.page))
            url = self.url2 + str(self.page)
            req = requests.get(url, headers=self.headers)
            self.soup = BeautifulSoup(req.content, 'html.parser')
            box = self.soup.find_all("div", class_="_2kHMtA")
            for onePhone in box:
                data = self.formatData(onePhone)
                if data not in self.listPhone:
                    self.item += 1
                    self.listPhone.append(data)
                    info = {
                        "_id": self.item,
                        "name": data[0],
                        "price": float(data[1]),
                        "ram": int(data[2])
                    }
                    self.phoneinfo.append(info)
            self.page += 1
        log.info("Scrapping Completed for flipkart.com")
