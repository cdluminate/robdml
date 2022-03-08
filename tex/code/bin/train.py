import sys
sys.path.append('.')

import robrank as rr
rr.cmdline.Train(sys.argv[1:])
