"""Lift scoring for promotional campaigns."""

from __future__ import annotations


class LiftScorer:
    """Calculate promotional lift as incremental sales above baseline."""

    def __init__(self) -> None:
        """Initialize the LiftScorer."""
        self._scores: dict[str, float] = {}

    def score(
        self, promo_sales: float, baseline_sales: float, campaign_id: str | None = None
    ) -> float:
        """
        Calculate lift score for a campaign.

        Args:
            promo_sales: Sales during promotional period.
            baseline_sales: Expected baseline sales.
            campaign_id: Optional campaign identifier for caching.

        Returns:
            Lift score (percentage increase above baseline).
        """
        if baseline_sales <= 0:
            return 0.0

        lift = ((promo_sales - baseline_sales) / baseline_sales) * 100

        if campaign_id:
            self._scores[campaign_id] = lift

        return lift

    def get_score(self, campaign_id: str) -> float:
        """
        Retrieve cached lift score.

        Args:
            campaign_id: Campaign identifier.

        Returns:
            Cached lift score or 0.0 if not computed.
        """
        return self._scores.get(campaign_id, 0.0)

    def clear_scores(self) -> None:
        """Clear cached scores."""
        self._scores.clear()
