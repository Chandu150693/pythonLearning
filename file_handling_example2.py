# if the file is in w mode all the file contents will replace with the new text
# f = open("demofile.txt", "a")
#
# f.write("\nNow the file has more content")
#
# f.close()
#
# fo = open("demofile.txt", "r")
# print(fo.read())
#
# f = open("demofile3.txt", "a")
# f.close()
import os

# To delete the files
# os.remove("demofile3.txt")

# To delete directory if directory is not present then it will through error
os.rmdir("remove_dir")
