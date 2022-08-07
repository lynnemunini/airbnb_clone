#!/usr/bin/env python3
"""
Let's intepreter know that the directory contains code for a python module
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
