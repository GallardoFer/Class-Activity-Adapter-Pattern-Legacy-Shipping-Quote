from .shipping_quote_provider import ShippingQuoteProvider


class Checkout:
    def __init__(self, shipping: ShippingQuoteProvider):
        self.shipping = shipping

    def shipping_quote(self, destination: str, weight_kg: float) -> float:
        return self.shipping.quote(destination, weight_kg)
