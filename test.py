

import pyusng

data = [
    ['15R YP 7962',30.364557,-90.093907],
    ['16R BU 3046',30.220759,-89.802346],
    ['03W VN 3638',65.264601,-166.362221],
    ['17T KJ 6010',43.413205,-83.960652],
    ['16T GP 4018',43.484461,-84.024213],
    ['19Q GV 5091',17.994984,-66.634049]
]

for itm in data:
    print("=============")
    print(itm)
    a = pyusng.LLtoUSNG(itm[1], itm[2], 6)
    ab = pyusng.LLtoUSNG(itm[1], itm[2], 2)
    print(a)
    print(ab)

    b = pyusng.USNGtoLL(itm[0])
    print(b)

    c = pyusng.USNGtoLL(a)
    print(c)

    # TODO: fix reverse conversions
    d = pyusng.USNGtoUTM(itm[0])
    print(d)

