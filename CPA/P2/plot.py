import matplotlib.pyplot as plt
x = [2.0, 4.0, 8.0, 16,32]
# ys0 = [26.098569,15.369443,8.308206,4.834699,3.126337]
# ys1 = [22.969833,11.502033,6.292179,3.592557,2.471968]
# ys2 = [17.304959,8.623851,5.019181,2.696642,1.853828]
# yd1 = [17.251117,8.627753,4.496865,2.693916,1.849314]
# yd2 = [17.234738,8.622996,4.586967,2.693860,1.849164]
#Tiempo2
ys0 = [
0.84,
0.80,
0.6625,
0.4,
0.206
]
ys1 = [
0.26,
0.205,
0.177,
0.165,
0.10
]
ys2 = [
0.405,
0.33,
0.288,
0.20,
0.12
]
yd1 = [
0.0329,
0.021,
0.125,
0.0043,
0.0017
]
yd2 = [
0.12,
0.045,
0.02,
0.0075,
0.0031,
]


plt.plot(x,ys0, label = "Static 0" )
plt.plot(x,ys1, label = "Static 1" )
plt.plot(x,ys2, label = "Static 2" )
plt.plot(x,yd1, label = "Dynamic 1" )
plt.plot(x,yd2, label = "Dynamic 2" )

plt.ylabel('Eficiencia')
plt.xlabel('Hilos')
plt.legend()
plt.axis([0, 32, 0, 1])
plt.show()
