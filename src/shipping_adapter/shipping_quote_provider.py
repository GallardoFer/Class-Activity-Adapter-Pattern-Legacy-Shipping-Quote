from abc import ABC, abstractmethod


class ShippingQuoteProvider(ABC):
    @abstractmethod
    def quote(self, destination: str, weight_kg: float) -> float:
        raise NotImplementedError
