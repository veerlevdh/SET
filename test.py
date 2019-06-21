#!/usr/bin/env python3

import time

a = True
ts = int(time.time())

while a == True:
    ts2 = int(time.time())
    print(ts2-ts)
    if (ts2-ts) > 30:
        a = False 


