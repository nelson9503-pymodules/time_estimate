# time_estimate

Calculate time estimate for a progress.

## Quick Start

```python
import time_estimate

timer = time_estimate.TimeEstimate()
for i in range(1, 301):
    hour, minute, second = timer.estimate(i, 300)
    print("time estimate: {:02d}:{02d}:{02d}".format(hour, minute, second))
```