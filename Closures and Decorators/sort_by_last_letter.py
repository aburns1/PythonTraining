store = []


def sort_by_last_letter(strings):
    def last_letter(s):             # local function
        return s[-1]
    store.append(last_letter)       # the local function is created as a new function each time the parent is called.
    print(last_letter)
    return sorted(strings, key=last_letter)
