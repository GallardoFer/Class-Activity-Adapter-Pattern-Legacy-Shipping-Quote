from .legacy_carrier import LegacyCarrier
from .shipping_quote_provider import ShippingQuoteProvider


class LegacyCarrierAdapter(ShippingQuoteProvider):
    """Adapts LegacyCarrier.get_price(postal_code, weight_lb) to the
    ShippingQuoteProvider.quote(destination, weight_kg) contract."""

    LB_PER_KG = 2.20462

    def __init__(self, carrier: LegacyCarrier):
        self._carrier = carrier

    def quote(self, destination: str, weight_kg: float) -> float:
        weight_lb = weight_kg * self.LB_PER_KG
        return self._carrier.get_price(destination, weight_lb)
