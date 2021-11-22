import sys
sys.path.append('.')

import robrank as rr
rr.cmdline.AdvRank(sys.argv[1:])
