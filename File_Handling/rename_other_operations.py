# # rename file anme

# import os

# if os.path.exists("next.txt"):
#     os.rename("next.txt", "new_n.txt")
#     print("file renamed.")
# else:
#     print("file dose not exists.")


# # delete empty directory

# import os

# if os.path.exists("folder_a"):
#     os.rmdir("folder_a")
#     print("deleted directory.")
# else:
#     print("directory dose not exists.")


# Deleting a directory when  its haveing contents

import os
import shutil

if os.path.exists("new_fold"):
    shutil.rmtree("new_fold")
    print("Directory and its content deleted.")
else:
    print("Can't delete this Directory/subdirectory or its files.")
