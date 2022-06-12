f = open('D:/Dora/mashup/python/file.txt','w')
name = ["Gopika","Nikhil","Gokul"]
for item in name:
    f.write("%s\n" %item)
print("done")