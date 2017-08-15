s = "light luma illumination illuminator illuminate glow ray beam flare LED  "

from itertools import product
l = s.split()
r='\n'.join(''.join(k*v for k,v in zip(l, x))
           for x in product(range(2), repeat=len(l))
           if sum(x) > 1)
print r
