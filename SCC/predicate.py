PREDICATE_TYPES = ['zero','one','two','three','four','five','six','seven']

class Predicate:
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments

    def __str__(self):
        return "{}({})".format(self.name,','.join(self.arguments))

def populatePredicates(mln):
    args = ['point','point','point']
    for p in PREDICATE_TYPES:
        predicate = Predicate(p,args)
        mln << str(predicate)

