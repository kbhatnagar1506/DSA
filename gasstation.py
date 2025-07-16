def gasstation(gas,cost):
    if sum(gas) < sum(cost):
        return -1
    marker = gas[0] - cost[0]
    for i in range(0,len(gas)):
        difference = gas[i] - cost[i]
        if  difference> marker :
            marker = difference
            index = i
    run = 0 
    tank = gas[index]
    for i in range(index,len(gas)):
        if tank  >= 0 and i != len(gas)-1:
            tank = tank -  cost[i] + gas[i+1]
            run = run + 1
        if i == len(gas)-1:
            tank = tank  - cost[i] +gas[0]
            run = run + 1
    print(tank)
    for i in range(0,index-1):
        if tank >= 0 :
            tank = tank - cost[i] + gas[i+1]
            run = run + 1
    if run == len(gas)-1:
        return tank
    else:
        return -1 

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(gasstation(gas,cost))