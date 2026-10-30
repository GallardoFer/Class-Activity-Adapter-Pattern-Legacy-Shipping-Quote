from shipping_adapter.legacy_carrier import LegacyCarrier


def test_legacy_carrier_still_works_on_its_own_terms():
    price = LegacyCarrier().get_price("45000", 10.0)
    assert price == 18.50
