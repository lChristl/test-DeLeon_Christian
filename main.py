import os
import shutil

list_of_files = os.listdir()
print(list_of_files)




img = 0
doc = 0
vid = 0
other = 0


# if os.path.exists("img"):
    
# os.mkdir("img")
# os.mkdir("doc")
# os.mkdir("vid")
# os.mkdir("other")

filename = input("enter file: ")
if os.path.exists(filename):
    print("it exists")

else:
    print("it does not exist")



for filename in os.listdir("."):
    if filename.endswith(".txt"):
        os.rename(filename, os.path.join("doc", filename))
        print(f"Moved: {filename} -> doc/")
    elif filename.endswith(".pptx"):
        os.rename(filename, os.path.join("doc", filename))
        print(f"Moved: {filename} -> doc/")
    elif filename.endswith(".png"):
        os.rename(filename, os.path.join("img", filename))
        print(f"Moved: {filename} -> img/")
    elif filename.endswith(".jpeg"):
        os.rename(filename, os.path.join("img", filename))
        print(f"Moved: {filename} -> img/")
    elif filename.endswith(".mp4"):
        os.rename(filename, os.path.join("vid", filename))
        print(f"Moved: {filename} -> vid/")
    elif filename.endswith(".mov"):
        os.rename(filename, os.path.join("vid", filename))
        print(f"Moved: {filename} -> vid/")


