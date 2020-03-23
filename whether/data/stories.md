## story 1
* greet
	- utter_greet

## story 2
* goodbye
	- utter_goodbye

## story 3
* ask_weather
	- utter_ask_location

## story 4
* ask_weather_location
	- actions_whether

## story 5
* ask_temperature
	- actions_whether
## Generated Story 1
* greet
    - utter_greet
* ask_weather_location{"location": "stuttgart"}
    - slot{"location": "stuttgart"}
    - actions_whether
    - slot{"location": "stuttgart"}
    - utter_did_that_help
* goodbye
    - utter_goodbye

## Generated Story 2
* greet
    - utter_greet
* ask_weather
    - utter_ask_location
* ask_weather_location{"location": "berlin"}
    - slot{"location": "berlin"}
    - actions_whether
    - slot{"location": "berlin"}
    - utter_did_that_help
* goodbye
    - utter_goodbye

## Generated Story 3
* greet
    - utter_greet
* ask_temperature{"location": "Oslo"}
    - slot{"location": "Oslo"}
    - actions_whether
    - slot{"location": "Oslo"}
    - utter_did_that_help
* goodbye
    - utter_goodbye

## Generated Story 4
* greet
    - utter_greet
* ask_weather
    - utter_ask_location
* ask_weather_location{"location": "cologne"}
    - slot{"location": "cologne"}
    - actions_whether
    - slot{"location": "cologne"}
    - utter_did_that_help
* goodbye
    - utter_goodbye

## Generated Story 5
* greet
    - utter_greet
* ask_weather
    - utter_ask_location
* ask_weather_location{"location": "Kiel"}
    - slot{"location": "Kiel"}
    - actions_whether
    - slot{"location": "Kiel"}
    - utter_did_that_help
* goodbye
    - utter_goodbye

## Generated Story 6
* greet
    - utter_greet
* ask_weather_location{"location": "Jamaica"}
    - slot{"location": "Jamaica"}
    - actions_whether
    - slot{"location": "Jamaica"}
    - utter_did_that_help
* goodbye
    - utter_goodbye

## Generated Story 7
* greet
    - utter_greet
* ask_weather
    - utter_ask_location
* ask_weather_location{"location": "dhaka"}
    - slot{"location": "dhaka"}
    - actions_whether
    - slot{"location": "dhaka"}
    - utter_did_that_help
* ask_weather_location{"location": "Chittagang"}
    - slot{"location": "Chittagang"}
    - actions_whether
    - slot{"location": "Chittagang"}
    - utter_did_that_help
* goodbye
    - utter_goodbye

## Generated Story 8
* greet
    - utter_greet
* ask_temperature{"location": "Frankfurt"}
    - slot{"location": "Frankfurt"}
    - actions_whether
    - slot{"location": "Frankfurt"}
    - utter_did_that_help
* ask_temperature{"location": "Bonn"}
    - slot{"location": "Bonn"}
    - actions_whether
    - slot{"location": "Bonn"}
    - utter_did_that_help
* goodbye
    - utter_goodbye

## Generated Story 9
* greet
    - utter_greet
* ask_weather
    - utter_ask_location
* ask_weather_location{"location": "hongkong"}
    - slot{"location": "hongkong"}
    - actions_whether
    - utter_did_that_help
