def dict_data(row, headers):
    """
    Create dict data from list header and row
    """
    data = {}
    for i in range(len(row)):
        data[headers[i]] = row[i]
    return data
