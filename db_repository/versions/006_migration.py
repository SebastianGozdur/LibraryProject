from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
books = Table('books', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=120)),
    Column('author', String(length=120)),
    Column('quantity', Integer),
)

reserved_books = Table('reserved_books', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('user_id', Integer),
    Column('book_id', Integer),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('nickname', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['books'].create()
    post_meta.tables['reserved_books'].create()
    pre_meta.tables['user'].columns['email'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['books'].drop()
    post_meta.tables['reserved_books'].drop()
    pre_meta.tables['user'].columns['email'].create()
