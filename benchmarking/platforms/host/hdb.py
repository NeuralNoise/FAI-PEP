#!/usr/bin/env python

##############################################################################
# Copyright 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
##############################################################################

import os
import shutil

from platforms.platform_util_base import PlatformUtilBase
from utils.custom_logger import getLogger


class HDB(PlatformUtilBase):
    def __init__(self, device=None, tempdir=None):
        super(HDB, self).__init__(device, tempdir)

    def push(self, src, tgt):
        getLogger().info("push {} to {}".format(src, tgt))
        if src != tgt:
            if os.path.isdir(src):
                if os.path.exists(tgt):
                    shutil.rmtree(tgt)
                shutil.copytree(src, tgt)
            else:
                shutil.copyfile(src, tgt)
                os.chmod(tgt, 0o777)

    def pull(self, src, tgt):
        getLogger().info("pull {} to {}".format(src, tgt))
        if src != tgt:
            shutil.copyfile(src, tgt)
            os.chmod(tgt, 0o777)

    def deleteFile(self, file):
        getLogger().info("delete {}".format(file))
        if os.path.isdir(file):
            shutil.rmtree(file)
        else:
            os.remove(file)
