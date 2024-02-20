from matplotlib import pyplot as plt


def print_graph(type_code, x_values, y_values):
    plt.grid(True)
    plt.step(x_values, y_values, where='post', color='black')
    plt.xlabel('Time')
    plt.ylabel('Signal Value')
    plt.title(type_code)
    for x in x_values:
        plt.axvline(x=x, color='black', linestyle='--', linewidth=1)
    if type_code == 'AMI':
        transitions_high = [i for i in range(0, len(y_values)) if y_values[i] == 1]
        transitions_invert = [i for i in range(0, len(y_values)) if y_values[i] == -1]
        transitions_low = [i for i in range(0, len(y_values)) if y_values[i] == 0]
        for i in range(len(transitions_high)):
            plt.hlines(y=1, xmin=transitions_high[i] + 1, xmax=transitions_high[i] + 2, color='blue', linestyles='-')
        for i in range(len(transitions_invert)):
            plt.hlines(y=-1, xmin=transitions_invert[i] + 1, xmax=transitions_invert[i] + 2, color='blue',
                       linestyles='-')
        for i in range(len(transitions_low)):
            plt.hlines(y=0, xmin=transitions_low[i] + 1, xmax=transitions_low[i] + 2, color='red', linestyles='-')

    if type_code == 'NRZ':
        transitions_high = [i for i in range(0, len(y_values)) if y_values[i] == 1]
        transitions_low = [i for i in range(0, len(y_values)) if y_values[i] == 0]
        for i in range(len(transitions_high)):
            plt.hlines(y=1, xmin=transitions_high[i] + 1, xmax=transitions_high[i] + 2, color='blue', linestyles='-')
        for i in range(len(transitions_low)):
            plt.hlines(y=0, xmin=transitions_low[i] + 1, xmax=transitions_low[i] + 2, color='red', linestyles='-')

    if type_code == 'RZ':
        transitions_high = [x_values[i] for i in range(0, len(y_values)) if y_values[i] == 1]
        transitions_low = [x_values[i] for i in range(0, len(y_values)) if y_values[i] == -1]
        for i in range(len(transitions_high)):
            plt.hlines(y=1, xmin=transitions_high[i], xmax=transitions_high[i] + (x_values[1] - x_values[0]),
                       color='blue', linestyles='-')
        for i in range(len(transitions_low)):
            plt.hlines(y=-1, xmin=transitions_low[i], xmax=transitions_low[i] + (x_values[1] - x_values[0]),
                       color='red', linestyles='-')
    plt.show()


def print_manchester(x_values, y_values, signal_values):
    plt.grid(True)
    plt.step(x_values, y_values, where='post', color='black')
    plt.xlabel('Time')
    plt.ylabel('Signal Value')
    plt.title('Manchester 2 (IEEE 802.3)')
    for x in x_values:
        plt.axvline(x=x, color='black', linestyle='--', linewidth=1)
    transitions_high = []
    transitions_low = []
    for i in range(len(signal_values)):
        if i != len(signal_values) - 1 and (signal_values[i] == 1 and signal_values[i+1] == 1):
            transitions_high.append(x_values[2*i+1])
        if i != 0 and (signal_values[i-1] == 1 and signal_values[i] == 1):
            transitions_high.append(x_values[2*i+1])
        if signal_values[i] == 0 and signal_values[i+1] == 1:
            transitions_high.append(x_values[2 * i + 3])

    for i in range(len(signal_values)):
        if i != len(signal_values) - 1 and (signal_values[i] == 0 and signal_values[i+1] == 0):
            transitions_low.append(x_values[2*i+1])
        if i != 0 and (signal_values[i-1] == 0 and signal_values[i] == 0):
            transitions_low.append(x_values[2*i+1])
        if i != len(signal_values) - 1 and signal_values[i] == 1 and signal_values[i+1] == 0:
            transitions_low.append(x_values[2 * i + 3])

    for i in range(len(transitions_high)):
        plt.axvline(x=transitions_high[i], ymin=0.05, ymax=0.95, color='blue')
    for i in range(len(transitions_low)):
        plt.axvline(x=transitions_low[i], ymin=0.05, ymax=0.95, color='red')
    plt.show()
