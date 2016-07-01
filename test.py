
#file_path = "iConference_edited/iConf2015.txt"
import os

print(os.getcwd())
os.chdir("..")
print(os.getcwd())


with open("iConference_edited/iConf2008t.txt", "r") as f:
    file = list(f)[:10]
file[0] = "  \n"
print(file)


for item in file:
    item = item.strip()

print(file)

