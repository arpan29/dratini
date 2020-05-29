import logging

from mew.client.google_calendar import GoogleCalendarClient


class MyService():

    def test_function(self, request):
        # Test Function.
        # Access the models and write most of the business logic here.
        # All the clients or external API calls can be done here.
        logging.info("Hello")
        logging.info("Hiiiiiiiiiiiiiiii")
        return {"status": "SUCCESS"}
