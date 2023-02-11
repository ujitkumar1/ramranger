import re

import requests
from bs4 import BeautifulSoup

from database import DataBase
from log import log
from scrape import Scrape


class Amazon(Scrape):
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
        phone = soupText.find("span", class_="a-size-medium a-color-base a-text-normal")
        price = soupText.find("span", class_="a-price-whole")
        ramD = 0

        # formatting the phone and price variable and extracting the Ram value
        if phone is not None and price is not None:
            rams = phone.text.split("|")
            for oneRam in rams:
                if "RAM" in oneRam:
                    ramD = oneRam
                    break

            # formatting the Ram value
            if ramD:
                ramD = ramD.split("RAM")
                ramD = ramD[0]
                ramD = ramD[-5:-1]
                ramD = re.sub(r'[^\d]+', '', ramD)

            phone = phone.text
            phone = phone.split("|")[0]
            price = price.text.replace(",", "")
            return phone, price, ramD

    def scrape(self, hostname):
        """
            This function scrapes information about smartphones from the Amazon.in website and stores the information
             in a collection.
            Args:
                self: The instance of the class that the function is being called on.This argument provides access to
                      the attributes and methods of the class.
                hostname: The Database host name
            Returns:

        """
        self.phoneinfo = []
        self.item = DataBase(hostname).getIndex()
        while self.soup.find('span', class_='s-pagination-item s-pagination-selected'):
            log.info("Scrapping amazon.in website, page no. :" + str(self.page))
            url = self.url2 + str(self.page)
            req = requests.get(url, headers=self.headers)
            self.soup = BeautifulSoup(req.content, 'html.parser')
            box = self.soup.find_all("div", class_=["sg-row", "s-card-border"])
            for onePhone in box:
                data = self.formatData(onePhone)
                if data and (data not in self.listPhone):
                    self.item += 1
                    info = {
                        "_id": self.item,
                        "name": data[0],
                        "price": float(data[1]),
                        "ram": int(data[2])
                    }
                    self.phoneinfo.append(info)
            self.page += 1
        log.info("Scrapping Completed for amazon.in")
