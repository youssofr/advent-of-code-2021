file_name_prefix = '../Inputs/'

def read_input_at_once(file_name):
    # handle auto name conversion
    if file_name[-3:] == '.py':
        file_name = file_name[:-3] +'.txt'
    
    # open file and return line seperated data points
    with open(file_name_prefix + file_name) as f:
        return f.readlines()

def read_input_one_by_one(file_name):
    # handle auto name conversion
    if file_name[-3:] == '.py':
        file_name = file_name[:-3] +'.txt'
    
    # open file and return line seperated data points
    with open(file_name_prefix + file_name) as f:
        for line in f.readlines():
            yield line