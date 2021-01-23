import math

def calculateStats(numbers):
    
    if len(numbers) == 0:
        return math.nan
    avg = sum(numbers) / len(numbers) 
    maximum = max(numbers)
    minimum = min(numbers)

    dict1 = dict({"avg":avg,"max":maximum,"min":minimum})
    
