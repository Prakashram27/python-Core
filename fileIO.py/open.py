# f.open(...)
# work with a File
# f.close() #if you dont close you can loose data


def read_series(filename):
    with open(filename,mode='rt', encoding='utf-8') as f:
        return [int(line.strip()) for line in f]
    


# with EXPR as VAR:
#     Block

