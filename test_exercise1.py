#!/usr/bin/env python

""" Assignment 3, Exercise 1, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise1 import selection, projection, cross_product


###########
# TABLES ##
###########

EMPLOYEES = [["Surname", "FirstName", "Age", "Salary"],
             ["Smith", "Mary", 25, 2000],
             ["Black", "Lucy", 40, 3000],
             ["Verdi", "Nico", 36, 4500],
             ["Smith", "Mark", 40, 3900]]

R1 = [["Employee", "Department"],
      ["Smith", "sales"],
      ["Black", "production"],
      ["White", "production"]]

R2 = [["Department", "Head"],
      ["production", "Mori"],
      ["sales", "Brown"]]

#####################
# HELPER FUNCTIONS ##
#####################

def is_equal(t1, t2):
    t1.sort()
    t2.sort()

    return t1 == t2


#####################
# FILTER FUNCTIONS ##
#####################

def filter_employees(row):
    """
    Check if employee represented by row
    is AT LEAST 30 years old and makes
    MORE THAN 3500.
    :param row: A List in the format:
        [{Surname}, {FirstName}, {Age}, {Salary}]
    :return: True if the row satisfies the condition.
    """
    return row[-2] >= 30 and row[-1] > 3500


def filter_eligible_voters(row):
    return row[-1] >= 18


###################
# TEST FUNCTIONS ##
###################

def test_selection():
    """
    Test select operation.
    """

    result = [["Surname", "FirstName", "Age", "Salary"],
              ["Verdi", "Nico", 36, 4500],
              ["Smith", "Mark", 40, 3900]]

    assert is_equal(result, selection(EMPLOYEES, filter_employees))


def test_projection():
    """
    Test projection operation.
    """

    result = [["Surname", "FirstName"],
              ["Smith", "Mary"],
              ["Black", "Lucy"],
              ["Verdi", "Nico"],
              ["Smith", "Mark"]]

    assert is_equal(result, projection(EMPLOYEES, ["Surname", "FirstName"]))


def test_cross_product():
    """
    Test cross product operation.
    """

    result = [["Employee", "Department", "Department", "Head"],
              ["Smith", "sales", "production", "Mori"],
              ["Smith", "sales", "sales", "Brown"],
              ["Black", "production", "production", "Mori"],
              ["Black", "production", "sales", "Brown"],
              ["White", "production", "production", "Mori"],
              ["White", "production", "sales", "Brown"]]

    assert is_equal(result, cross_product(R1, R2))

###########################
# ADDITIONAL TEST TABLE ##
###########################


BASEBALL_PLAYERS = [["Surname", "First Name", "Shirt Number"],
                    ["Donaldson", "Josh", 20],
                    ["Bird", "Greg", 31],
                    ["Encarnacion", "Edwin", 10],
                    ["Archer", "Chris", 22],
                    ["Machado", "Manny", 13],
                    ["Bogaerts", "Xander", 2]]



##########################
# ADDITIONAL TEST CASES ##
##########################


def test_projection_returns_error():
    # Checks if projection() function raises an "AttributeError" if column is in the attributes list but not in table1.
    try:
        projection(BASEBALL_PLAYERS, ["Shirt Number", "name"])
    except AttributeError:
        assert True


def test_selection_returns_none():
    # Checks if selection() function returns "None" if the result is an empty table.
    t = [["Age", "Name"],
         ["Dan", 50],
         ["Mary", 44],
         ["Jose", 54]]

    def f(r):
        return r[-1] < 35

    assert selection(t, f) == None


def test_cross_product_returns_none():
    # Checks if  cross_product() function returns "None" if result is empty table.
    t1 = [["Name", "Age"],
          ["Dan", 50],
          ["Mary", 44],
          ["Jose", 54]]
    t2 = [["Name", "Age"]]

    assert cross_product(t1, t2) == None