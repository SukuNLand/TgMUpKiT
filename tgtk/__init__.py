#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = "3.5.9"
__author__ = "unkown"

import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s",
    handlers=[logging.StreamHandler(),logging.FileHandler("tk_log.txt")]
)

from tgtk.core.wserver import start_server
from .core.database_handle import tkupload, tkdb, tktorrents, userdb
from .core.varholdern import VarHolder
import time

logging.info("database created")
upload_db = tkupload()
var_db = tkdb()
tor_db = tktorrents()
user_db = userdb()
transfer = [0,0] # UP,DOWN

uptime = time.time()
to_del = []
SessionVars = VarHolder(var_db)
