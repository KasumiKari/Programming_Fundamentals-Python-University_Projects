# STAGE 1
def sleep_score(hours, goal=8):
    return 0
print(sleep_score(7))

# STAGE 2
def sleep_score(hours, goal=8):
    # implementing basic proportional score
    return(hours/goal) * 100
print(sleep_score(7))
print(sleep_score(8))
print(sleep_score(12))

# STAGE 3
def sleep_score(hours, goal=8):
    # Clamp score to 0..100 and round to int
    mark = (hours/goal) * 100
    if mark < 0:
        mark = 0
    if mark > 100:
        mark = 100
    return(int(round(mark)))
print(sleep_score(7))
print(sleep_score(8))
print(sleep_score(12))

# STAGE 4
def sleep_score(hours, goal=8):
    # validating inputs for faster debugging
    if not isinstance(hours, (int, float)) or not isinstance (goal, (int, float)):
        raise TypeError("hours and goals must be numbers")
    if not (0 <= hours <= 24):
        raise ValueError("hours must be between 0 and 24")
    if not (4 <= goal <= 12):
        raise ValueError("goal must be between 4 and 12 hours")

    mark = (hours/goal) * 100
    mark = max(0, min(100, mark))
    
    return(int(round(mark)))

print(sleep_score(7))
print(sleep_score(8))
print(sleep_score(12))
