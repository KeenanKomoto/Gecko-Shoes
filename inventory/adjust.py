#!/usr/bin/env python3

import pickle as pkl

def read_inventory_file():
    with open("shoe_inventory.pkl", 'rb') as handle:
        STOCK = pkl.load(handle)

def write_inventory(stock):
    with open("shoe_inventory.pkl", 'wb') as handle:
        pkl.dump(stock, handle)

def restock_shoe_quantity(shoe, size, color, quantity):
    stock = read_inventory_file()
    stock[shoe][size][color] += quantity
    write_inventory(stock)
