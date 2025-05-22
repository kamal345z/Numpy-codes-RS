

import numpy as np
checkboard = (np.indices((8,8)).sum(axis=0) % 2)
print(checkboard)