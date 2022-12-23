from typing import List

from fastapi import APIRouter, Depends

from db.dals.sale_dls import SaleDAL
from db.models.models import Product, Store
from dependencies import get_sale_dal

router = APIRouter()

@router.get("/products")
async def get_all_product(sale_dal: SaleDAL = Depends(get_sale_dal)) -> List[Product]:
    return await sale_dal.get_all_products()

@router.get("/stores")
async def get_all_stores(sale_dal: SaleDAL = Depends(get_sale_dal)) -> List[Store]:
    return await sale_dal.get_all_stores()

@router.post("/sale")
async def post_sale_product(product_id: int, store_id: int, sale_dal: SaleDAL = Depends(get_sale_dal)):
    return await sale_dal.post_sale_product(product_id, store_id)

@router.get("/stores/top")
async def get_top_stores(sale_dal: SaleDAL = Depends(get_sale_dal)) -> List[Store]:
    return await sale_dal.get_top_stores()

@router.get("/products/top")
async def get_top_product(sale_dal: SaleDAL = Depends(get_sale_dal)) -> List[Product]:
    return await sale_dal.get_top_products()
