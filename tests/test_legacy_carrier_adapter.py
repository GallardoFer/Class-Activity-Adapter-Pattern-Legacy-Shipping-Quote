from shipping_adapter.checkout import Checkout
from shipping_adapter.legacy_carrier import LegacyCarrier
from shipping_adapter.legacy_carrier_adapter import LegacyCarrierAdapter


def test_checkout_quotes_through_legacy_carrier_via_adapter():
    checkout = Checkout(LegacyCarrierAdapter(LegacyCarrier()))

    # 10 kg -> 22.0462 lb -> 6.0 zone fee + 22.0462 * 1.25 = 33.56
    assert checkout.shipping_quote("45000", 10.0) == 33.56
