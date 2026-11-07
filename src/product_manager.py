import uuid
# universally unique id
def generate_product_id():
    return str(uuid.uuid4())
product_id=generate_product_id()
print(product_id)