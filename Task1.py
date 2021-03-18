def File():
    #str="Training  march batch"
    #print(str)
    names=[]
    filename="Employee.txt"
    with open(filename) as f:
        for line in f:
            names.append(line.strip())
            #print(line)
    names.sort()
    temp=0
    for temp in names:
        print("%s: is Tranining  Employee"%(temp))
    #print(names)
    filename="sorted.txt"
    with open(filename,"w") as fp:
        for x in names:
            fp.write(x+'\n')
    #print("Tranining batch Employee %s" % x)
File()         

