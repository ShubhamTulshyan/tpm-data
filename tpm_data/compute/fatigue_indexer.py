"""Promotional fatigue indexing and tracking."""

from __future__ import annotations


class FatigueIndexer:
    """Calculate and track promotional fatigue for products and categories."""

    def __init__(self) -> None:
        """Initialize the FatigueIndexer."""
        self._fatigue_scores: dict[str, float] = {}
        self._promo_counts: dict[str, int] = {}

    def index(self, product_id: str, promotion_frequency: int) -> float:
        """
        Calculate fatigue index based on promotion frequency.

        Args:
            product_id: Product identifier.
            promotion_frequency: Number of promotions in period.

        Returns:
            Fatigue index score (0-100, where 100 is highest fatigue).
        """
        # Simple model: fatigue increases with promotion count
        # Normalize to 0-100 scale
        fatigue = min(promotion_frequency * 10.0, 100.0)

        self._fatigue_scores[product_id] = fatigue
        self._promo_counts[product_id] = promotion_frequency

        return fatigue

    def get_fatigue(self, product_id: str) -> float:
        """
        Get cached fatigue score.

        Args:
            product_id: Product identifier.

        Returns:
            Fatigue index or 0.0 if not computed.
        """
        return self._fatigue_scores.get(product_id, 0.0)

    def get_promo_count(self, product_id: str) -> int:
        """
        Get promotion count for a product.

        Args:
            product_id: Product identifier.

        Returns:
            Number of promotions or 0 if not tracked.
        """
        return self._promo_counts.get(product_id, 0)

    def clear_index(self) -> None:
        """Clear all fatigue data."""
        self._fatigue_scores.clear()
        self._promo_counts.clear()
