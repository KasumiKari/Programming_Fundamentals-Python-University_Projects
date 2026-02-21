# --- Defining countdown function for positive n ---
def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)

# --- Defining countup function for negative n ---
def countup(n):
    if n >= 0:
        print("Blastoff!")
    else:
        print(n)
        countup(n+1)

# --- main program ---
s = input("Enter a positive or negative number: ")
n = int(s)

if n > 0:
    countdown(n)
elif n < 0:
    countup(n)
else:
    print("Blastoff!")
