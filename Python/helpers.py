file_name_prefix = '../Inputs/'

def read_input_at_once(file_name, unit='line'):
    # handle auto name conversion
    if file_name[-3:] == '.py':
        file_name = file_name[:-3] +'.txt'
    
    # open file and return line seperated data points
    with open(file_name_prefix + file_name) as f:
        if unit == 'line':
            return f.readlines()
        if unit == 'char':
            return [[char for char in line] for line in f.readlines()]

def read_input_one_by_one(file_name, unit='line'):
    # handle auto name conversion
    if file_name[-3:] == '.py':
        file_name = file_name[:-3] +'.txt'
    
    # open file and return line seperated data points
    with open(file_name_prefix + file_name) as f:
        if unit == 'line':
            for line in f.readlines():
                yield line
        elif unit == 'char':
            for line in f.readlines():
                for char in line:
                    yield char