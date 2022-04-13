import random
import time
import json
from pathlib import Path

class Serials(object):

    def __init__(self, Serials, Prefix, Chars: str):
        self.Serials = Serials
        self.Prefix = Prefix
        self.Chars = Chars
        #'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'

    def SerialGenerate(self, lengh: int):
        serial = ""
        if lengh >= 100:
            raise Exception("Lengh is to big. You can't have more then 100 characters.")
        else:
            for x in range(lengh):
                serial_chars = random.choice(self.Chars)
                serial = serial + serial_chars

            return str(self.Prefix + serial)

    def SerialsMassGenerate(self, amout: int, lengh: int):
        if lengh >= 100:
            raise Exception("Lengh is to big. You can't have more then 100 characters.")
        else:
            for i in range(amout):
                gen1 = self.SerialGenerate(lengh)
                self.Serials.append(gen1)
            return self.Serials
