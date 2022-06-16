def greedyKnapsack(items, wtMax):
    items = sorted(items, key=lambda items: items[1]/items[2], reverse=True)
    print(items)
    chosen = {}
    profit = 0
    for i in range(len(items)):
        name,value,weight = items[i]
        numOfItems = (wtMax - wtMax % weight) / weight
        chosen[name] = numOfItems
        wtMax = wtMax % weight
        profit += numOfItems * value
    return(round(profit,2)), chosen
   
# Driver code 
items = [('A', 2.2, 170), ('B', 8, 1500), ('C', 22, 1500), ('D', 0.26, 15), ('E', 0.4, 20), ('F', 1, 200)]
maxCapacity = 2000
print(greedyKnapsack(items, maxCapacity))
