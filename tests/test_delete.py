import builtins #used to patch the global builtins input function so tests can simulate user responses
from unittest.mock import patch, MagicMock
import pytest

#import module under test (adjust import path if needed)
import project.delete as delete_mod
