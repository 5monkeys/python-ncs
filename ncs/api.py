from collections import namedtuple

import ncs.db

NCSColor = namedtuple('NCSColor', ['name', 'rgb', 'hex'])


def _hex_to_rgb(h):
    if h and len(h) == 6:
        return tuple(map(lambda v: int(v, 16), (h[0:2], h[2:4], h[4:6])))


def _iter():
    for name, hex in ncs.db.colors:
        yield NCSColor(name=name, hex=hex, rgb=_hex_to_rgb(hex))


def all():
    return list(_iter())


def get(name=None, rgb=None, hex=None):
    if name:
        attr = 'name'
        value = name
    elif rgb:
        attr = 'rgb'
        value = rgb
    elif hex:
        attr = 'hex'
        value = hex

    for color in _iter():
        if getattr(color, attr) == value:
            return color
