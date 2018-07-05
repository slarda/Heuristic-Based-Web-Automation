import re

def normalize_text(text):
    # ToDo Proper normalization
    return text.lower()\
        .replace('-', ' ') \
        .replace('_', ' ') \
        .replace('  ', ' ')


def check_text(text, contains, not_contains, normalize=True):
    if not contains:
        contains = []

    if not not_contains:
        not_contains = []

    if normalize:
        text = normalize_text(text)

    has_searched = False
    for str in contains:
        if re.search(str, text):
            has_searched = True
            break

    if not has_searched:
        return False

    has_forbidden = False
    for str in not_contains:
        if re.search(str, text):
            has_forbidden = True
            break

    return not has_forbidden


def check_if_empty_cart(text):
    contains = ['cart is empty', 
                'no .*in .*cart',
                'zero products in .*cart', 
                'nothing in.* cart', 
                'empty cart',
                '0 items',
                'zero items'
               ]
    
    return check_text(text, contains, [])
