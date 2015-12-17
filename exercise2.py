#!/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. Kanadia

Computer-based immigration office for Kanadia

"""

__author__ = 'Adam Rogers Green, Therese Owusu, Paola Santiago'

import re
import datetime
import json

with open("test_jsons/test_returning_citizen.json", "r") as file_reader:
    file_contents = file_reader.read()

json_contents = json.loads(file_contents)

######################
## global constants ##
######################
REQUIRED_FIELDS = ["passport", "first_name", "last_name",
                   "birth_date", "home", "entry_reason", "from"]

######################
## global variables ##
######################
'''
countries:
dictionary mapping country codes (lowercase strings) to dictionaries
containing the following keys:
"code","name","visitor_visa_required",
"transit_visa_required","medical_advisory"
'''
COUNTRIES = None


with open("test_returning_citizen.json", "r") as file_reader:
    file_contents = file_reader.read()
with open("countries.json", "r") as file_reader:
    json_citizens = json.loads(file_contents)


#####################
# HELPER FUNCTIONS ##
#####################




def is_more_than_x_years_ago(x, date_string):
    """
    Check if date is less than x years ago.

    :param x: int representing years
    :param date_string: a date string in format "YYYY-mm-dd"
    :return: True if date is less than x years ago; False otherwise.
    """

    now = datetime.datetime.now()
    x_years_ago = now.replace(year=now.year - x)
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d')

    return (date - x_years_ago).total_seconds() < 0


def decide(input_file, countries_file):
    """
    Decides whether a traveller's entry into Kanadia should be accepted

    :param input_file: The name of a JSON formatted file that contains
        cases to decide
    :param countries_file: The name of a JSON formatted file that contains
        country data, such as whether an entry or transit visa is required,
        and whether there is currently a medical advisory
    :return: List of strings. Possible values of strings are:
        "Accept", "Reject", and "Quarantine"
    """

    return ["Reject"]


def valid_passport_format(passport_number):
    """
    Checks whether a passport number is five sets of five alpha-number characters separated by dashes
    :param passport_number: alpha-numeric string
    :return: Boolean; True if the format is valid, False otherwise
    """

    if re.match('^\w{5}-\w{5}-\w{5}-\w{5}-\w{5}$', passport_number):
        return True
    else:
        return False


for item in file_contents:
    print (valid_passport_format(item["passport"]))

def valid_visa_format(visa_code):
    """
    Checks whether a visa code is two groups of five alphanumeric characters
    :param visa_code: alphanumeric string
    :return: Boolean; True if the format is valid, False otherwise

    """
    if re.match('^\w{5}-\w{5}-$', visa_code):
        return True
    else:
        return False

for item in json_contents:
        print ((valid_visa_format(item['visa_code']))



def valid_date_format(date_string):
    """
    Checks whether a date has the format YYYY-mm-dd in numbers
    :param date_string: date to be checked
    :return: Boolean True if the format is valid, False otherwise
    """


    if re.match('^\d{4}-\d{2}-\d{2}$', date_string):
        return True
    else:
        return False


for item in json_contents:
    print (valid_date_format(item['birth_date']))



def home_from_country(location_known):
    if location_known is CITIZEN["home"]["country"] == "KAN":
        return True
    else:
        if location_known in COUNTRY:
            return


