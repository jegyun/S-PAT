"""Initial migration

Revision ID: ad7b6223ba8e
Revises: 
Create Date: 2025-04-30 16:24:32.632649

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'ad7b6223ba8e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('conversation',
    sa.Column('conversation_id', sa.Integer(), nullable=False),
    sa.Column('session_id', sa.String(length=50), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('query', sa.String(length=250), nullable=True),
    sa.Column('answer', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('conversation_id')
    )
    op.create_index(op.f('ix_conversation_conversation_id'), 'conversation', ['conversation_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_conversation_conversation_id'), table_name='conversation')
    op.drop_table('conversation')
    # ### end Alembic commands ###
