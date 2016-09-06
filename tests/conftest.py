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


"""Pytest configuration."""

from __future__ import absolute_import, print_function

import os
import pytest
import shutil
import tempfile

from flask import Flask
from invenio_collections import InvenioCollections
from invenio_collections.models import Collection
from invenio_db import db as db_
from invenio_db import InvenioDB
from invenio_collections_metadata import InvenioCollectionsMetadata
from invenio_collections_metadata.models import CollectionMetadata
# from invenio_jsonschemas import InvenioJSONSchemas
from sqlalchemy_utils.functions import create_database, database_exists

SAMPLE_DESCRIPTION = '''<p>
<strong>Lorem ipsum</strong> dolor sit amet, consectetur adipiscing elit. In
quis nunc blandit, imperdiet mi in, blandit dolor. Proin nisi libero, commodo
non tempor et, lacinia at risus. Vestibulum in fermentum lectus. Aenean vel
cursus felis, eu molestie risus. Pellentesque in sagittis eros. Maecenas
porttitor ultrices lectus, et gravida nisi commodo varius. Vestibulum in
tellus interdum, convallis odio ultrices, scelerisque leo. Suspendisse lacinia
massa et convallis fermentum. Sed facilisis justo vel ante dictum elementum.
Nunc rhoncus, justo quis finibus lobortis, dui elit tempus lacus, commodo
porta nunc magna hendrerit dolor. Donec fermentum dui ac ante vestibulum
pharetra. Donec rutrum faucibus convallis. Pellentesque convallis dapibus
eros, quis ultricies lorem elementum in. Quisque laoreet varius mauris sed
tincidunt. Vestibulum sapien dolor, maximus ut interdum sit amet, pretium et
velit.
'''


@pytest.yield_fixture()
def app(request):
    """Flask application fixture."""
    instance_path = tempfile.mkdtemp()
    app_ = Flask(__name__, instance_path=instance_path)
    app_.config.update(
        SECRET_KEY='CHANGE_ME',
        SQLALCHEMY_DATABASE_URI=os.environ.get(
            'SQLALCHEMY_DATABASE_URI', 'sqlite://'),
        SQLALCHEMY_TRACK_MODIFICATIONS=True,
        TESTING=True,
    )
    # app_.register_blueprint(files_rest_blueprint)
    # FlaskCLI(app_)
    InvenioDB(app_)
    InvenioCollections(app_)
    InvenioCollectionsMetadata(app_)
    # InvenioJSONSchemas(app_)
    # (app_)

    with app_.app_context():
        yield app_

    shutil.rmtree(instance_path)


@pytest.yield_fixture()
def db(app):
    """Database fixture."""
    if not database_exists(str(db_.engine.url)):
        create_database(str(db_.engine.url))
    db_.create_all()
    yield db_
    db_.session.remove()
    db_.drop_all()


@pytest.fixture()
def collection_metadata(db):
    """Create a bucket."""
    col = Collection(name='test')
    db.session.add(col)
    db.session.commit()
    col_meta = CollectionMetadata(collection=col,
                                  infos={'description': SAMPLE_DESCRIPTION})
    db.session.add(col_meta)
    db.session.commit()
    return col_meta
