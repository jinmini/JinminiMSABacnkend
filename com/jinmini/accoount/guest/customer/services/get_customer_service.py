from sqlalchemy.ext.asyncio import AsyncSession
from com.jinmini.utils.creational.abstract.abstract_service import AbstractService

class GetCustomer(AbstractService):
    async def handle(self, db: AsyncSession, **kwargs):
        pass

class GetCustomerById(AbstractService):
    async def handle(self, db: AsyncSession, **kwargs):
        pass


