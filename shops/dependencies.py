from HomeWorks.shops.db.config import async_session
from HomeWorks.shops.db.dals.sale_dls import SaleDAL


async def get_sale_dal():
    async with async_session() as session:
        async with session.begin():
            yield SaleDAL(session)
