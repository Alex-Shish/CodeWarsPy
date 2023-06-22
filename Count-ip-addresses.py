# Count IP Addresses
"""Implement a function that receives two IPv4 addresses, and returns the number of addresses between them
(including the first one, excluding the last one).
All inputs will be valid IPv4 addresses in the form of strings.
The last address will always be greater than the first one.

Examples
* With input "10.0.0.0", "10.0.0.50"  => return   50
* With input "10.0.0.0", "10.0.1.0"   => return  256
* With input "20.0.0.10", "20.0.1.0"  => return  246"""

def ips_between(start, end):
    sm = 0
    st = start.split(".")
    stn = [int(x) for x in st]
    fn = end.split(".")
    fnn = [int(x) for x in fn]
    i = 3
    while i >= 0:
        sm += 256 ** (3 - i) * (fnn[i] - stn[i])
        i -= 1
    return sm
print(ips_between("10.0.0.0", "10.0.0.50"))
print(ips_between("10.0.0.0", "10.0.1.0"))
print(ips_between("20.0.0.10", "20.0.1.0"))