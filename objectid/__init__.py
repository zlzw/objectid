import hashlib
import socket
import random
import struct
import os
import time

__version__ = '0.0.1'


def _calc_hostname_bytes():
    m = hashlib.md5()
    m.update(socket.gethostname())

    return m.digest()[0:3]


class ObjectId(object):
    _inc = random.randint(0, 0xFFFFFF)
    _hostname_bytes = _calc_hostname_bytes()

    def __init__(self, oid=None):
        if not oid:
            self._id = self._assemble()
        else:
            self._disassemble(oid)
            self._id = oid

    def _assemble(self):
        # 4 bytes current time
        self.time = int(time.time())
        oid = struct.pack(">i", int(self.time))

        # 3 bytes machine
        oid += ObjectId._hostname_bytes

        # 2 bytes pid
        oid += struct.pack(">H", os.getpid() % 0xFFFF)

        # 3 bytes inc
        ObjectId._inc += 1
        oid += struct.pack(">i", ObjectId._inc)[1:4]

        return oid.encode("hex")

    def _disassemble(self, oid):
        b = oid.decode("hex")
        self.time = struct.unpack(">i", b[0:4])[0]

    def __str__(self):
        return self._id

    def __repr__(self):
        return "ObjectId('%s')" % (str(self),)

    def __eq__(self, other):
        if isinstance(other, ObjectId):
            return self._id == other._id
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, ObjectId):
            return self._id != other._id
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, ObjectId):
            return self._id < other._id
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, ObjectId):
            return self._id <= other._id
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, ObjectId):
            return self._id > other._id
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, ObjectId):
            return self._id >= other._id
        return NotImplemented
