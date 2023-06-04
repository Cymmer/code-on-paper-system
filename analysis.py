
import re
import Levenshtein

def remove_comments(code):
    pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
    regex = re.compile(pattern, re.MULTILINE | re.DOTALL)

    def _replacer(match):
        if match.group(2) is not None:
            return ""
        else:
            return match.group(1)

    return regex.sub(_replacer, code)


def minify_c_code(code):
    # Remove comments
    code = remove_comments(code)

    # Remove extra whitespaces and newlines
    code = re.sub(r"\s+", " ", code)

    # Remove spaces around punctuation
    code = re.sub(r"\s*([\(\){};=<>!+-/*&|^%~])\s*", r"\1", code)

    return code

def string_similarity(string1, string2):
    distance = Levenshtein.distance(string1, string2)
    return (1 - (distance / max(len(string1), len(string2)))) * 100