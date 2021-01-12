# Author: PJG (AMDG) 1/12/2021

younglings = ['Petro', 'Katooni', 'Byph', 'Ganodi', 'Zatt', 'Gungi']
race = ['Human', 'Tholothian', 'Ithorian', 'Rodian', 'Nautolan', 'Wookie']



def young_race(younglings, race):
    total_lst = []
    for i, v in enumerate(younglings):
        total_lst += v
    for i, v in enumerate(race):
        total_lst += v
    return total_lst


print(young_race(younglings, race))