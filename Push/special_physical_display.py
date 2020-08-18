#Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Push/special_physical_display.py
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import group, flatten
from ableton.v2.control_surface.elements import PhysicalDisplayElement
DISPLAY_BLOCK_LENGTH = 18

class SpecialPhysicalDisplay(PhysicalDisplayElement):
    u"""
    Special physical display subclass that handles custom and special characters
    """
    ascii_translations = {u'\x00': 0,
     u'\x01': 1,
     u'\x02': 2,
     u'\x03': 3,
     u'\x04': 4,
     u'\x05': 5,
     u'\x06': 6,
     u'\x07': 7,
     u'\xa6': 8,
     u'\xb0': 9,
     u'\xc4': 10,
     u'\xc7': 11,
     u'\xd6': 12,
     u'\xdc': 13,
     u'\xdf': 14,
     u'\xe0': 15,
     u'\xe4': 16,
     u'\xe7': 17,
     u'\xe8': 18,
     u'\xe9': 19,
     u'\xea': 20,
     u'\xee': 21,
     u'\xf1': 22,
     u'\xf6': 23,
     u'\xf7': 24,
     u'\xf8': 25,
     u'\xfc': 26,
     u'\u266d': 27,
     u'\x1b': 27,
     u'\x1c': 28,
     u'\x1d': 29,
     u'\x1e': 30,
     u'\x1f': 31,
     u' ': 32,
     u'!': 33,
     u'"': 34,
     u'#': 35,
     u'$': 36,
     u'%': 37,
     u'&': 38,
     u"'": 39,
     u'(': 40,
     u')': 41,
     u'*': 42,
     u'+': 43,
     u',': 44,
     u'-': 45,
     u'.': 46,
     u'/': 47,
     u'0': 48,
     u'1': 49,
     u'2': 50,
     u'3': 51,
     u'4': 52,
     u'5': 53,
     u'6': 54,
     u'7': 55,
     u'8': 56,
     u'9': 57,
     u':': 58,
     u';': 59,
     u'<': 60,
     u'=': 61,
     u'>': 62,
     u'?': 63,
     u'@': 64,
     u'A': 65,
     u'B': 66,
     u'C': 67,
     u'D': 68,
     u'E': 69,
     u'F': 70,
     u'G': 71,
     u'H': 72,
     u'I': 73,
     u'J': 74,
     u'K': 75,
     u'L': 76,
     u'M': 77,
     u'N': 78,
     u'O': 79,
     u'P': 80,
     u'Q': 81,
     u'R': 82,
     u'S': 83,
     u'T': 84,
     u'U': 85,
     u'V': 86,
     u'W': 87,
     u'X': 88,
     u'Y': 89,
     u'Z': 90,
     u'[': 91,
     u'\\': 92,
     u']': 93,
     u'^': 94,
     u'_': 95,
     u'`': 96,
     u'a': 97,
     u'b': 98,
     u'c': 99,
     u'd': 100,
     u'e': 101,
     u'f': 102,
     u'g': 103,
     u'h': 104,
     u'i': 105,
     u'j': 106,
     u'k': 107,
     u'l': 108,
     u'm': 109,
     u'n': 110,
     u'o': 111,
     u'p': 112,
     u'q': 113,
     u'r': 114,
     u's': 115,
     u't': 116,
     u'u': 117,
     u'v': 118,
     u'w': 119,
     u'x': 120,
     u'y': 121,
     u'z': 122,
     u'{': 125,
     u'|': 124,
     u'}': 125,
     u'~': 126,
     u'\x7f': 127}

    def set_num_segments(self, num_segments):
        super(SpecialPhysicalDisplay, self).set_num_segments(num_segments)
        for segment in self._logical_segments:
            segment.separator = u' '

    def _build_inner_message(self, message):
        message = super(SpecialPhysicalDisplay, self)._build_inner_message(message)
        return flatten([ g[:-1] for g in group(message, DISPLAY_BLOCK_LENGTH) ])
