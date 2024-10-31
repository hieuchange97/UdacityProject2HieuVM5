import json
import logging
import datetime
import azure.functions as func


def main(event: func.EventGridEvent):
    logging.info('Python EventGrid trigger processed an event at %s for topic: %s', str(datetime.datetime.now()), event.topic)
