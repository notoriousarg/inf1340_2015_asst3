#!/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists. """

__author__ = 'Adam Rogers-Green, Therese Owusu, Paola Santiago'


#####################
# HELPER FUNCTIONS ##
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

def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class UnknownAttributeException(Exception):
    """
    Raised when attempting set operations on a table
    that does not contain the named attribute
    """
    pass


def selection(t, f):
    """

    Perform select operation on table t that satisfy condition f.
    Example:
    > R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    ># Define function f that returns True iff
    > # the last element in the row is greater than 3.
    > def f(row): row[-1] > 3
    > select(R, f)
    [["A", "B", "C"], [4, 5, 6]]
    """
    selection_list = []
    selection_list.append(t[0])
    for row in t[1:]:
        if f(row) is True:
            selection_list.append(row)
    if len(selection_list) == 1:
        return None
    else:
        return selection_list


    return []

#print(selection(, filter_employees))


def projection(t, r):
    """
    Perform projection operation on table t
    using the attributes subset r.

    Example:
    > R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    > projection(R, ["A", "C"])
    [["A", "C"], [1, 3], [4, 6]]

    """
    projection_list = []
    new_list = []
    for i in xrange(len(t[0])):
        for s in xrange(len(r)):
            if r[s] == t[0][i]:
                projection_list.append(i)
            else:
                UnknownAttributeException("Not the same attribution")
    for n in xrange(len(t)):
        new_list.append([t[n][index] for index in projection_list])
    return remove_duplicates(new_list)

    return []


def cross_product(t1, t2):
    """
    Return the cross-product of tables t1 and t2.

    Example:
    > R1 = [["A", "B"], [1,2], [3,4]]
    > R2 = [["C", "D"], [5,6]]
    [["A", "B", "C", "D"], [1, 2, 5, 6], [3, 4, 5, 6]]


    """

    result = []
    result.append(t1[0] + t2[0])
    t1_i = 1
    for i in range(1, len(t1)):
        t2_i = 1
        for j in range(1, len(t2)):
            result.append(t1[i] + t2[j])
            t2_i += 1
        t1_i += 1
    if len(result) == 1:
        return None
    else:
        return result

    return result
