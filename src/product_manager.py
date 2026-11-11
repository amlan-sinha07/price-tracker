import uuid

def add_product(products,new_product):
    product=new_product.copy()
    product['id']=str(uuid.uuid4())

    products.append(product)
    return product
def get_product(products,product_id):
    for product in products:
        if product.get('id')==product_id:
            return product
    return None
def update_product(products,product_id,updates):
    allowed_fields={"name","url","target_price"}
    invalid_fields=set(updates)-allowed_fields
    if invalid_fields :
        raise ValueError(
            f"Invalid update fields: {sorted(invalid_fields)}"
        )
    for product in products:
        if product.get("id")==product_id:
            products.update(updates)
            return products
    return None
def remove_product(products,product_id):
    for index,product in enumerate(products):
        if product.get('id')==product_id:
            del products[index]
            return True
    return False