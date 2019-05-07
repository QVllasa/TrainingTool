import glob
import os

for i in glob.glob('files/new_version/*.docx'):
    os.remove(i)