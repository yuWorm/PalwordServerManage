from enum import Enum


class DifficultyEnum(str, Enum):
    """
    游戏难度
    """

    # 休闲模式
    CASUAL: str = "Casual"
    # 普通模式
    NORMAL: str = "Normal"
    # 困难模式
    HARD: str = "Hard"


class DeathPenaltyEnum(str, Enum):
    """
    死亡掉落
    """

    # 不掉落
    NONE: str = "None"
    # 掉落装备了的物品
    ITEM: str = "Item"
    # 掉落身上带着的
    ITEM_AND_EQUIPMENT: str = "ItemAndEquipment"
    # 掉落所有，包括终端里面的
    ALL: str = "All"


class DockerStatusEnum(str, Enum):
    RUNNING: str = "running"
    EXITED: str = "exited"
