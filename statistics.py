import math

def calculateStats(numbers):
    
    if len(numbers) < 1:
        return math.nan
    avg = float(sum(numbers) / len(numbers))
    maximum = max(numbers)
    minimum = min(numbers)

    dict1 = dict({"avg":avg,"max":maximum,"min":minimum})
    return dict1
