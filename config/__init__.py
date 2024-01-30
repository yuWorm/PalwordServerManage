from .base import Config
from .pal import PalGameSettings

settings = Config()
pal_settings: PalGameSettings = PalGameSettings(
    settings.PALWORLD_CONFIG_PATH, settings.PALWORLD_BLACKLIST_PATH
)
