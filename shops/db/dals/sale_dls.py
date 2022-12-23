from typing import List
from sqlalchemy import func
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from db.models.models import Product, Store, Sale


class SaleDAL():
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def get_all_products(self) -> List[Product]:
        query = await self.db_session.execute(select(Product).order_by(Product.id))
        return query.scalars().all()

    async def get_all_stores(self) -> List[Store]:
        query = await self.db_session.execute(select(Store).order_by(Store.id))
        return query.scalars().all()

    async def post_sale_product(self, product_id: Product.id, store_id: Store.id):
        new_sale = Sale(product_id=product_id, store_id=store_id)
        self.db_session.add(new_sale)
        await self.db_session.flush()
        return {"product id": product_id, "store id": store_id}

    async def get_top_stores(self) -> List[Store]:
        query = await self.db_session.execute(select(Sale.store_id, Store.address, func.sum(Product.price).label('total_amount')).
                                              join(Store).join(Product).group_by(Store.address).order_by(func.sum(Product.price).desc()).limit(10))
        return query.all()

    async def get_top_products(self) -> List[Product]:
        query = await self.db_session.execute(select(Sale.product_id, Product.name, func.count(Sale.product_id).label('sales_count_products')).
                                              join(Product).group_by(Product.name).order_by(func.count(Sale.product_id).desc()).limit(10))
        return query.all()
