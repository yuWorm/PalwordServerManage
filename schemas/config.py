from datetime import datetime
from pydantic import BaseModel


class IntervalConfigSchema(BaseModel):
    auto_restart_palworld_server: bool
    auto_restart_palworld_server_time: datetime
    auto_backup: bool
    auto_backup_interval: int
    update_player: bool
    update_player_interval: int
    auto_update_palworld_server: bool
    auto_update_palworld_interval: datetime
