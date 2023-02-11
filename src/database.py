import pymongo


class DataBase:
    def __init__(self, hostname):
        """
            Initialize the MongoDB connection and set the collection to use.
            Args:
                hostname (str): The hostname or URL of the MongoDB instance to connect to.
            Return:

        """
        client = pymongo.MongoClient(hostname)
        db = client["ramranger"]
        self.collection = db["phoneDB"]

    def read(self):
        """
            reads data from the MongoDB database.
            Args:

            Return:
            A cursor object that can be used to iterate through the documents in the collection.
            Each document is represented as a dictionary.
        """
        return self.collection.find()

    def write(self, data):
        """
            writes data to MongoDB database.
            Args:
                data: List of dictionaries representing the data to be written.
            Return:

        """
        self.collection.insert_many(data)

    def getIndex(self):
        """
            Gets the count of documents in the collection
            Args:

            Returns:
                The count of documents in the collection.
            """
        return self.collection.count_documents({})
