from pracmln import MLN, Database
from SCC.predicate import populatePredicates
from SCC.formula import populateFormulas
from SCC.evidence import ThreePointEvidence, FourPointsEvidence
import geopandas as gpd
import os

def main():
    path = os.path.join('Vessel Traffic Data sub-areas April 2020','cts_sub-areas_04_2020_pt','cts_bass_st_04_2020_pt.shp')
    df = gpd.read_file(path)
    mln = MLN()
    populatePredicates(mln)
    populateFormulas(mln)
    mln.write()
    dbs = []
    for i in range(100):
        collection = df.sample(n=3)
        lons = collection['LON'].tolist()
        lats = collection['LAT'].tolist()
        points = list(zip(lons,lats))
        evidence = ThreePointEvidence(*points)
        db = Database(mln)
        evidence.generateEvidence(db)
        dbs.append(db)
    mln.learn(dbs)

if __name__ == '__main__':
    main()


