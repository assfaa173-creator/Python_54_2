import re


def is_valid_id(oder_id ):
    return bool (re.search("^oORD-...$",oder_id))
print(is_valid_id("oORD-123"))
print(is_valid_id("oORD-12"))
print(is_valid_id("oORD-123"))


