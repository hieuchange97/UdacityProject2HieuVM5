import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import os


def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = os.environ.get("MyDBConnectionString")   # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['hieuvm5db']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

