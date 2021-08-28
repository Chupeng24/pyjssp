from pyjssp.simulators import Simulator
import numpy as np
import random
from pyjssp.benchmarks import *

np.random.seed(2)
random.seed(2)

s = FT06()

while True:
    s.transit()

    # s.plot_graph()

    s.flush_trivial_ops()

    g, _, done = s.observe()

    if done:
        print(s.global_time)
        break

