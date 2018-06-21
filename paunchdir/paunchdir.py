# -*- coding: utf-8 -*-

"""Main module."""

import os.path
from pathlib import Path


class PaunchDir(object):
    def __init__(self, base_dir, levels=3, level_name_len=2):
        self._base_dir = base_dir
        self._levels = levels
        self._level_name_len = level_name_len

    @property
    def min_file_name_len(self):
        return self._levels * self._level_name_len + 1

    def compose(self, file_name):
        parts = []
        for l in range(0, self._levels):
            parts.append(file_name[
                (l + 0) * self._level_name_len:
                (l + 1) * self._level_name_len])

        file_name = file_name[self._levels * self._level_name_len:]
        return os.path.join(self._base_dir, '/'.join(parts), file_name)

    def decompose(self, file_path):
        parts = Path(file_path).parts
        return ''.join(parts[len(parts) - self._levels - 1:])
