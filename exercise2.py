#!/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. Kanadia

Computer-based immigration office for Kanadia

"""

__author__ = 'Adam Rogers Green, Therese Owusu, Paola Santiago'

import re
import datetime
import json


with open("test_jsons/countries.json", "r") as file_reader:
    country_contents = file_reader.read()
COUNTRY = json.loads(country_contents)
with open("test_jsons/test_returning_citizen.json", "r") as file_reader:
    citizen_contents = file_reader.read()
CITIZEN = json.loads(citizen_contents)
######################
## global constants ##
######################
REQUIRED_FIELDS = ["passport", "first_name", "last_name",
                   "birth_date", "home", "entry_reason", "from"]

PLACES = ["home", "from", "country"]
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


#def valid_visa_format(visa_code):
#        if re.match('^\w{5}-\w{5}$', visa_code) == True and is_more_than_x_years_ago(2, item['visa']['date']) == True:
#            return True
#        else:
#            return False

#for item in CITIZEN:
#        print valid_visa_format(item['visa']['code'])

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


def valid_visa():
    if re.match('^\w{5}-\w{5}$', visa_code) == True and is_more_than_x_years_ago(2, item['visa']['date']) == True:
        return True
    else:
        return False


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



def check_required_fields (CITIZEN):
    #check if all fields in entry record are present with values

    for entries in REQUIRED_FIELDS:
        person = CITIZEN[entries]
        if len(person) < 0:
            return False
        else:
            return True


def location_known(homecountry,fromcountry):

    """
    Checks whether the home country and from country of each citizen in test_returning_citizen.json are valid in the country code countries.json data
    :param home country
    :param from country:
    :return Boolean:
    """
    if country_home and country_from in country_code:
        return True
    else:
        return False

def returning_or_visitor():
    #check if traveller is returning or visitor and then check whether that country needs visitor_visa or not
    if CITIZEN["entry_reason"] == "returning":
        if CITIZEN["home"]["country"] == "KAN":
            return True
        else:
            return False
    elif CITIZEN["entry_reason"] == "visiting" and CITIZEN["home"]["country"] in COUNTRY["code"]:
        country_home = CITIZEN["home"]["country"]
        if COUNTRY[country_home]["visitor_visa_required"] == "0":
            return True
        elif COUNTRY[country_home]["visitor_visa_required"] == "1":
            if valid_visa() == "True":
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def medical_advisory_warning(citizen, country):
    #check whether country has medical_advisory warning from country.json

    boundary = PLACES[1:]
    for a in boundary:
        if a in CITIZEN:
            code_country = CITIZEN["country"]["from"]
            if COUNTRY[code_country]["medical_advisory"] != "":
                return True

    return medical_advisory_warning

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


with open("test_jsons/countries.json", "r") as file_reader:
    country_contents = file_reader.read()
COUNTRY = json.loads(country_contents)
with open("test_jsons/test_returning_citizen.json", "r") as file_reader:
    citizen_contents = file_reader.read()
CITIZEN = json.loads(citizen_contents)


if medical_advisory_warning() == True:
    return "Quarantine"
elif check_required_fields() == False or location_known() == False or returning_or_visitor() == False:
    print "Reject"
else:
    print "Accept"

decide(CITIZEN, COUNTRY)
