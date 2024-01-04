from pymongo import MongoClient

class FormulaOneDatabase:
    """
    Wrapper class for connecting to the Formula One MongoDB database using pymongo.

    Attributes:
    - client (MongoClient): The MongoDB client.
    - db (Database): The Formula One MongoDB database.
    """

    def __init__(self, uri: str = 'mongodb://localhost:27017/', db_name: str = 'formulaone'):
        """
        Initialize a connection to the Formula One MongoDB database.

        Parameters:
        - uri (str): The MongoDB connection URI.
        - db_name (str): The name of the Formula One MongoDB database.
        """
        self.client = MongoClient(uri)
        self.db = self.client[db_name]