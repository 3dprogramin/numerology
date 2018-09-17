#!/usr/bin/python2.7

import sys

class Numerology:
    def __init__(self, s):
        self._s = s
        self._l = list(self._s.replace(' ', '').strip().lower())
        self._dicts = {
            'pythagorean': {
                'a': 1,
                'b': 2,
                'c': 3,
                'd': 4,
                'e': 5,
                'f': 6,
                'g': 7,
                'h': 8,
                'i': 9,
                'j': 1,
                'k': 2,
                'l': 3,
                'm': 4,
                'n': 5,
                'o': 6,
                'p': 7,
                'q': 8,
                'r': 9,
                's': 1,
                't': 2,
                'u': 3,
                'v': 4,
                'w': 5,
                'x': 6,
                'y': 7,
                'z': 8
            }
        }
    def pythagorean(self):
        d = self._dicts['pythagorean']
        s = ''
        k = 0
        for c in self._l:
            i = d[c]
            s += str(i)
            k += i
        return {
            'sum': k,
            'string': s
        }

def main():
    a = sys.argv
    if (len(a) < 2):
        print ('Usage: ./numerology.py billgates')
        return
    n = Numerology(sys.argv[-1])
    r = n.pythagorean()
    print ('Pythagorean: {}'.format(r['sum']))

if __name__ == "__main__":
    main()
