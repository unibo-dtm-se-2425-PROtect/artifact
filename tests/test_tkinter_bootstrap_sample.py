import tkinter as tk
from unittest import mock
import types

import project.tkinter_bootstrap_sample as app_module #import module under test

#fake widget implementations

class FakeWidget:
    """
    Base fake widget.
    - Records init kwargs in _config for possible assertions.
    """
    def __init__(self, *args, **kwargs):
        self._config = kwargs
        self._packed = False
