from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionWelcomeMessage(Action):
    def name(self) -> Text:
        return "action_welcome_message"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        welcome_message = "Welcome to Holidayz Inn! How can I assist you with your room booking today?"
        dispatcher.utter_message(text=welcome_message)
        return []


class ActionProcessBooking(Action):
    def name(self) -> Text:
        return "action_process_booking"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("ActionProcessBooking triggered")
        name = tracker.get_slot("name")
        guest_count = tracker.get_slot("guest_count")
        check_in = tracker.get_slot("check_in")
        check_out = tracker.get_slot("check_out")
        breakfast = tracker.get_slot("breakfast")
        payment_method = tracker.get_slot("payment_method")

        # Here we would typically interact with our booking system
        # For this example, we'll just print the information
        print(f"Processing booking for {name}, {guest_count} guests, "
              f"from {check_in} and {check_out} "
              f"breakfast: {'included' if breakfast else 'not included'}, paying by {payment_method}")

        # Simulate booking confirmation
        dispatcher.utter_message(text=f"Booking processed for {name} from {check_in} to {check_out}.")
        dispatcher.utter_message(text="Your room has been booked. Confirmation sent to your email.")

        return []


class ActionAskBreakfast(Action):
    def name(self) -> Text:
        return "action_ask_breakfast"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Do you need breakfast included?")
        return []

class ActionAskPaymentMethod(Action):
    def name(self) -> Text:
        return "action_ask_payment_method"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="What's your preferred payment method?")
        return []
