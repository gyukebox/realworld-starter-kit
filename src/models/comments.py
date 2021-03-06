import sqlalchemy as sa
import sqlalchemy_utils as sau
from sqlalchemy.orm import relationship

from associations import articles_comments_relationship_table
from models.database import Base, Session


class CommentManager(object):
    """
    Manager class for model Comment
    """

    def __init__(self):
        self.session = Session()

    pass


class Comment(Base, sau.Timestamp):
    """
    Comment model class
    """
    __tablename__ = 'conduit_api_comment'

    # base fields
    id = sa.Column(
        'id',
        sa.Integer,
        autoincrement=True,
        primary_key=True,
        nullable=False,
        unique=True
    )
    body = sa.Column(
        'body',
        sa.String(100),
        nullable=False
    )

    author_id = sa.Column(
        'author-id',
        sau.UUIDType(binary=False),
        sa.ForeignKey('conduit_api_profile.user-id'),
        nullable=False
    )
    article_id = sa.Column(
        'article-id',
        sau.UUIDType(binary=False),
        sa.ForeignKey('conduit_api_article.uuid'),
        nullable=False
    )

    # relationship fields
    author = relationship('Profile', back_populates='conduit_api_profile')
    article = relationship(
        'Article',
        secondary=articles_comments_relationship_table,
        back_populates='conduit_api_article'
    )

    __manager__ = CommentManager()

    def __repr__(self):
        pass

    def __str__(self):
        return 'Conduit API Comment Model'

    def serialize(self):
        pass
