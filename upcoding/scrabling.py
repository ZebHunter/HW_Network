def scramble(signal, v1 = 3, v2 = 5):

	B = []

	for i, a in enumerate(signal):
		line = "B"+str(i)+" = A"+str(i)
		b_first = 0 if i-v1 < 0 else B[i-v1]
		line += (" XOR B"+str(i-v1)) if i-v1 >=0 else ""
		b_second = 0 if i-v2 < 0 else B[i-v2]
		line += (" XOR B"+str(i-v2)) if i-v2 >=0 else ""

		B.append(1 if (a ^ b_first ^ b_second) else 0)
		print(line)
		print()

	maxi = 1
	counter = 1

	for i in range(1, len(B)):
		if(B[i] == B[i-1]):
			counter+=1
		else:
			maxi = max(maxi, counter)
			counter = 1
	maxi = max(maxi, counter)

	print(*B)
	print("New Size is", len(B))
	print("Largest number of repeated characters is", maxi)
	print("Formula : B_i = A_i xor B_{i-"+str(v1)+"} xor B_{i-"+str(v2)+"}")
	return B
