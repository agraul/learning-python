x = 0.25
delta = 0.01
if x > 0 and x < 1:
    low = x
    high = 1
else:
    low = 1
    high = x
ans = (high + low) / 2.0

while abs(ans**2 - x) >= delta:
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0

print("{0} is close to the square root of  {1}" .format(ans, x))

