from simulation_engines.cycles import cycles
import numpy as np
import time
'''
#Test1
system = [
    {"name": "Sun",
    "mass": 1.989 * (10**30),
    "pos":np.array([float(0),float(0)]),
    "vel":np.array([float(0),float(0)])
    },
    {"name": "Earth",
    "mass": 5.972 * (10**24),
    "pos":np.array([float(1.496*(10**11)),0.]),
    "vel":np.array([float(0),29800.])
    }
]
'''
'''
#Test2
system = system = [
    {"name": "Sun",
    "mass": 1.989 * (10**30),
    "pos":np.array([float(0),float(0)]),
    "vel":np.array([float(0),float(0)])
    },
    {"name": "Earth",
    "mass": 5.972 * (10**24),
    "pos":np.array([float(1.496*(10**11)),0.]),
    "vel":np.array([float(0),29800.])
    },
    {"name": "Jupiter",
    "mass": 1.898 * (10**27),
    "pos":np.array([float(778.5*(10**9)),0.]),
    "vel":np.array([float(0),13100.])
    }
]
'''
#Test3
system = system = [
    {"name": "Sun",
    "mass": 1.989 * (10**30),
    "pos":np.array([float(0),float(0)]),
    "vel":np.array([float(0),float(0)])
    },
    {"name": "Earth",
    "mass": 5.972 * (10**24),
    "pos":np.array([float(1.496*(10**11)),0.]),
    "vel":np.array([float(0),29800.])
    },
    {"name": "Jupiter",
    "mass": 1.898 * (10**27),
    "pos":np.array([float(778.5*(10**9)),0.]),
    "vel":np.array([float(0),13100.])
    },
    {"name": "Mars",
    "mass": 6.39 * (10**23),
    "pos":np.array([float(227.9*(10**9)),0.]),
    "vel":np.array([float(0),24100.])
    }
]

sim = cycles(system)
while True:
    print(sim.update(3600))