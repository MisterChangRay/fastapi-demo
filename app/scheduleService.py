
from loguru import logger
from .service import KVService

def scheduleForExpireKeyValueTalbe():
    """
    计划任务
    用于清除KV表中的过期数据
    """
    KVService.expireData()
    pass