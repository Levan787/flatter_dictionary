from dictionary import ugly_dictionary
from pprint import pprint


def flatter_dictionary(my_dict):
    pretty_dictionary = {}
    for key, value in my_dict.items():
        if key == 'actions':
            for actions in value:
                dict_to_list = list(actions.values())
                pretty_dict_key = dict_to_list[0]
                pretty_dict_value = dict_to_list[1]
                pretty_dictionary[pretty_dict_key] = pretty_dict_value

        else:
            pretty_dictionary[key] = value
    return pretty_dictionary


pprint(flatter_dictionary(ugly_dictionary))
