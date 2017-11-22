
# Just in case your input data has duplicates this will clean out the final results so you only get
# one domain name line

gFile = open("good.txt","r")
gURLS = dict()
for g in gFile:
	if g in gURLS.keys():
		pass
	else:
		gURLS[g] = 1
gFile.close()

gFile = open("good.txt","w")
for g in gURLS.keys():
	gFile.write(g)
gFile.close()
		
bFile = open("bad.txt","r")
bURLS = dict()
for b in bFile:
	if b in bURLS.keys():
		pass
	else:
		bURLS[b] = 1
bFile.close()

bFile = open("bad.txt","w")
for b in bURLS.keys():
	bFile.write(b)
bFile.close()
