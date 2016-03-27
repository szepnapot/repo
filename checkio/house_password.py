import re

analyze = re.compile('(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{10,}')
def checkio(data):
    if re.search(analyze,data):
        return True
    else:
        return False
