import time

from amazon_scrape import Amazon
from analyzedata import AnalyzeData
from database import DataBase
from flipkart_scrape import Flipkart
from log import log
from plotgraph import PlotGrpah


def main():
    """
        Main function that performs a series of steps to gather, store, analyze and plot data on smartphones.

        Returns:
            None
    """
    hostname = "mongodb://localhost:27017/"
    db = DataBase(hostname=hostname)

    log.info("Scrapping of flipkart.com")
    flipkart_product_home = "https://www.flipkart.com/search?q=smartphone&otracker=search&otracker1=search&marketplace=" \
                            "FLIPKART&as-show=on&as=off&page=1"
    flipkart_product_page = "https://www.flipkart.com/search?q=smartphone&otracker=search&otracker1=search&marketplace=" \
                            "FLIPKART&as-show=on&as=off&page="
    flipkartscrape = Flipkart(url=flipkart_product_home, url2=flipkart_product_page)
    flipkartscrape.scrape(hostname)
    flipD = flipkartscrape.getData()
    log.info("\nWriting the data of flipkart.com to the Database")
    db.write(flipD)

    time.sleep(2)
    log.info("")

    log.info("Scrapping of amazon.in")
    amazon_product_home = "https://www.amazon.in/s?k=smartphone"
    amazon_product_page = "https://www.amazon.in/s?k=smartphone&page="
    amazonscrape = Amazon(url=amazon_product_home, url2=amazon_product_page)
    amazonscrape.scrape(hostname)
    amazD = amazonscrape.getData()
    log.info("\nWriting the data of amazon.in to the Database")
    db.write(amazD)

    log.info("\nData Transferred completed for flipkart.com and amazon.in to the Database")

    log.info("\nAnalyzing the data")
    data = AnalyzeData().analyzData(hostname, db.read())
    log.info("\nThe Smartphone of highest RAM " + str(AnalyzeData().getMaxRam()) + "GB is priced at " + str(
        AnalyzeData().getLowestPrice()) + "(LowestPrice)")

    log.info("\nPlotting the Graph")
    PlotGrpah.barplot(data[0], data[1])


if __name__ == "__main__":
    main()
