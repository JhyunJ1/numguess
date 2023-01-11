from random import shuffle, choice

doors = [0,0,1]

n = 100000

nochange = 0
change = 0

for _ in range(100000):
    shuffle(doors)
    c = choice(doors)
    doors.remove(0)
    if c == 1:
        nochange += 1

float(nochange) /= n
float(change) = 1.0 - nochagne


print(f"If, nothing change? {nochange}!!")
print(f"if, change? {change}!!")

