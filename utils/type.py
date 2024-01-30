from datetime import datetime

BASE_TYPE = {"int": int, "str": str, "datetime": datetime, "float": float, "bool": bool}


def is_float(s: str) -> bool:
    """
    检测字符串是否是float
    :param s: 需要检测的
    :return:检测结果
    """
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_bool(s: str) -> (bool, bool | None):
    """
    检测字符串是否是True or False
    :param s:
    :return: 结果， 值
    """
    if s.lower() in ("yes", "true", "t", "y", "True"):
        return True, True
    elif s.lower() in ("no", "false", "f", "False"):
        return True, False
    else:
        return False, None


def translate_type(s: str, t: str) -> BASE_TYPE.values:
    """
    转换类型
    :param s: 需要转化的值
    :param t: 目标类型
    :return:
    """
    if t not in BASE_TYPE.keys():
        raise ValueError("传入的类型不支持类型转换")

    # 布尔值需要进行特殊转换
    if t == "bool":
        if s == "True":
            return True
        return False
    if t == "datetime":
        return datetime.fromisoformat(s)
    t_v = BASE_TYPE[t](s)
    return t_v
