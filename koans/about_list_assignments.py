#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrayAssignments in the Ruby Koans
#

from runner.koan import *

class AboutListAssignments(Koan):
    def test_non_parallel_assignment(self):
        names = ["John", "Smith"]
        self.assertEqual(['John','Smith'], names)

    def test_parallel_assignments(self):
        first_name, last_name = ["John", "Smith"]
        self.assertEqual('John', first_name) #Enter first name in string form 
        self.assertEqual('Smith', last_name) #Enter last name in string form 

    def test_parallel_assignments_with_extra_values(self):
        title, *first_names, last_name = ["Sir", "Ricky", "Bobby", "Worthington"]
        self.assertEqual("Sir", title) #Enter title such as MR. or Mrs. 
        self.assertEqual(["Ricky","Bobby"], first_names) #Since there is no middle initial slot put both in first name 
        self.assertEqual("Worthington", last_name) #Enter last name of list 

    def test_parallel_assignments_with_fewer_values(self):
        title, *first_names, last_name = ["Mr", "Bond"]
        self.assertEqual("Mr", title) #Title such as mr, mrs
        self.assertEqual([], first_names) #Since there is no first name i made the list empty 
        self.assertEqual("Bond", last_name) #Entered last name 

    def test_parallel_assignments_with_sublists(self):
        first_name, last_name = [["Willie", "Rae"], "Johnson"]
        self.assertEqual(["Willie", "Rae"], first_name) #Since there is no middle initial slot put both in first name 
        self.assertEqual("Johnson", last_name)

    def test_swapping_with_parallel_assignment(self):
        first_name = "Roy"
        last_name = "Rob"
        first_name, last_name = last_name, first_name
        self.assertEqual("Rob", first_name) #Swap First name with Last name
        self.assertEqual("Roy", last_name)  #Swap Last name with First name 

