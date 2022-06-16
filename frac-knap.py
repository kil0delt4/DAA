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
items = [('A', 200, 40), ('B', 120, 20), ('C', 100, 10), ('D', 100, 50)]
print(greedyKnapsack(items, 60))