import random
import sys

def lookup(set):
	cnt=0
	for i in set:
		hashcnt=0
		for j in hashes:
			temp=(i^j)%bits
			if bloomfilterTable[temp]==1:
				hashcnt+=1
		if hashcnt==7:
			cnt+=1
	return cnt	

no_hashes=7
no_elements=1000
bits=10000
bloomfilterTable = bits*[0]
A=[]
for i in range(no_elements):
	A.append(random.randint(1, sys.maxsize))
hashes = []
for i in range(no_hashes):
	hashes.append(random.randint(1, sys.maxsize))
cnt1 = 0
cnt2 = 0

#insert
for i in A:
	flag=0
	for j in hashes:
		temp = (i^j)%bits
		if bloomfilterTable[temp]==0:
			bloomfilterTable[temp]=1

B = []
for i in range(no_elements):
	B.append(random.randint(1, sys.maxsize))
cnt1=lookup(A)
cnt2=lookup(B)

print(cnt1)
print(cnt2)

sys.stdout = open("normalBloomFilterOutput.txt","w")
print("Number of Lookup in A: %d" %cnt1)
print("\nNumber of Lookup in B: %d" %cnt2)
sys.stdout.close()