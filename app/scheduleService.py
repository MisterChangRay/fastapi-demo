
from loguru import logger

def test():
    """
    一个演示用的计划任务
    方法需要在 main.py 中注册
    """
    logger.info("测试, 每3秒执行一次")
    pass