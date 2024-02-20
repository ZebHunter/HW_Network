from util.charts import *
from util.util import *

def rz(signals, C):
	print(*signals)
	x_values = []
	y_values = []

	i = 1

	while i < (len(signals)+1):
		x_values.append(i)
		i+=1/2

	for i in range(len(signals)):
		if(signals[i] == 0):
			y_values.append(-1)
			y_values.append(0)
		else:
			y_values.append(1)
			y_values.append(0)

	print(*signals)
	print("T = t, t = 1/C =", str(1/C))
	print("f_h = 1/T = C =", str(C), "MHz")
	print("f_l = C/2 =", str(C/2), "MHz")
	ones = signals.count(1)
	zeros = signals.count(0)
	print("f_mid =", (zeros*C + ones*C/2)/(len(signals)), "MHz")
	print("Middle of spectrum = (f_h + f_l)/2 =", (C + C/2)/2, "MHz")
	print("Spectrum width = f_h - f_l =", C - C/2, "MHz")
	print("bandwidth F: f_h - f_l =", (C - C/2), "MHz")

	print_graph("RZ", x_values, y_values)
