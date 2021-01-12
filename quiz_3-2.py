# Author: PJG (AMDG) 1/12/2021


ledger = [['Sebulba', 100, 200, 400], ['Skywalker', 500, 100, 20000], ['Reeso', 200, 700, 100]]


def ledger_sorter(lst):
names = []
numbers = []
    if x in lst is int:
        numbers += x
    else:
        names += x
    return names, numbers


print(ledger_sorter(ledger))