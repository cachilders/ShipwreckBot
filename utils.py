def csv_to_dict(filename):
    fid = open(filename)
    lines = fid.readlines()

    keys = lines[0].rstrip('\n').split(',')
    out = list(
        map(lambda l: dict(zip(keys, l.rstrip('\n').split(','))), lines[1:]))
    return out
