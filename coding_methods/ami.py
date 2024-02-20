from util.charts import *
from util.util import *


def ami(signals, C):
    print(*signals)
    is_one = 0
    x_values = range(1, len(signals) + 1)
    y_values = []

    for i in range(len(signals)):
        if (signals[i] == 0):
            y_values.append(0)
        else:
            if (is_one):
                y_values.append(-1)
                is_one = 0
            else:
                y_values.append(1)
                is_one = 1

    print(*signals)
    print("T = 2t, t = 1/C =", str(1 / C))
    print("f_h = 1/T = C/2 =", str(C / 2), "MHz")
    print("f_l =  1 / (2 * longest_substr * t) = C/(2* longest_substr) =", str(C / (2 * longest_substr_ami(signals))),
          "MHz")
    print("f_mid =", f_mid_ami(signals, C / 2), "MHz")
    print("Middle of spectrum = (f_h + f_l)/2 =", (C / 2 + C / (longest_substr_ami(signals) * 2)) / 2, "MHz")
    print("Spectrum width = f_h - f_l =", C / 2 - C / (longest_substr_ami(signals) * 2), "MHz")
    print("bandwidth F: f_h - f_l =", (C / 2 - C / (longest_substr_ami(signals) * 2)), "MHz")

    print_graph("AMI", x_values, y_values)


def count_sequences_ami(curr_signal):
    maxi = 1
    sequences = [0 for i in range(len(curr_signal) + 1)]
    current_sequence = 1

    for i in range(1, len(curr_signal)):
        if curr_signal[i] == curr_signal[i - 1] == 0:
            current_sequence += 1
        else:
            sequences[current_sequence] += 1
            maxi = max(maxi, current_sequence)
            current_sequence = 1

    if current_sequence > 0:
        maxi = max(maxi, current_sequence)
        sequences[current_sequence] += 1

    return maxi, sequences


def longest_substr_ami(array):
    return count_sequences_ami(array)[0]


def f_mid_ami(curr_signal, f):
    a = count_sequences_ami(curr_signal)[1]
    suma = 0
    for i in range(1, len(a)):
        suma += i * a[i] * f // i
    return suma / len(curr_signal)
