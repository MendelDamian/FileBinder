from FileBinder.SkipFiles import SkipFiles
import os

# TODO categories management
categories = {'Documents': ['.doc', '.docx', '.txt', '.pdf'], 
              'Photos': ['.jpg', '.png', '.raw'], 
              'Archives': ['.zip', '.rar', '.tar'], 
              'Music': ['.mp3', '.flac'], 
              'Videos': ['.mp4'],
              'Applications': ['.exe']}


def scan_files(path, skip=set()):
    files = set()
    for file in os.listdir(path):
        if set([file]).difference(skip).difference(set(categories.keys())):
            files.add(os.path.join(path, file))
    return files
