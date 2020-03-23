from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import AllSlotsReset

class ActionsWhether(Action):

    def name(self):
        return 'actions_whether'

    def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        import requests
        api_key = 'e4cbc7391fe166345b50533bed70d9c8'
        loc = tracker.get_slot('location')
        print("location: ============= ", loc)
        params = {'access_key': api_key,'query': loc}
        api_result = requests.get('http://api.weatherstack.com/current', params)
        api_response = api_result.json()
        country = api_response['location']['country']
        city = api_response['location']['name']
        condition = api_response['current']['weather_descriptions']
        current = api_response['current']['temperature']
        humidity = api_response['current']['humidity']

        response = """It is currently {},{} in {} at the moment. The temperature is {} degrees,
                    the humidity is {}% """.format(city, country, condition, current, humidity)
        dispatcher.utter_message(response)
        return [SlotSet('location',loc)]
