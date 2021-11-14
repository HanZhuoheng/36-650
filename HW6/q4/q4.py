def delete_keys(keys, dictionary):
    for k in keys:
        dictionary.pop(k)
    return dictionary  