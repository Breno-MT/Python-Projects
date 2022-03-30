############################# delete a file
import os
import shutil
path = "new_folder"

try:
    #os.remove(path) #// remove some file
    #os.rmdir(path) # remove directory
    shutil.rmtree(path) # now we can delete folder that contains files!! BEWARE, ITS DANGEROUS!
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You don't have permission to delete that!")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")
