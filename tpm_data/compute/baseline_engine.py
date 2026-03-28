"""Baseline calculation engine for promotional analysis."""

from __future__ import annotations


class BaselineEngine:
    """Calculate baseline sales for products using statistical methods."""

    def __init__(self, method: str = "mean") -> None:
        """
        Initialize the BaselineEngine.

        Args:
            method: Baseline calculation method ("mean", "median", "trend").
        """
        self.method = method
        self._baselines: dict[str, float] = {}

    def compute_baseline(
        self, product_id: str, historical_sales: list[float] | None = None
    ) -> float:
        """
        Compute baseline sales for a product.

        Args:
            product_id: Product identifier.
            historical_sales: Historical sales data for the product.

        Returns:
            Baseline sales value.
        """
        if product_id in self._baselines:
            return self._baselines[product_id]

        if not historical_sales or len(historical_sales) == 0:
            return 0.0

        if self.method == "mean":
            baseline = sum(historical_sales) / len(historical_sales)
        elif self.method == "median":
            sorted_sales = sorted(historical_sales)
            mid = len(sorted_sales) // 2
            baseline = (
                sorted_sales[mid]
                if len(sorted_sales) % 2 == 1
                else (sorted_sales[mid - 1] + sorted_sales[mid]) / 2
            )
        else:
            # Default to mean
            baseline = sum(historical_sales) / len(historical_sales)

        self._baselines[product_id] = baseline
        return baseline

    def get_baseline(self, product_id: str) -> float:
        """
        Retrieve cached baseline for a product.

        Args:
            product_id: Product identifier.

        Returns:
            Baseline value or 0.0 if not computed.
        """
        return self._baselines.get(product_id, 0.0)
