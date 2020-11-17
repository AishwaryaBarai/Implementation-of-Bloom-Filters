import random
import sys

no_sets = 7
no_elements = 1000
no_filters = 3
bits = 30000
no_hashes = 7

bloomTable = [[0 for _ in range(bits)] for __ in range(no_filters)]
hashes =[]
for i in range(no_hashes):
	hashes.append(random.randint(1, sys.maxsize))
sets=[]
for i in range(no_sets):
	temp=[]
	for j in range(no_elements):
		temp.append(random.randint(0,sys.maxsize))
	sets.append(temp)


for i in range(1, len(sets) + 1):
    for bit in range(no_filters): 
        if (i >> bit) & 1:
            for element in sets[i-1]:
                for hash in hashes:
                  pos = (element ^ hash) % bits
                  bloomTable[bit][pos] = 1

cnt = 0
for i in range(1, len(sets) + 1):
    for element in sets[i-1]:
        res = 0 
        for bit in range(no_filters):
 
          flag = 0 
          for hash in hashes:
            pos = (element ^ hash) % bits
            if bloomTable[bit][pos] == 1:
              flag+= 1
     
          if flag == 7:
            res |= (1 << bit)
        
        if res == i:
            cnt+= 1

print(cnt)
sys.stdout  =  open("codedbloomTableOutput.txt","w")
print("Lookup Count: %d" %cnt)
sys.stdout.close()



