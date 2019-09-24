def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)


@escape_unicode
def northern_city():
    return 'Tromsø'
