import shutil
images_folder = '/home/pi/Documents/OTIS-2U-Repo/images/'
archived_folder = '/home/pi/Documents/OTIS-2U-Repo/archived/'

shutil.rmtree(images_folder, ignore_errors=False, onerror=None)
shutil.rmtree(archived_folder, ignore_errors=False, onerror=None)