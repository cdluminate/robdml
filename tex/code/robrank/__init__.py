
from . import utils
from . import configs
from . import datasets
from . import models
from . import losses
from . import attacks
from . import defenses
from . import cmdline
import rich.traceback
rich.traceback.install()

r'''
Naming conventions for `robrank.models` and `robrank.configs`

```
<task><backbone><modifier>
```

* `task` in {c, r, h} for classification, ranking, hybrid
* `backbone` e.g. lenet, res18, mnas10
* `moddifier` in {, d, e, p} for vanilla, advrank:defense, ses, and pnp defenses

For example

* `cc2f2` stands for classification, c2f2
* `rc2f2` stands for ranking, c2f2
* `rc2f2d` stands for ranking, c2f2, with advrank:defense (EST)
'''
