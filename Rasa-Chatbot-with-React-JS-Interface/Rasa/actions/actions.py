from typing import Any, Text, Dict, List

from rasa_sdk import Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase


class ActionInquirePrescription(ActionQueryKnowledgeBase):

    def __init__(self):
        super().__init__(ActionQueryKnowledgeBase)

    def name(self) -> Text:
        return "action_inquire_organize_blood_donation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        person_nic = next(
            tracker.get_latest_entity_values("blood"), None)

        blood = str(person_nic).lower().replace(" ", "")

        if blood is not None:
            SlotSet("blood", blood)

            # with open('application.yaml') as f:
            #     application_yml = yaml.safe_load(f)
            #
            # prescription_url = application_yml['api']['prescription']['url']
            # print(prescription_url + person_nic)
            # response = requests.get(prescription_url + person_nic).text
            #
            # print(response)
            # dispatcher.utter_message(text=str(response))
            dispatcher.utter_message(text=str("I can organize blood donation camp"))
        else:
            dispatcher.utter_message(text=str("please send the valid nic"))

        return []
