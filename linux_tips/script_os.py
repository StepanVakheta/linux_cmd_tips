#!/usr/bin/env python3

import sys, os, ftplib

with ftplib.FTP ("") as ftp:
    ftp.login("")
    ftp.retrlines()