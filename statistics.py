def calculateStats(numbers):
    
    if numbers is None:
    return none
    numbers = [1.5,2,3,4]
    avg = sum(numbers) / len(numbers) 
    maximum = max(numbers)
    minimum = min(numbers)

    dict1 = dict({"avg":avg,"max":maximum,"min":minimum})
    
