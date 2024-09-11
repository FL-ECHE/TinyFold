#! /usr/bin/env python3

import numpy as np

class DistMap():
    def __init__(self,matrix,thresh_dist,thresh_iter):
        #square matrix corresponding to correctly indexed residue pairs
        self.dm = matrix
        self.tdist = thresh_dist
        self.titer = thresh_iter

        #to implement later
        #self.noise = noise_type

        self.skipid = []
        self.coords = np.matrix([[0.,0.,0.] for i in range(len(matrix[0]))])
        self.rng = np.random.default_rng()
    
    def distance(self,a, b):
        return np.linalg.norm(a-b)

    def apply_t(self,a,b):
        return np.add(a,b)

    def generate(self):
        for i in range(self.titer):
            idx1 = int(self.rng.integers(low=0,high=len(self.dm[0]), size=1))
            idx2 = int(self.rng.integers(low=0,high=len(self.dm[0]), size=1))
            if idx1 == idx2 :
                continue
            bestdist = 10000
            trans =np.array([0,0,0])
            if idx1 in self.skipid: #2nd resid as well?
                continue
            for j in range(3):
                temptrans = self.rng.standard_normal(3)
                pos1 = self.apply_t(self.coords[idx1],temptrans) #apply translation
                pos2 = self.coords[idx2]
                dist = self.distance(pos1,pos2)
                if dist < bestdist:
                    bestdist = dist
                    trans = pos1
            self.coords[idx1] = trans

            if (dist < self.dm[idx1,idx2] + self.tdist) and (dist > self.dm[idx1,idx2] - self.tdist):
                self.skipid.append(idx1)
                self.skipid.append(idx2)
        
        return self.coords
