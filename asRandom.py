import numpy as np
import random

mean = 0
stander_div= 1
smaple_size = 100

ans = np.random.normal(mean, stander_div, smaple_size)

int  = np.round(ans).astype(int)

print(ans[0])

smaple_mean = np.mean(int)
smaple_variance = np.var(int)

print(smaple_mean)
print(smaple_variance)

