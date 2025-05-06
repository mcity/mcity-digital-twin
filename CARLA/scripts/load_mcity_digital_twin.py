#!/usr/bin/env python

from __future__ import print_function


import glob
import os
import sys

try:
    sys.path.append(
        glob.glob(
            "../carla/dist/carla-*%d.%d-%s.egg"
            % (
                sys.version_info.major,
                sys.version_info.minor,
                "win-amd64" if os.name == "nt" else "linux-x86_64",
            )
        )[0]
    )
except IndexError:
    pass


import carla


client = carla.Client("localhost", 2000)

world = client.load_world("McityMap_Main")

print("Welcome To Mcity!")
