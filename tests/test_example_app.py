# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016 RERO.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, RERO does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.


"""Test example app."""

import os
import signal
import subprocess
import sys
import time


def setup_module(module):
    """Set up before all tests."""
    # switch to examples/app.py
    exampleappdir = os.path.join(os.path.split(sys.path[0])[0],
                                 'examples')
    os.chdir(exampleappdir)


def teardown_module(module):
    """Tear down after all tests."""
    pass


def test_example_app():
    """Test example app."""
    pass