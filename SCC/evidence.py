import numpy as np
import itertools
from .predicate import PREDICATE_TYPES,Predicate
def locationsToPredicate(point1,point2,point3):
    vec1 = [point2[0]-point1[0],point2[1]-point1[1]]
    vec2 = [point3[0]-point2[0],point3[1]-point2[1]]
    unit_vec1 = vec1/np.linalg.norm(vec1)
    unit_vec2 = vec2/np.linalg.norm(vec2)
    dot = np.dot(unit_vec1,unit_vec2)
    det = unit_vec1[0]*unit_vec2[1]-unit_vec1[1]*unit_vec2[0]
    angle = np.arctan2(det,dot)
    if angle == 0:
        return 0
    elif angle< np.pi/2:
        return 1
    elif angle == np.pi/2:
        return 2
    elif angle < np.pi:
        return 3
    elif angle == np.pi:
        return 4
    elif angle < np.pi*3/2:
        return 5
    elif angle == np.pi*3/2:
        return 6
    else:
        return 7

class ThreePointEvidence:
    def __init__(self,point1,point2,point3):
        self.p1 = point1
        self.p2 = point2
        self.p3 = point3

    def generateEvidence(self,database):
        points = {'p1':self.p1,'p2':self.p2,'p3':self.p3}
        for i, j, k in itertools.permutations(['p1','p2','p3']):
            p = locationsToPredicate(points[i],points[j],points[k])
            p = Predicate(PREDICATE_TYPES[p],[i,j,k])
            database << str(p)

class FourPointsEvidence:
    def __init__(self,p1,p2,p3,p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
    def generateEvidence(self,db):
        points = {'p1':self.p1,'p2':self.p2,'p3':self.p3,'p4':self.p4}
        p = locationsToPredicate(points['p1'],points['p2'],points['p3'])
        p = Predicate(PREDICATE_TYPES[p],['p1','p2','p3'])
        db << str(p)
        p = locationsToPredicate(points['p2'],points['p3'],points['p4'])
        p = Predicate(PREDICATE_TYPES[p],['p2','p3','p4'])
        db << str(p)
        p = locationsToPredicate(points['p1'],points['p2'],points['p4'])
        p = Predicate(PREDICATE_TYPES[p],['p1','p2','p4'])
        db << str(p)




