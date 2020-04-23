#!/usr/bin/env python3

import pickle as pkl
import sys


def purchase_shoe(shoe, quantity):
    """Adjust inventory for shoe purchase"""
    #TODO: Update this to match new format found in shoe_inventory.pkl
    stock[shoe] = stock.get(shoe) - quantity
    return stock

