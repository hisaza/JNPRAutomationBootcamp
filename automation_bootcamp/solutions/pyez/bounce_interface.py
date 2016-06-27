#!/usr/bin/env python
"""
PyEZ structured change illustration.

darien@sdnessentials.com
"""

from jnpr.junos.cfg.phyport import PhyPortClassic
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import sys
import time


def main():
    """Simple main method to change port status."""
    r1 = Device(host='10.11.12.1', user='netconf', password='test123')
    r1.open()

    r2 = Device(host='10.11.12.2', user='netconf', password='test123')
    r2.open()

    r1_port = PhyPortClassic(r1, namevar='ge-0/0/3')
    r2_port = PhyPortClassic(r2, namevar='ge-0/0/2')

    # Step 1.1
    # print(r1_port.properties)
    # print r1_port.admin
    # print(r2_port.properties)
    # print r2_port.admin

    # Step 1.2
    r1_port.admin = False
    r1_port.write()
    r2_port.admin = False
    r2_port.write()

    print("Disabling interfaces!")
    r1_cfg = Config(r1)
    r2_cfg = Config(r2)
    r1_cfg.commit()
    r2_cfg.commit()

    time.sleep(10)

    r1_port.admin = True
    r1_port.write()
    r2_port.admin = True
    r2_port.write()

    print("Enabling interfaces!")
    r1_cfg.commit()
    r2_cfg.commit()

    r1.close()
    r2.close()

if __name__ == '__main__':
    sys.exit(main())
