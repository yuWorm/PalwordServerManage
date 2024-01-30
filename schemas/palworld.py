from pydantic import BaseModel, Field

from schemas.enum import DifficultyEnum, DeathPenaltyEnum


class PalGameWorldSettingsSchema(BaseModel):
    difficulty: DifficultyEnum = Field(
        default=DifficultyEnum.NORMAL, alias="Difficulty", description="难度"
    )
    day_time_speed_rate: float = Field(
        1.0, alias="DayTimeSpeedRate", description="白天的速率"
    )
    night_time_speed_rate: float = Field(
        1.0, alias="NightTimeSpeedRate", description="夜晚的速率"
    )
    exp_rate: float = Field(1.0, alias="ExpRate", description="经验值倍率")
    pal_capture_rate: float = Field(1.0, alias="PalCaptureRate", description="捕获成功倍率")
    pal_spawn_num_rate: float = Field(
        1.0, alias="PalSpawnNumRate", description="帕鲁生成数量倍率"
    )
    pal_damage_rate_attack: float = Field(
        1.0, alias="PalDamageRateAttack", description="帕鲁攻击伤害倍率"
    )
    pal_damage_rate_defense: float = Field(
        1.0, alias="PalDamageRateDefense", description="帕鲁承受伤害倍率"
    )
    player_damage_rate_attack: float = Field(
        1.0, alias="PlayerDamageRateAttack", description="玩家造成的伤害倍率"
    )
    player_damage_rate_defense: float = Field(
        1.0, alias="PlayerDamageRateDefense", description="玩家受到的伤害倍率"
    )
    player_stomach_decrease_rate: float = Field(
        1.0, alias="PlayerStomachDecreaceRate", description="玩家饥饿消耗倍率"
    )
    player_stamina_decrease_rate: float = Field(
        1.0, alias="PlayerStaminaDecreaceRate", description="玩家耐力降低倍率"
    )
    player_auto_hp_regene_rate: float = Field(
        1.0, alias="PlayerAutoHPRegeneRate", description="玩家自动HP恢复倍率"
    )
    player_auto_hp_regene_rate_in_sleep: float = Field(
        1.0, alias="PlayerAutoHpRegeneRateInSleep", description="玩家睡眠HP恢复倍率"
    )
    pal_stomach_decrease_rate: float = Field(
        1.0, alias="PalStomachDecreaceRate", description="帕鲁饥饿消耗倍率"
    )
    pal_stamina_decrease_rate: float = Field(
        1.0, alias="PalStaminaDecreaceRate", description="帕鲁耐力降低倍率"
    )
    pal_auto_hp_regene_rate: float = Field(
        1.0, alias="PalAutoHPRegeneRate", description="帕鲁受伤时HP自动恢复的速度"
    )
    pal_auto_hp_regene_rate_in_sleep: float = Field(
        1.0, alias="PalAutoHpRegeneRateInSleep", description="帕鲁睡眠时恢复多少HP倍率"
    )
    build_object_damage_rate: float = Field(
        1.0, alias="BuildObjectDamageRate", description="建筑伤害倍率"
    )
    build_object_deterioration_damage_rate: float = Field(
        1.0, alias="BuildObjectDeteriorationDamageRate", description="建筑在一段时间内将受到的伤害倍率"
    )
    collection_drop_rate: float = Field(
        1.0, alias="CollectionDropRate", description="树木或岩石等物体的掉落倍率"
    )
    collection_object_hp_rate: float = Field(
        1.0, alias="CollectionObjectHpRate", description="树木或岩石等物体的血量倍率"
    )
    collection_object_respawn_speed_rate: float = Field(
        1.0, alias="CollectionObjectRespawnSpeedRate", description="树木或岩石等物体中的刷新速度倍率"
    )
    enemy_drop_item_rate: float = Field(
        1.0, alias="EnemyDropItemRate", description="敌人掉落物品的倍率"
    )
    death_penalty: DeathPenaltyEnum = Field(
        DeathPenaltyEnum.ITEM_AND_EQUIPMENT, alias="DeathPenalty", description="死亡掉落"
    )
    b_enable_aim_assist_pad: bool = Field(
        True, alias="bEnableAimAssistPad", description="允许您启用或禁用瞄准辅助"
    )
    b_enable_aim_assist_keyboard: bool = Field(
        False, alias="bEnableAimAssistKeyboard", description="允许您启用或禁用瞄准辅助"
    )
    drop_item_max_num: int = Field(
        3000, alias="DropItemMaxNum", description="一次允许丢弃的最大项目数量"
    )
    base_camp_max_num: int = Field(
        128, alias="BaseCampMaxNum", description="一次可以建造的最大基地数量"
    )
    base_camp_worker_max_num: int = Field(
        15, alias="BaseCampWorkerMaxNum", description="营地中可以容纳的最大工人伙伴数量"
    )
    drop_item_alive_max_hours: float = Field(
        1.0, alias="DropItemAliveMaxHours", description="掉落的物品在消失之前会停留多长时间"
    )
    b_auto_reset_guild_no_online_players: bool = Field(
        False, alias="bAutoResetGuildNoOnlinePlayers", description="没有玩家在线的情况下解散工会"
    )
    auto_reset_guild_time_no_online_players: float = Field(
        72.0, alias="AutoResetGuildTimeNoOnlinePlayers", description="不活跃的公会解散的时间（小时）"
    )
    guild_player_max_num: int = Field(
        20, alias="GuildPlayerMaxNum", description="最大公会玩家数量"
    )
    pal_egg_default_hatching_time: float = Field(
        72.0, alias="PalEggDefaultHatchingTime", description="孵化帕鲁蛋需要多长时间（小时）"
    )
    work_speed_rate: float = Field(1.0, alias="WorkSpeedRate", description="工作速度倍率")
    coop_player_max_num: int = Field(
        4, alias="CoopPlayerMaxNum", description="群中的最大玩家数量"
    )
    server_player_max_num: int = Field(
        32, alias="ServerPlayerMaxNum", description="服务器上允许的最大玩家数（上限为 32）"
    )
    server_name: str = Field(
        "Default Palworld Server", alias="ServerName", description="服务器名称"
    )
    server_description: str = Field(
        "", alias="ServerDescription", description="在列表中选择服务器时显示的内容"
    )
    admin_password: str = Field("", alias="AdminPassword", description="管理员密码")
    server_password: str = Field("", alias="ServerPassword", description="服务器密码")
    public_port: int = Field(8211, alias="PublicPort", description="公开的服务器端口")
    public_ip: str = Field("", alias="PublicIP", description="公开服务器的IP")
    rcon_enabled: bool = Field(True, alias="RCONEnabled", description="是否启用 RCON")
    rcon_port: int = Field(25575, alias="RCONPort", description="RCON 的默认端口号")
