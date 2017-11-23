#!/usr/bin/env python

import socket
import json

from pycsco.nxos.device import Device
from pycsco.nxos.utils import nxapi_lib


def main():

    username = 'cisco'
    password = 'cisco'
    protocol = 'http'
    node = 'n9k1'
    host = socket.gethostbyname(node)

    device = Device(ip=host, username=username, password=password,
                    protocol=protocol)

    neighbors = nxapi_lib.get_neighbors(device)

    print neighbors   # returns a list

    neighs = dict(neighbors=neighbors)

if __name__ == "__main__":
    main()
