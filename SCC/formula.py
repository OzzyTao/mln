from .predicate import Predicate, PREDICATE_TYPES
class Formula:
    def __init__(self,leftExpression,connector,rightExpression, weight=None):
        self.leftExpression = leftExpression
        self.connector = connector
        self.rightExpression = rightExpression
        self.weight = weight

    def __str__(self):
        string = self.leftExpression + self.connector+self.rightExpression
        if self.weight is None:
            return string+'.'
        else:
            return str(self.weight)+' '+string

class UnaryFormula(Formula):
    def __init__(self, predicate1, connector, predicate2,weight=None):
        super(UnaryFormula,self).__init__(str(predicate1),connector,str(predicate2),weight)

class BinaryFormula(Formula):
    def __init__(self, predicate1, operator, predicate2, connector, predicate3,weight=None):
        super(BinaryFormula,self).__init__(str(predicate1) + operator + str(predicate2),connector,str(predicate3),weight)

def populateFormulas(mln):
    # unary formulas
    args1 = ['a','b','c']
    args2 = ['b','a','c']
    combines = [[0,4,None],
                [1,5,None],
                [2,5,None],
                [3,5,0.0],
                [3,6,0.0],
                [3,7,0.0],
                [4,0,None],
                [5,1,0.0],
                [5,2,0.0],
                [5,3,0.0],
                [6,3,None],
                [7,3,None],
                [4,4,None]]
    for i1,i2,w in combines:
        p1 = Predicate(PREDICATE_TYPES[i1],args1)
        p2 = Predicate(PREDICATE_TYPES[i2],args2)
        formula = UnaryFormula(p1,'=>',p2,w)
        mln << str(formula)
    # binary formulas/Inferences
    args1 = ['a','b','c']
    args2 = ['b','c','d']
    args3 = ['a','b','d']
    for i in PREDICATE_TYPES:
        p1 = Predicate(i,args1)
        for j in PREDICATE_TYPES:
            p2 = Predicate(j,args2)
            for k in PREDICATE_TYPES:
                p3 = Predicate(k,args3)
                formula = BinaryFormula(p1,'^',p2,'=>',p3, 0.0)
                mln << str(formula)


