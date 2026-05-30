from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Product
from schemas import ProductCreate

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("/")
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products


@router.post("/add")
def add_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):

    new_product = Product(
        name=product.name,
        category=product.category,
        price=product.price,
        quantity=product.quantity,
        image=product.image
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return {
        "message": "Product Added Successfully",
        "product_id": new_product.id
    }



@router.delete("/delete/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:
        return {
            "message": "Product Not Found"
        }

    db.delete(product)
    db.commit()

    return {
        "message": "Product Deleted Successfully"
    }


@router.put("/buy/{product_id}")
def buy_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:
        return {
            "message": "Product Not Found"
        }

    if product.quantity <= 0:
        return {
            "message": "Out Of Stock"
        }

    product.quantity -= 1
    product.sold += 1

    db.commit()

    return {
        "message": "Product Purchased Successfully"
    }