#! python3
# backupToTarBzip2.py - Copies an entire folder and its contents into a .tar.bz2 ball whose filename increments.
import tarfile, os

target = input('Please write path to folder/directory you want to backup into a .tar.bz2 file: ')

def backupToTarBz2(folder):
    # Backup the entire contents of "folder" into a .tar.bz2 file.

    folder = os.path.abspath(folder) # make sure folder is absolute

    # Figure out the filename this code should use based on what files already exist.
    number = 1
    while True:
        tarFilename = os.path.basename(folder) + '_' + str(number) + '.tar.bz2'
        if not os.path.exists(tarFilename):
            break
        number = number + 1

    # Create the tarball
    print('Creating {}...' .format(tarFilename))
    backupTar = tarfile.open(tarFilename, 'w:bz2')

    backupTar.add(folder)
    backupTar.close()

    print('Done.')

backupToTarBz2(target)
