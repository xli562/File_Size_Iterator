import os


def get_size(path = '.'):
    '''
    I would expect PermissionError for whole C:/ scans,
    since the function needs to access every sub-folder.
    But apparantly, it does not have PermissionError problems. '''
    total_size = 0
    if os.path.isdir(path)
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
    else:
        total_size = os.path.getsize(path)

    return total_size

def find_largest_files(path:str = '.', n:int = 3, iters:int = 3):
    '''Finds the n largest files under a specific directory for i iterations. 
    Marks other files or directories as "Others".'''
    # alternative: only list files greater than 30% of the total size of the parent directory?
    for iter in iters:

    
