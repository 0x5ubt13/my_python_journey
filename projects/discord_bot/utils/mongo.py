import logging
import collections

"""
This is a utility file for using Mongo DB. The class "Document" aims to make using mongo calls easy, saving the need
to know the syntax for it. Just pass in the db instance on init and the doc to create an instance on and db goes brrrr
"""


class Document():
    def __init__(self, connection, document_name):
        """
        Parameters:
            - connection (Mongo connection) : Our database connection
            - document_name (str) : the document this instance should be
        """
        self.db = connection[document_name]
        self.logger = logging.getLogger(__name__)

    # <-- Pointer Methods -->
    async def update(self, dict):
        """ For simpler calls, points to self.update_by_id """
        await self.update_by_id(dict)

    async def get_by_id(self, id):
        """ This is essentially find_by_id so point to that """
        return await self.find_by_id

    async def find(self, id):
        """ For simpler calls, points to self.delete_by_id """
        await self.delete_by_id(id)

    # <-- Actual Methods -->
    async def find_by_id(self, id):
        """
        Returns the data found under `id`
        Params:
            - id () : The id to search for

        Returns:
            - None if nothing is found
            - If something's found, return that
        """
        return await self.db.find_one({"_id": id})

    async def delete_by_id(self, id):
        """
        Deletes all items found with _id: `id`

        Params:
            - id () : The id to search for and send to oblivion
        """
        # Raise if the _id does not exist in database
        if not await self.find_by_id(id):
            pass

        await self.db.delete_many({"_id": id})

    async def insert(self, dict):
        """
        Insert something in the db

        Params:
            - dict : the dict to insert
        """
        # Check if it's actually a dict
        if not isinstance(dict, collections.abc.Mapping):
            raise TypeError("Expected Dictionary.")

    async def upsert(self, data, option="set", *args, **kwargs):
        """
        Makes a new item in the document. If it already exists, it will update that item instead. This function
        parses an input dict to get the relevant information needed to insert. It supports inserting when the document
        already exists.

        Params:
            - data (dict) : the dict to insert
        """
        await self.update_by_id(data, option, upsert=True, *args, **kwargs)

    async def update_by_id(self, data, option="set", *args, **kwargs):
        """
        For when a document already exists in the data and you want to update something in it;
        This function parses an input Dict to get the relevant information needed to update.

        Params:
         - data (Dict) : The data to insert
        """

        upsert = kwargs.get("upsert", False)

        # Check if its actually a Dictionary
        if not isinstance(data, collections.abc.Mapping):
            raise TypeError("Expected Dictionary.")

        # Always use your own _id
        if not data.get("_id"):
            raise KeyError("_id not found in supplied dict.")

        # Raise if the _id does not exist in database
        try:
            await self.find_by_id(data["_id"])
        except IdNotFound as e:
            if not upsert:
                raise e

        _id = data["_id"]
        data.pop("_id")
        await self.db.update_one({"_id": _id}, {f"${option}": data}, *args, **kwargs)

    async def unset(self, data):
        """
        For when you want to remove a field from
        a pre-existing document in the collection
        This function parses an input Dictionary to get
        the relevant information needed to unset.

        Params:
         - data (Dictionary) : Dictionary to parse for info
        """
        # Check if its actually a Dictionary
        if not isinstance(data, collections.abc.Mapping):
            raise TypeError("Expected Dictionary.")

        # Always use your own _id
        if not data.get("_id"):
            raise KeyError("_id not found in supplied dict.")

        # Raise if the _id does not exist in database
        await self.find_by_id(data["_id"])

        _id = data["_id"]
        data.pop("_id")
        await self.db.update_one({"_id": _id}, {"$unset": data})

    async def increment(self, _id, amount, field):
        """
        Increment a given `field` by `amount`

        Params:
        - _id () : The id to search for
        - amount (int) : Amount to increment by
        - field () : field to increment
        """
        # Raise if the _id does not exist in database
        await self.find_by_id(_id)

        self.db.update_one({"_id": _id}, {"$inc": {field: amount}})

    # <-- Private methods -->
    async def __get_raw(self, _id):
        """
        An internal private method used to eval certain checks
        within other methods which require the actual data
        """
        return await self.db.find_one({"_id": _id})
