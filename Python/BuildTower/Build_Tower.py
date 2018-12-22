def tower_builder(n_floors):
    towerList = []
    floor = "*"
    buffVal = n_floors - 1
    for i in range(n_floors):
        if i == 0:
            buffer = " " * buffVal
            towerList.append(buffer + floor + buffer)
            buffVal = buffVal - 1
            floor = floor + "**"
        else:
            buffer = " " * buffVal
            towerList.append(buffer + floor + buffer)
            buffVal = buffVal - 1
            floor = floor + "**"
    print(towerList)

tower_builder(3)