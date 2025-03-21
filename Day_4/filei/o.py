#file handaling
import os
file=open("C:\\Users\\nadiy\\Downloads\\sample3.txt", "r")
print(file.read())
file.close()

import os
file=open("C:\\Users\\nadiy\\Downloads\\sample3.txt", "r")
print(file.read(7))
file.close()

import os
file=open("C:\\Users\\nadiy\\Downloads\\sample3.txt", "r")
print(file.readlines())
file.close()

# write 
import os
file=open("C:\\Users\\nadiy\\Downloads\\sample3.txt", "w")
file.write("hai,hello\n")
file.write("holi is filled with colors\n")
file.close()


#remove
os.remove("C:\\Users\\nadiy\\Downloads\\sample3.txt")

#conditions
import os
if os.path.exists("C:\\Users\\nadiy\\Downloads\\sample3.txt"):
    os.remove("C:\\Users\\nadiy\\Downloads\\sample3.txt")
else:
    print("file not exists")