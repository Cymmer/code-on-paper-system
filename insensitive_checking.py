import re

def _remove_new_lines(code):
    return code.replace('\r', '').replace('\n', '')

def _remove_spaces(code):
    return code.replace(" ", "")

def _convert_all_to_lowercase(code):
    return code.lower()

def _clean_symbols(code):
    result = []
    # Split the string into alphanumeric substrings and symbols
    for substr in re.findall(r'\w+|[^\w\s]', code):
        # If the substring contains a digit, add it as is
        if re.search(r'\d', substr):
            result.append(substr)
        # If the substring is a period and the previous and next characters are digits, add it as is
        elif substr == '.' and re.search(r'\d', code[code.index(substr)-1:code.index(substr)]) and re.search(r'\d', code[code.index(substr)+1:code.index(substr)+2]):
            result.append(substr)
        # Otherwise, remove all symbols and add the alphanumeric characters
        else:
            result.append(re.sub(r'[^\w]', '', substr))

    # Join the substrings together into a new string
    result_string = ''.join(result)

    return result_string

def insensitive_checking_preprocessing(code):
    code = _clean_symbols(code)
    code = _remove_new_lines(code)
    code = _remove_spaces(code)
    code = _convert_all_to_lowercase(code)
    return code