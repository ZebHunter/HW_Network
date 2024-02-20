def count_sequences(curr_signal):
    maxi = 0
    sequences = [0 for i in range(len(curr_signal) + 1)]
    current_sequence = 1

    for i in range(1, len(curr_signal)):
        if curr_signal[i] == curr_signal[i - 1]:
            current_sequence += 1
        else:
            sequences[current_sequence] += 1
            maxi = max(maxi, current_sequence)
            current_sequence = 1

    if current_sequence > 0:
        maxi = max(maxi, current_sequence)
        sequences[current_sequence] += 1

    return maxi, sequences


def count_ones(curr_signal):
    return curr_signal.count(1)


def longest_substr(array):
    return count_sequences(array)[0]


def f_mid(curr_signal, f):
    a = count_sequences(curr_signal)[1]
    suma = 0
    for i in range(1, len(a)):
        suma += i * a[i] * f // i
    return (suma / len(curr_signal))
