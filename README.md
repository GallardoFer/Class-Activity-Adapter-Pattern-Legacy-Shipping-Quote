# Legacy Shipping Quote Adapter — Starter

Small class activity for the **Adapter** pattern.

`Checkout` expects a `ShippingQuoteProvider` with:

```text
quote(destination, weight_kg)
```

A useful legacy dependency already exists, but exposes:

```text
get_price(postal_code, weight_lb)
```

## Your task

1. Implement `LegacyCarrierAdapter`.
2. Do **not** modify `Checkout`, `ShippingQuoteProvider`, or `LegacyCarrier`.
3. Convert kilograms to pounds inside the Adapter (`1 kg = 2.20462 lb`).
4. Add one focused test proving Checkout can use the legacy carrier through the Target contract.
5. Be ready to name one complexity cost introduced by the Adapter.

Use explicit OO design and keep one main class per source file.

## Team workflow

Only one teammate creates the repository from this template. The team repository must be **public** and everyone works in that same repository.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```
