## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = "BQBddNHSNNeY5nHINmZU_Q4-fBK5wn52q9WvgL7AhO8vYoejmvrkQq14wWsz0QuUF5dxSohCDH7A1tYquVtN5J8h3RcfiKu-IRQ8hwRlKe3yj_GkBC4vjgKQp4Xv1r8EC4RniZ3IuJzxETorisvDNuBN1yc7DOzpGnNE2IkDtRcFXtQ8SY5SOKHVVGYSeQrX8LmNgCWh61agjjF-lfBmIDSZPiok8FB20D2Hq-Wfup3fgZ_nQOXgbgwRKlV1zcpD0M4M0NKSAb4Fz7wT6f4G4rmCZf0aaSy0esJhP5eOhlsNechoQL-9qHnNyu5bA38bG21JLAdA8sOL-Bq0pV9gNyz6AAAAAU44AhIA"
BOT_TOKEN = "6083378336:AAHzkawEuJ_3-x4N2DIBMniKzW55scmVWFU"
BOT_NAME = "Rythm Beatz"
API_ID = "19584198"
API_HASH = "0ed81ce2babcf61c880d2b49c2dee9f1"
OWNER_NAME = "The Inflex Leader"
ALIVE_NAME = "Alive"
ASSISTANT_USERNAME = "RythmBeatzBot_Assistant"
BOT_USERNAME = "RythmBeatzBot"
ASSISTANT_NAME = "RythmBeatzBot Assistant"
GROUP_SUPPORT = "InflexSupport"
UPDATES_CHANNEL = "InflexUpdates"
SUDO_USERS = "5747402681"
COMMAND_PREFIXES = "/"
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TrickyYash198/HerokuMusic")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
