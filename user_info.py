"""global variant
USERNAME
PART
EMAIL
PARTS
usage: user_info.get_value('USERNAME')
"""


def _init():
    global _global_dict
    _global_dict = {}

def set_value(key,value):
    _global_dict[key] = value


def get_value(key):
    return _global_dict.get(key, None)

