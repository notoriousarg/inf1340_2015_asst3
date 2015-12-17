#!/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. Kanadia

Computer-based immigration office for Kanadia

"""

__author__ = 'Adam Rogers-Green, Therese Owusu, Paola Santiago'

import re
import datetime
import json

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
    if valid_visa_format() == True and is_more_than_x_years_ago(2, ['visa']['date']) == True:
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


def check_required_fields(citizen):
    """check if all fields in entry record are present with values
        :param citizen: each value in the citizens json
        :return: Boolean True if the format is valid, False otherwise
    """
    acceptable = True
    for entries in REQUIRED_FIELDS:
        if entries not in citizen:
            acceptable = False
    return acceptable


def location_known(citizen, country):
    """
    Checks whether the home country and from country of each citizen in test_returning_citizen.json are valid in the country code countries.json data
    :param home country and from country of citizen.json
    :param country code of country.json
    :return Boolean: True if both home and from countries are valid, false otherwise
    """
    if citizen["home"]["country"] and citizen["from"]["country"] in country["code"]:
        return True
    else:
        return False


def returning(citizen):
    """
     check if traveller is returning
     :param: citizen entry reason and home country in citizen.json
      :return: Boolean - true if it is valid, false otherwise
    """
    if citizen["entry_reason"] == "returning":
        if citizen["home"]["country"] == "KAN":
            return True
        else:
            return False


def visitor(citizen, country):
    """
    :param citizen: check whether that country needs visitor_visa or not in country.json
    :return: Boolean - true if citizen does not need visa or has required visa, false otherwise
    """
    if citizen["entry_reason"] == "visiting" and citizen["home"]["country"] in country["code"]:
        country_home = citizen["home"]["country"]
        if country[country_home]["visitor_visa_required"] == "0":
            return True
        elif country[country_home]["visitor_visa_required"] == "1":
            if valid_visa() == "True":
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def medical_advisory_warning(citizen, country):
    """check whether country has medical_advisory warning from country.json
    :param: citizen.json, country.json
    :return: Boolean - true if no medical advisory warning
    """

    boundary = PLACES[1:]
    for a in boundary:
        if a in citizen:
            code_country = citizen["country"]["from"]
            if country[code_country]["medical_advisory"] != "":
                return True


def decide(input_file, countries_file):
    """
    Decides whether a traveller's entry into Kanadia should be accepted

    :param input_file: The name of a JSON formatted file that contains
        cases to decide
    :param countries_file: The name of a JSON formatted file that contains
        country data, such as whether an entry or transit visa is required,
        and whether there is currently a medical advisory
    :return: results [] List of strings. Possible values of strings are:
        "Accept", "Reject", and "Quarantine"
    """

    with open("test_jsons/countries.json", "r") as file_reader:
        country_contents = file_reader.read()
        country = json.loads(country_contents)
    with open("test_jsons/test_returning_citizen.json", "r") as file_reader:
        citizen_contents = file_reader.read()
        citizen = json.loads(citizen_contents)

    results = []

    for c in citizen:
        reject = False
        quarantine = False
        accept = False
        if not check_required_fields(citizen):
            reject = True
        elif not location_known(citizen, country):
            reject = True
        else:
            if returning(citizen):
                accept = True
            elif visitor(citizen):
                accept = True
            else:
                reject = True

            if medical_advisory_warning(citizen, country):
                quarantine = True

        if reject:
            results.append("Reject")
        elif quarantine:
            results.append("Quarantine")
        elif accept:
            results.append("Accept")

    return results
