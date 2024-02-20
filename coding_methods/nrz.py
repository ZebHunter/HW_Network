from util.charts import *
from util.util import *

def nrz(signals, C):
	print(*signals)
	print("T = 2t, t = 1/C =", str(1/C))
	print("f_h = 1/T = C/2 =", str(C/2), "MHz")
	print("f_l =  1 / (2 * longest_substr * t) = C/(2* longest_substr) =", str(C/(longest_substr(signals) * 2)), "MHz")
	print("f_mid =", f_mid(signals, C/2), "MHz")
	print("Middle of spectrum = (f_h + f_l)/2 =", (C/2 + C/(longest_substr(signals) * 2))/2, "MHz")
	print("Spectrum width = f_h - f_l =", C/2 - C/(longest_substr(signals) * 2), "MHz")
	print("bandwidth F: f_h - f_l =", (C/2 - C/(longest_substr(signals) * 2)), "MHz")

	print_graph("NRZ", range(1, len(signals)+1), signals)