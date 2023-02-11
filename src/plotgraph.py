import matplotlib.pyplot as plt


class PlotGrpah:
    @staticmethod
    def barplot(xCor, yCor):
        """
            This function plots a bar graph of RAM versus price, using the data stored in the `ram` and `price`
            attributes.
            Args:
                xCor: list of x-coordinates
                yCor: list of y-coordinates
            Return:

        """
        plt.bar(xCor, yCor, color="lightgreen")
        plt.title("Bar Graph(RAM vs Price)")
        plt.xlabel("RAM(GB)")
        plt.ylabel("PRICE(Rs.)")
        plt.grid()
        plt.show()
