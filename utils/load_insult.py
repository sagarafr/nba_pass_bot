from os.path import isfile


def load_insult(insult_file: str):
    r_list = []
    if isfile(insult_file):
        with open(insult_file, 'r') as fd_file:
            line = fd_file.readline()
            if line != '':
                r_list.append(line)
    else:
        open(insult_file, 'a').close()
    return r_list
