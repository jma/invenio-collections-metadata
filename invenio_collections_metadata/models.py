"""CollectionMetadata models."""


from invenio_db import db
from invenio_collections.models import Collection
from sqlalchemy.dialects import postgresql
from sqlalchemy_utils.types import JSONType


class CollectionMetadata(db.Model):
    """Represent a collection metadata inside the SQL database.

    """

    __tablename__ = 'collections_metadata'

    """Collection identifier."""
    collection_id = db.Column(
        db.Integer,
        db.ForeignKey(Collection.id),
        primary_key=True,
        nullable=False,
        # NOTE no unique constrain for better future ...
    )

    infos = db.Column(
        JSONType().with_variant(
            postgresql.JSON(none_as_null=True),
            'postgresql',
        ),
        default=lambda: dict(),
        nullable=True
    )

    collection = db.relationship(Collection)


__all__ = (
    'CollectionMetadata',
)
