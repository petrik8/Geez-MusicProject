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
Berikut cara penggunaan bot ini :

Song Playing
- /play (judul lagu): memutar lagu melalui Youtube
- /play (yt url): memutar lagu melalui url Youtube
- /dplay: memutar lagu melalui Deezer
- /splay: memutar lagu melalui Jio Saavn
""",

f"""
- /skip: pindah ke lagu berikutnya
- /pause: jeda pemutaran lagu saat ini
- /resume: melanjutkan pemutaran lagu
- /end: menghentikan pemutaran lagu
- /userbotjoin: mengundang asisten musik
- /admincache: memperbarui admin list
"""
      ]
