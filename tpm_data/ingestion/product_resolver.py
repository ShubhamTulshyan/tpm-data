"""Product name resolution using fuzzy matching."""

from __future__ import annotations

from rapidfuzy import fuzz


class ProductResolver:
    """Resolve raw product names to canonical product identifiers."""

    def __init__(self, threshold: int = 85) -> None:
        """
        Initialize the ProductResolver.

        Args:
            threshold: Minimum fuzzy match score (0-100) for resolution.
        """
        self.threshold = threshold
        self._cache: dict[str, str] = {}

    def resolve(self, raw_name: str) -> str:
        """
        Resolve a raw product name to a canonical form.

        Args:
            raw_name: The raw product name from source data.

        Returns:
            The canonical product identifier.
        """
        if not raw_name or not isinstance(raw_name, str):
            return ""

        if raw_name in self._cache:
            return self._cache[raw_name]

        # Normalize whitespace and case
        normalized = " ".join(raw_name.split()).lower().strip()

        if not normalized:
            return ""

        # For now, return normalized form
        # In production, would match against master product catalog
        result = normalized.upper()
        self._cache[raw_name] = result
        return result

    def similarity(self, name1: str, name2: str) -> int:
        """
        Calculate fuzzy match similarity between two product names.

        Args:
            name1: First product name.
            name2: Second product name.

        Returns:
            Similarity score (0-100).
        """
        return fuzz.token_set_ratio(name1.lower(), name2.lower())

    def clear_cache(self) -> None:
        """Clear the resolution cache."""
        self._cache.clear()
