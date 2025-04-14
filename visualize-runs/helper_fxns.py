import numpy as np
import glob


def make_yearlist_AMOC(yrst, yrend, tr,
                  resultsdir = '/gpfs/home/mep22dku/scratch/TiMBER-runsets/visualize-runs/data/'):
   
    yrs = np.arange(yrst,yrend+1,1)
    ylist = []
    for i in range(0,len(yrs)):
        yr = yrs[i]
        ty = f'{resultsdir}/{tr}_{yr}-AMOC.nc'
        #print(ty)
        t2 = glob.glob(ty)
        #print(t2)
        ylist.append(t2[0])
    return ylist

