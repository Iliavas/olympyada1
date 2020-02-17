from math import sqrt

def search(ks, bs):
	for i in range(len(ks)):
		for j in range(len(bs)):
			try:
				if ks[i] == bs[j]: 
					del ks[i]
					del bs[j]
					truer.append(True)
				else: truer.append(False)
			except: search(ks, bs)
	if not len(ks): return True
	else: False

def dist(x1, x2):
	return sqrt(x1 ** 2 + x2 **2)

def normalise(*args):
	d = []
	for i in range(len(args), 2):
		d.append(dist(args[i], args[i - 1]))
	m = 0
	for amount, at in enumerate(range(len(d))):
		if at > m:
			m = amount
	mx = args[m * 2]
	my = args[m * 2 - 1]
	normalise_l = []
	for i in range(len(args)):
		if i % 2 == 0 or i == 0: 
			normalise_l.append(args[i] - mx) 
		else: 
			normalise_l.append(args[i] - my)
	return normalise_l

def is_line(x1, y1, x2, y2, x3, y3, x4, y4):
	if x1 == x2 == x3 == x4: return 2
	if y1 == y2 == y3 == y4: return 2
	if y1 == y2 == y3 or y1 == y2 == y4 or y1 == y3 == y4 or y2 == y3 == y4: return 3
	n = normalise(x1, y1, x2, y2, x3, y3, x4, y4)
	k, b, k1, b1, k2, b2, k3, b3, k4, b4, k5, b5, k6, b6 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	try:
		k = (n[1] - n[3])/(n[0] - n[2])
		b = (n[0] * n[3] + n[1] * n[2]) / (n[0] + n[2])
		
	except ZeroDivisionError:
		pass
	else:
		if n[4] * k + b == float(n[5]) and n[6] * k + b == float(n[7]):
			return 2
	try:
		n_l = normalise(x1, y1, x2, y2)
		k1 = float((n_l[1] - n_l[3])/(n_l[0] - n_l[2]))
		b1 = (n_l[0] * n_l[3] + n_l[1] * n_l[2]) / (n_l[0] + n_l[2])
	except ZeroDivisionError:
		pass

	n_l = normalise(x2, y2, x3, y3)
	try:
		k2 = float((n_l[1] - n_l[3])/(n_l[0] - n_l[2]))
		b2 = (n_l[0] * n_l[3] + n_l[1] * n_l[2]) / (n_l[0] + n_l[2])
	except ZeroDivisionError:
		pass
	n_l = normalise(x3, y3, x4, y4)
	try:
		k3 = float((n_l[1] - n_l[3])/(n_l[0] - n_l[2]))
		b3 = (n_l[0] * n_l[3] + n_l[1] * n_l[2]) / (n_l[0] + n_l[2])
	except ZeroDivisionError:
		pass
	n_l = normalise(x1, y1, x3, y3)
	try:
		k4 = float((n_l[1] - n_l[3])/(n_l[0] - n_l[2]))
		b4 = (n_l[0] * n_l[3] + n_l[1] * n_l[2]) / (n_l[0] + n_l[2])
	except ZeroDivisionError:
		pass
	n_l = normalise(x1, y1, x4, y4)
	try:
		k5 = float((n_l[1] - n_l[3])/(n_l[0] - n_l[2]))
		b5 = (n_l[0] * n_l[3] + n_l[1] * n_l[2]) / (n_l[0] + n_l[2])
	except: pass
	n_l = normalise(x2, y2, x4, y4)
	try:
		k6 = float((n_l[1] - n_l[3])/(n_l[0] - n_l[2]))
		b6 = (n_l[0] * n_l[3] + n_l[1] * n_l[2]) / (n_l[0] + n_l[2])
	except ZeroDivisionError:
		pass
	except ZeroDivisionError:
		pass
	ks = [k1, k2, k3, k4, k5, k6]
	bs = [b1, b2, b3, b4, b5, b6]
	a = search(ks, bs)
	counter = 0
	for i in ks:
		if i != 0: counter += 1
	if (k1 == k2 or k1 == k3 or k2 == k3) and ((counter != 2) or a):
		return 3
	else: return 4   
#print(is_line(*list(map(lambda x: int(x), input().split()))))
