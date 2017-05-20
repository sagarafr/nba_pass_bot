def get_info(taken_by_info):
    info = ''
    if 'username' in taken_by_info:
        info = taken_by_info['username']
    if info == '' and 'first_name' in taken_by_info:
        info = taken_by_info['first_name']
    if info == '' and 'last_name' in taken_by_info:
        info = taken_by_info['last_name']

    return info
