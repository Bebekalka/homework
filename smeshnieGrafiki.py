import matplotlib.pyplot as plt
x1 = [i for i in range(-12, 13)]
x2 = [i for i in range(-4, 5)]
x3 = [i for i in range(-12, -3)]
x4 = [i for i in range(4, 13)]
x5 = [i for i in range(-4, 1)]
x6 = [i for i in range(-4, 1)]
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []

for i in x1:
    y1.append(-1/18 * i**2 + 12)
for i in x2:
    y2.append(-1/8 * i**2 + 6)
for i in x3:
    y3.append(-1/8 * (i+8)**2 + 6)
for i in x4:
    y4.append(-1/8 * (i-8)**2 + 6)
for i in x5:
    y5.append(2 * (i+3)**2 - 9)
for i in x6:
    y6.append(1.5 * (i+3)**2 - 10)
plt.grid(True)
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.plot(x6, y6)
plt.legend(("-1/18*x1**2+12", "-1/8*x2**2+6",
            "-1/8*(x3+8)**2+6", "-1/8*(x4-8)**2+6",
            "2*(x5+3)**2-9", "1.5*(x6+3)**2-10"))
plt.show()
