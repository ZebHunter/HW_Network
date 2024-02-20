from util.charts import *
from util.util import *
def fb2fb_converter(signal):
    groups = []
    cur = ""
    for i, el in enumerate(signal):
        cur += str(el)
        if not ((i + 1) % 4):
            if cur == "0000":
                groups += [1, 1, 1, 1, 0]
            elif cur == "0001":
                groups += [0, 1, 0, 0, 1]
            elif cur == "0010":
                groups += [1, 0, 1, 0, 0]
            elif cur == "0011":
                groups += [1, 0, 1, 0, 1]
            elif cur == "0100":
                groups += [0, 1, 0, 1, 0]
            elif cur == "0101":
                groups += [0, 1, 0, 1, 1]
            elif cur == "0110":
                groups += [0, 1, 1, 1, 0]
            elif cur == "0111":
                groups += [0, 1, 1, 1, 1]
            elif cur == "1000":
                groups += [1, 0, 0, 1, 0]
            elif cur == "1001":
                groups += [1, 0, 0, 1, 1]
            elif cur == "1010":
                groups += [1, 0, 1, 1, 0]
            elif cur == "1011":
                groups += [1, 0, 1, 1, 1]
            elif cur == "1100":
                groups += [1, 1, 0, 1, 0]
            elif cur == "1101":
                groups += [1, 1, 0, 1, 1]
            elif cur == "1110":
                groups += [1, 1, 1, 0, 0]
            elif cur == "1111":
                groups += [1, 1, 1, 0, 1]
            cur = ""
    print(groups)
    print("New size is", len(groups), "Bits")
    print("Redundancy is 25%")
    return groups