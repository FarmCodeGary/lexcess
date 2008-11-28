
from distutils.core import setup
import py2exe

setup(windows = ["lexcess_gui.py"],
      author="Garrison Benson",
      author_email="benson.garrison@gmail.com",
      url="http://www.bensonbasement.com",
      data_files=[('.', ["buzzer.wav",
                         "ding.wav",
                         "wordset.dat"
                         ])])