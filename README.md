# Adapter Pattern — Legacy Shipping Quote

**Modified by:** Fernando Gallardo Romero

## Target / Adapter / Adaptee structure

- **Target:** `ShippingQuoteProvider` — the contract `Checkout` depends on: `quote(destination, weight_kg)`.
- **Adaptee:** `LegacyCarrier` — the useful legacy class with an incompatible interface: `get_price(postal_code, weight_lb)`.
- **Adapter:** `LegacyCarrierAdapter` (`src/shipping_adapter/legacy_carrier_adapter.py`) — implements `ShippingQuoteProvider` and wraps a `LegacyCarrier` through composition (object adapter).
- **Client:** `Checkout` — receives any `ShippingQuoteProvider` and never knows the legacy carrier exists.

`Checkout`, `ShippingQuoteProvider`, and `LegacyCarrier` were not modified.

## Translation (kg → lb)

The adapter translates the call in one place: `destination` is passed as the `postal_code`, and the weight is converted using `1 kg = 2.20462 lb` (stored as the constant `LB_PER_KG`) before calling `get_price`. The returned price is passed back unchanged.

```python
def quote(self, destination: str, weight_kg: float) -> float:
    weight_lb = weight_kg * self.LB_PER_KG
    return self._carrier.get_price(destination, weight_lb)
```

## Focused test

`tests/test_legacy_carrier_adapter.py` builds a real `Checkout` with `LegacyCarrierAdapter(LegacyCarrier())` and asks for a quote through the Target contract. For 10 kg to postal code `45000`: 10 × 2.20462 = 22.0462 lb, then 6.0 + 22.0462 × 1.25 = **33.56**. If the conversion were missing, the result would be 18.50, so the test also proves the kg → lb translation happens. Run it with `pytest -q` (2 passed).

## Design explanation / complexity cost

`Checkout` depends on the `ShippingQuoteProvider` contract, while the existing `LegacyCarrier` speaks a different interface and works in pounds. Instead of changing either side, the adapter sits between them, so `Checkout` and the legacy code stay untouched and loosely coupled, and a new carrier could be plugged in the same way. The complexity cost is an extra layer of indirection. When a price looks wrong, the real logic is no longer in the class `Checkout` calls but behind a hidden translation step. That means one more class to maintain and one more place where bugs can appear (a wrong conversion factor, or rounding differences between kg and lb), and the adapter also has to change whenever `LegacyCarrier` changes its interface.
