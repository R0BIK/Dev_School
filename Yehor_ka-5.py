def get_root_property(dictionary, number):
    for key, value in dictionary.items():
        if isinstance(value, list):
            if number in value:
                return(key)
        elif get_root_property(value, number):
            return(key)