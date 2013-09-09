def main():
	a = [8, 5, 1, 38, 4, 2, 9, 75, 6, 16, 3, 8, 10]
	b = [0] * len(a)

	for i in xrange(0,len(a)):
		cur_max = 0
		for j in xrange(0, i):
			if a[j] < a[i] and cur_max < b[j]:
				cur_max = b[j]
		b[i] = cur_max + 1

	print b
	print max(b)

if __name__ == '__main__':
	main()