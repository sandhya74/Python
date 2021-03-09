#f=open("demo.txt","a")
#f.write("hi")
#f.close()
#f=open("demo.txt","r")
#print(f.read())
"""
fp = open("demo.txt", "w")
for _ in range(10):
    fp.write("Edureka is a platform for developing market based skills \n")

fp.close()
"""
"""
fp=open("demo.txt","a")
for _ in range(5):
    fp.write("hello\n")
fp.close()    
fp=open("demo.txt","r")
print(fp.read())
 """
#fp=open("mydemo.txt","x")
"""
fp=open("mydemo.txt","w")

fp.write("hi hello")
fp.close()

fp=open("mydemo.txt","r")
print(fp.read())
"""

with open("python.txt","w") as f:
    f.write("i love program")
    f.write("sandhiya")