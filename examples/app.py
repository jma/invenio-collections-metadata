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


"""Minimal Flask application example for development.

Run example development server:

.. code-block:: console

   $ cd examples
   $ export FLASK_APP=app.py
   $ export FLASK_DEBUG=1
   $ flask run
"""

from __future__ import absolute_import, print_function

import os

from flask import Flask
from flask_babelex import Babel

from invenio_collections import InvenioCollections
from invenio_collections_metadata import InvenioCollectionsMetadata
from invenio_db import InvenioDB

# Create Flask application
app = Flask(__name__)
app.config.update(
    SECRET_KEY='CHANGE_ME',
    SQLALCHEMY_DATABASE_URI=os.environ.get(
        'SQLALCHEMY_DATABASE_URI', 'sqlite://'),
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    TESTING=True,
)
Babel(app)
    # instance_path = tempfile.mkdtemp()
InvenioDB(app)
InvenioCollections(application)
InvenioCollectionsMetadata(app)
