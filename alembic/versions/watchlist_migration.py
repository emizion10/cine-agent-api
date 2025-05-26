"""create watchlist table

Revision ID: 002
Revises: 001
Create Date: 2024-03-21 11:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '002'
down_revision = '001'
branch_labels = None
depends_on = None

def upgrade():
    # Create watchlist table with status as string first
    op.create_table(
        'watchlist',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('movie_id', sa.Integer(), nullable=False),
        sa.Column('status', sa.String(20), nullable=False, server_default='pending'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_watchlist_id'), 'watchlist', ['id'], unique=False)
    op.create_index(op.f('ix_watchlist_user_id'), 'watchlist', ['user_id'], unique=False)
    op.create_index(op.f('ix_watchlist_movie_id'), 'watchlist', ['movie_id'], unique=False)

    # Add check constraint to ensure status is one of the allowed values
    op.execute("""
        ALTER TABLE watchlist 
        ADD CONSTRAINT watchlist_status_check 
        CHECK (status IN ('pending', 'watching', 'watched', 'dropped'))
    """)

def downgrade():
    op.drop_index(op.f('ix_watchlist_movie_id'), table_name='watchlist')
    op.drop_index(op.f('ix_watchlist_user_id'), table_name='watchlist')
    op.drop_index(op.f('ix_watchlist_id'), table_name='watchlist')
    op.drop_table('watchlist') 