"""Generate narrative insights from TPM analysis."""

from __future__ import annotations


class NarrativeGenerator:
    """Generate executive narratives from TPM data analysis."""

    def __init__(self) -> None:
        """Initialize the NarrativeGenerator."""
        self._narratives: dict[str, str] = {}

    def generate(
        self,
        campaign_id: str,
        lift: float,
        roi: float,
        fatigue: float,
    ) -> str:
        """
        Generate narrative insights for a campaign.

        Args:
            campaign_id: Campaign identifier.
            lift: Lift score percentage.
            roi: ROI percentage.
            fatigue: Fatigue index score.

        Returns:
            Generated narrative string.
        """
        narrative_parts = []

        narrative_parts.append(f"Campaign {campaign_id} Analysis:")

        if lift > 0:
            narrative_parts.append(f"Achieved {lift:.1f}% lift vs. baseline.")
        else:
            narrative_parts.append("Did not achieve positive lift.")

        if roi > 0:
            narrative_parts.append(f"Generated {roi:.1f}% ROI on promotional spend.")
        else:
            narrative_parts.append("ROI was negative or zero.")

        if fatigue < 30:
            narrative_parts.append("Promotional fatigue is low.")
        elif fatigue < 70:
            narrative_parts.append("Moderate promotional fatigue detected.")
        else:
            narrative_parts.append("High promotional fatigue risk.")

        narrative = " ".join(narrative_parts)
        self._narratives[campaign_id] = narrative

        return narrative

    def get_narrative(self, campaign_id: str) -> str:
        """
        Retrieve cached narrative.

        Args:
            campaign_id: Campaign identifier.

        Returns:
            Generated narrative or empty string.
        """
        return self._narratives.get(campaign_id, "")
