#!/usr/bin/python3

################################
# File Name:	basketUnitTest.py
# Author:		Chadd Williams
# Date:			11/17/2014
# Class:		CS 360
# Assignment:	Lecture Examples
# Purpose:		
################################

import unittest
from basket import Basket
from SaleItem import SaleItem
from ShippingLogic import ShippingLogic

class TestBasketFunctions(unittest.TestCase):
	
	def setUp (self):
		self.theBasket = Basket ()
		
	def tearDown (self):
		pass
		
	def test_addItem (self):
		item = SaleItem(['10', '2', 'TestItem1'])
		self.theBasket.addItem((1, item))
		self.assertTrue (self.theBasket.contains (item.getID()))
		
	def test_getTotalShipping (self):
		""" This is currently bugged
		"""
		sLogic = ShippingLogic ()
		item = SaleItem (['10', '1', 'TestItem2'])
		self.theBasket.addItem((1, item))
		self.assertEqual (self.theBasket.getTotalShipping(sLogic), 7)
		
	def test_contains (self):
		item = SaleItem(['10', '1', 'TestItem3'])
		self.theBasket.addItem((1, item))
		self.assertTrue (self.theBasket.contains (item.getID())
		
	def test_merge (self):
		""" Not quite finished 
		"""
		item = SaleItem(['10', '1', 'TestItem4'])
		self.theBasket.addItem((1, item))
		self.theBasket.merge (item.getId(), 10)
