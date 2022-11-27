import os
import time

#function variant for absolute path.
#absolute path to folder to clear from
dir_path = ""
#No of days before which the files are to be deleted
limit_days = 0

treshold = time.time() - limit_days*86400
entries = os.listdir(dir_path)
for dir in entries:
    creation_time = os.stat(os.path.join(dir_path,dir)).st_ctime
    if creation_time < treshold:
        print(f"{dir} was created on {time.ctime(creation_time)} and will be deleted")
        #absolute path to dir to clear from
        os.remove(f"C:/Users/Maciej Winiarski/old_files/new DIR/{dir}")

#function variant for relative path
#No of days before which the files are to be deleted

# limit_days = 0
# treshold = time.time() - limit_days*86400
# entries = os.listdir()
# for dir in entries:
#     creation_time = os.stat(dir).st_ctime
#     if (creation_time < treshold) and dir != "script.py":
#         print(f"{dir} was created on {time.ctime(creation_time)} and will be deleted")
#         os.remove(dir)