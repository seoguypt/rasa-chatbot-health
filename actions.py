from rasa_sdk.forms import FormAction
from rasa_sdk.events import Form, AllSlotsReset, SlotSet, UserUttered
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Text, Dict, Any, List
import json


class ActionUserName(Action):

    def name(self):
        return 'action_user_name'

    def run(self, dispatcher, tracker, domain):
        name = tracker.get_latest_entity_values('name')
        print(name)
        if name == None or name == "None" or name == "":
            return [SlotSet("name", name)]
        else:
            dispatcher.utter_template("utter_naming_friend", tracker)
            return [SlotSet("name", "my friend")]
        return []


class ActionConfirm(Action):
    """Example of a custom action"""

    def name(self):
        return "action_confirm"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message["intent"].get("name")
        if (intent == "yes"):
            return [
                UserUttered("/get_started_onboarding",
                            {'name': 'get_started_onboarding', 'confidence': 1.0})]
        elif (intent == "no"):
            return [
                UserUttered("/get_started_funfact",
                            {'name': 'get_started_funfact', 'confidence': 1.0})]
        elif (intent == "smalltalk"):
            dispatcher.utter_template("utter_smalltalk", tracker)
            dispatcher.utter_template("utter_ask_continue_form", tracker)
            dispatcher.utter_template("utter_ask_lifestyle", tracker)
        else:
            return [
                UserUttered("/" + intent,
                            {'name': intent, 'confidence': 1.0})]

        return []


class AnswerForm(FormAction):

    def name(self):
        """Unique identifier of the form"""
        return "answer_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["input_value"]

    def slot_mappings(self):
        return {"input_value": [self.from_text()]}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        return []


class GriefForm(FormAction):
    """Collects sales information and adds it to the spreadsheet"""

    def name(self):
        return "grief_form"

    @staticmethod
    def required_slots(tracker):
        return [
            "when",
            "strong_feel",
            "stage_grief",
            "grief_impact",
        ]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "when": [
                self.from_entity(entity="when"),
                self.from_text(),
            ],
            "grief_impact": [
                self.from_text(),
            ],
            "stage_grief": [
                self.from_text(),
            ],
            "strong_feel": [
                self.from_text(),
            ],
        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        return []


class ActionStrongFeel(Action):
    """Example of a custom action"""

    def name(self):
        return "action_strong_feel"

    def run(self, dispatcher, tracker, domain):
        strong_feel = tracker.latest_message.get('text')
        if int(strong_feel) < 6:
            print("Less 6*********" + strong_feel)
            dispatcher.utter_message(template="utter_grief_quote")
            return [AllSlotsReset(None)]
            #         UserUttered("/get_started_feedback", {'name': 'get_started_feedback', 'confidence': 1.0})]
        else:
            print("Big 6*********" + strong_feel)
            dispatcher.utter_message(template="utter_ask_stage_grief")
            # return [SlotSet("strong_feel", strong_feel)]
        return [SlotSet("strong_feel", strong_feel)]


class ActionStageGrief(Action):
    """Example of a custom action"""

    def name(self):
        return "action_stage_grief"

    def run(self, dispatcher, tracker, domain):
        stage_grief = tracker.latest_message.get('text')
        if stage_grief == 'acceptance':
            dispatcher.utter_message(template="utter_pain_purpose")
            # "Making record"
            return [AllSlotsReset(None)]
            #         UserUttered("/get_started_goal", {'name': 'get_started_goal', 'confidence': 1.0})]
        else:
            dispatcher.utter_message(template="utter_ask_grief_impact")
        print("stage_grief*********" + stage_grief)
        return [SlotSet("stage_grief", stage_grief)]


class ActionGriefImpact(Action):
    """Example of a custom action"""

    def name(self):
        return "action_grief_impact"

    def run(self, dispatcher, tracker, domain):
        grief_impact = tracker.latest_message.get('text')
        if grief_impact == 'no':
            dispatcher.utter_message(template="utter_pain_purpose")
            # "Making record"
            # return [Form(None), AllSlotsReset(None),
            #         UserUttered("/get_started_goal", {'name': 'get_started_goal', 'confidence': 1.0})]
        # else:
            # "Making record"
            # return [UserUttered("/get_started_goal", {'name': 'get_started_behav', 'confidence': 1.0})]
        return []


class BehavForm(FormAction):
    """Collects sales information and adds it to the spreadsheet"""

    def name(self):
        return "behav_form"

    @staticmethod
    def required_slots(tracker):
        return [
            "when",
            "length_struggle",
            "medication",
            "pro_help",
            "secret",
        ]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "when": [
                self.from_entity(entity="when"),
                self.from_text(),
            ],
            "length_struggle": [
                self.from_text(),
            ],
            "pro_help": [
                self.from_text(),
            ],
            "medication": [
                self.from_text(),
            ],
            "secret": [
                self.from_text(),
            ],
        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        return []


class ActionStruggleLength(Action):
    """Example of a custom action"""

    def name(self):
        return "action_length_struggle"

    def run(self, dispatcher, tracker, domain):
        length_struggle = tracker.get_slot('length_struggle')
        print(length_struggle)
        # length_struggle = "5"
        if int(length_struggle) > 4:
            print("big more than 4**************"+length_struggle)
            dispatcher.utter_message(template="utter_ask_medication")
        else:
            print("small more than 4**************" + length_struggle)
            dispatcher.utter_message(template="utter_ask_secret")
        return []


class ActionMedication(Action):
    """Example of a custom action"""

    def name(self):
        return "action_medication"

    def run(self, dispatcher, tracker, domain):
        medication = tracker.latest_message.get('text')
        dispatcher.utter_message(template="utter_ask_pro_help}")
        return [SlotSet("medication", medication)]


class ActionProHelp(Action):
    """Example of a custom action"""

    def name(self):
        return "action_pro_help"

    def run(self, dispatcher, tracker, domain):
        pro_help = tracker.latest_message.get('text')
        if pro_help == 'probably':
            dispatcher.utter_message(template="utter_get_help")
            # "Making record"
            return [AllSlotsReset(None)]
                    # UserUttered("/get_started_feedback", {'name': 'get_started_feedback', 'confidence': 1.0})]
        elif pro_help == 'already tried':
            dispatcher.utter_message(template="utter_get_help")
            # "Making record"
            return [AllSlotsReset(None)]
                    # UserUttered("/get_started_mentalH_form", {'name': 'get_started_mentalH_form', 'confidence': 1.0})]
        else:
            dispatcher.utter_message(template="utter_get_help")
            # "Making record"
            return [AllSlotsReset(None)]
                    # UserUttered("/get_started_hopeless_form", {'name': 'get_started_hopeless_form', 'confidence': 1.0})]
        return []


class ActionSecret(Action):
    """Example of a custom action"""

    def name(self):
        return "action_secret"

    def run(self, dispatcher, tracker, domain):
        secret = tracker.latest_message.get('text')
        if secret == "no":
            print(secret)
            dispatcher.utter_message(template="utter_ask_pro_help")
        else:
            dispatcher.utter_message(template="utter_get_help")
            # "Making record"
            return [AllSlotsReset(None)]
                    # UserUttered("/get_started_feedback", {'name': 'get_started_feedback', 'confidence': 1.0})]
        return []
