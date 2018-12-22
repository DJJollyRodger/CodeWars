def countPeopleOn(amount, amountOn):
    amount = amount + amountOn
    return amount

def countPeopleOff(amount, amountOff):
    amount = amount - amountOff
    return amount

def number(bus_stops):
    busCapacity = 0
    for trips in bus_stops:
        busCapacity = countPeopleOn(busCapacity, trips[0])
        busCapacity = countPeopleOff(busCapacity, trips[1])
    print(busCapacity)