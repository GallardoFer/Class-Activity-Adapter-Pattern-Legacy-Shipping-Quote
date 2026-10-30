class LegacyCarrier:
    def get_price(self, postal_code: str, weight_lb: float) -> float:
        zone_fee = 6.0 if postal_code.startswith("45") else 8.0
        return round(zone_fee + (weight_lb * 1.25), 2)
