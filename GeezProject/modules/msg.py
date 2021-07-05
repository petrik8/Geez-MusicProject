# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from GeezProject.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL, OWNER
class Messages():
      HELP_MSG = [
        ".",
f"""
- /song (judul lagu): download lagu dari YouTube 
- /song (link youtube): download lagu dari link YouTube
- /vsong (judul video): download video dari YouTube 
- /vsong (link youtube): download video dari link YouTube
""",

f"""
Masukkan judul secara detail untuk mendapatkan lagu dan video yang sesuai. Gunakan perintah /search untuk mendapatkan link lagu dan video yang kamu minta. 
"""
      ]
