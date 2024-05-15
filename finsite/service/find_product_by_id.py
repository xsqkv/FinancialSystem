from ..models import Product


class FindProductById:

    def __init__(self, product_id: int):
        self.product_id = product_id

    def __call__(self):
        product = self._find_product()
        return {"name": product.name, "description": product.description}

    def _find_product(self):
        return Product.objects.get(id=self.product_id)