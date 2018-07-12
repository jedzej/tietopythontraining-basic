access_count = -1


def has_access():
    '''
    let's pretend this function calls some authorization services
    returns True if access is granted and False if not
    access is granted every 3rd time
    '''
    global access_count
    access_count += 1
    if access_count >= 3:
        access_count = 0
    return access_count == 0

