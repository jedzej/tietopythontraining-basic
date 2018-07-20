access_count = -1


def has_access():

    global access_count
    access_count += 1
    if access_count >= 3:
        access_count = 0

    return access_count == 0
