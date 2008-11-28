from __future__ import with_statement
import pickle

l = []
with open("scores.dat",'w') as f:
    pickle.dump(l,f)
