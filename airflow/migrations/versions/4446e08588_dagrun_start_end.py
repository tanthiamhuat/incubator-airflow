# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""dagrun start end

Revision ID: 4446e08588
Revises: 561833c1c74b
Create Date: 2015-12-10 11:26:18.439223

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "4446e08588"
down_revision = "561833c1c74b"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("dag_run", sa.Column("end_date", sa.DateTime(), nullable=True))
    op.add_column("dag_run", sa.Column("start_date", sa.DateTime(), nullable=True))


def downgrade():
    op.drop_column("dag_run", "start_date")
    op.drop_column("dag_run", "end_date")
