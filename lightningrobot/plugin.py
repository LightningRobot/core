from abc import ABC, abstractmethod
from . import log
class Plugin(ABC):
    @abstractmethod
    async def on_command(self, message: str,id) -> None:
        """处理接收到的消息"""
        await log.info("收到来自"+id+"的消息：",message)
        #未来在此处添加判断用户。
        pass