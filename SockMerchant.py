import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(number, a):
    count = 0
    a.sort()
    a.append('#')
    i = 0
    while i<number:
        if a[i]==a[i+1]:
            count = count+1
            i+=2
        else:
            i+=1
    return count
