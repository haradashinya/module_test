import os
import sys

# It happens error!
# import a
a_dir = os.path.join(os.path.abspath(""),"a")
sys.path.append(a_dir)

# It works!
import hello


# I'm looking for alternative way.



