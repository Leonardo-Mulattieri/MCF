import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.append('../../accessori/L05')

import esercizio2_funz

rwN     = 1000
rw_step = 1

#esercizio2_funz.random_walk_5p(rw_step , rwN)
esercizio2_funz.random_walk_pAB(rw_step , rwN)
