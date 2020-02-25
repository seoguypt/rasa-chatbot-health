## behav story1

* alarming_behaviors
    - utter_empathy
    - utter_ask_length_struggle
* enter_data{"length_struggle":"3"}
    - slot{"length_struggle":"3"}
    - action_length_struggle
* enter_data{"secret":"no"}
	- slot{"secret":"no"}
    - action_secret
* enter_data{"pro_help":"probably"}
    - slot{"pro_help":"probably"}
    - action_pro_help

## behav story2

* alarming_behaviors
    - utter_empathy
	- utter_ask_length_struggle
* enter_data{"length_struggle":"3"}
    - slot{"length_struggle":"3"}
	- action_length_struggle
* enter_data{"secret":"yes"}
    - slot{"secret":"yes"}
	- action_secret
	- slot{"secret":"yes"}

## behav story3

* alarming_behaviors
    - utter_empathy
    - utter_ask_length_struggle
* enter_data{"length_struggle":"3"}
    - slot{"length_struggle":"3"}
    - action_length_struggle
* enter_data{"secret":"no"}
	- slot{"secret":"no"}
    - action_secret
* enter_data{"pro_help":"already tried"}
    - slot{"pro_help":"already tried"}
    - action_pro_help

## behav story4

* alarming_behaviors
    - utter_empathy
    - utter_ask_length_struggle
* enter_data{"length_struggle":"3"}
    - slot{"length_struggle":"3"}
    - action_length_struggle
* enter_data{"secret":"no"}
    - slot{"secret":"no"}
    - action_secret
* enter_data{"pro_help":"not really"}
    - slot{"pro_help":"not really"}
    - action_pro_help

## behav story5

* alarming_behaviors
    - utter_empathy
    - utter_ask_length_struggle
* enter_data{"length_struggle":"5"}
    - slot{"length_struggle":"5"}
    - action_length_struggle
* anitdepressant{"medication":"Trintellix"}
    - slot{"medication":"Trintellix"}
    - utter_ask_pro_help
* enter_data{"pro_help":"not really"}
    - slot{"pro_help":"not really"}
    - action_pro_help

## behav story6

* alarming_behaviors
    - utter_empathy
    - utter_ask_length_struggle
* smalltalk
    - respond_smalltalk
    - utter_ask_continue
* enter_data{"length_struggle":"3"}
    - slot{"length_struggle":"3"}
    - action_length_struggle
* enter_data{"secret":"no"}
	- slot{"secret":"no"}
    - action_secret
* enter_data{"pro_help":"probably"}
    - slot{"pro_help":"probably"}
    - action_pro_help

## behav story7

* alarming_behaviors
    - utter_empathy
	- utter_ask_length_struggle
* smalltalk
    - respond_smalltalk
    - utter_ask_continue
* enter_data{"length_struggle":"3"}
    - slot{"length_struggle":"3"}
	- action_length_struggle
* enter_data{"secret":"yes"}
    - slot{"secret":"yes"}
	- action_secret
	- slot{"secret":"yes"}

## behav story8

* alarming_behaviors
    - utter_empathy
    - utter_ask_length_struggle
* smalltalk
    - respond_smalltalk
    - utter_ask_continue
* enter_data{"length_struggle":"3"}
    - slot{"length_struggle":"3"}
    - action_length_struggle
* enter_data{"secret":"no"}
	- slot{"secret":"no"}
    - action_secret
* enter_data{"pro_help":"already tried"}
    - slot{"pro_help":"already tried"}
    - action_pro_help

## behav story9

* alarming_behaviors
    - utter_empathy
    - utter_ask_length_struggle
* smalltalk
    - respond_smalltalk
    - utter_ask_continue
* enter_data{"length_struggle":"3"}
    - slot{"length_struggle":"3"}
    - action_length_struggle
* enter_data{"secret":"no"}
    - slot{"secret":"no"}
    - action_secret
* enter_data{"pro_help":"not really"}
    - slot{"pro_help":"not really"}
    - action_pro_help

## behav story10

* alarming_behaviors
    - utter_empathy
    - utter_ask_length_struggle
* smalltalk
    - respond_smalltalk
    - utter_ask_continue
* enter_data{"length_struggle":"5"}
    - slot{"length_struggle":"5"}
    - action_length_struggle
* anitdepressant{"medication":"Trintellix"}
    - slot{"medication":"Trintellix"}
    - utter_ask_pro_help
* enter_data{"pro_help":"not really"}
    - slot{"pro_help":"not really"}
    - action_pro_help
