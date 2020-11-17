import random
import sys


def remove():
	for i in range(500):
		flow=A[i]
		for j in hashes:
			temp=(flow^j)%bits
			if bloomFilter[temp]>0:
				bloomFilter[temp]-=1

def add():
	for i in new:
		for j in hashes:
			temp = (i^j) % bits
			bloomFilter[temp]+=1

no_hashes=7
no_elements=1000
bits=10000
bloomFilter = bits*[0]
A=[]
for i in range(no_elements):
	A.append(random.randint(1, sys.maxsize))
hashes=[]
for i in range(no_hashes):
	hashes.append(random.randint(1, sys.maxsize))

cnt = 0

for i in A:
	for j in hashes:
		temp = (i^j) % bits
		bloomFilter[temp]+=1

remove()

new = []
for i in range(500):
	new.append(random.randint(1, sys.maxsize) )

add()

for i in A:
	mincnt=float("inf")
	flag=0
	for j in hashes:
		hashVal=(i^j) % bits
		if bloomFilter[hashVal]>0:
			flag+=1
		mincnt=min(mincnt,bloomFilter[hashVal])
	if flag==no_hashes:
		cnt+=mincnt

print(cnt)

sys.stdout = open("countingBloomFilterOutput.txt","w")
print("Lookup Count: %d" %cnt)
sys.stdout.close()
