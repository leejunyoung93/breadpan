import os
import sys

# Add parent path to import back-end pkg modules. 
# current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parent_dir = os.path.dirname(current_dir)
# parent_dir = os.path.dirname(parent_dir)
# sys.path.insert(0, parent_dir) 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import breadpan
import todo
