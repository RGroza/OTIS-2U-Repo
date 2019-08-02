import os, shutil
images_folder = '/home/pi/Documents/OTIS-2U-Repo/images/'
archived_folder = '/home/pi/Documents/OTIS-2U-Repo/archived/'

folders = []
folders.append(images_folder)
folders.append(archived_folder)

for folder in folders:
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)

#shutil.rmtree(images_folder, ignore_errors=False, onerror=None)
#shutil.rmtree(archived_folder, ignore_errors=False, onerror=None)