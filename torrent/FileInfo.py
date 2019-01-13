import os
from math import ceil


class FileInfo:
    def __init__(self, path):
        self.path = path
        if os.path.exists(path):
            self.size = os.path.getsize(path)
        else:
            self.size = 0
        self.offset = None

    def get_block_size(self, piece):
        return self.get_piece_size(piece) / self.block_size


    def get_piece_size(self, piece_size):
        pass

    # def send_block(piece, block):
    #     offset
