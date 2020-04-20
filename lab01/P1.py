"""
     Given an average power consumption of a machine p (in Watt) and
     a number of hours operating it, write a program to compute the energy
     consumption (in Watt-hour and in Joules).
     Hint: Energy (in Wh) = power (in W)  time (in h); Joules = 3600  Watt-hour.
"""
power = float(input("Enter power in watt:"))
time = float(input("Enter operating hours:"))
wh = power*time
j = 3600*wh
text = "Energy = {:.2f} Wh or {:.2f} J"
print(text.format(wh,j))