def raise_to(exp):
    """ 'exp' will be kept as a closure and this will be useful for generating functions such as square() and cube() """
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp
