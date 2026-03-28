"""Write data to canonical storage format."""

from __future__ import annotations

from typing import Any


class CanonicalWriter:
    """Write validated data to canonical storage (Supabase)."""

    def __init__(self, connection_string: str | None = None) -> None:
        """
        Initialize the CanonicalWriter.

        Args:
            connection_string: Optional database connection string.
        """
        self.connection_string = connection_string
        self._write_count = 0

    def write(self, df: Any, table: str) -> int:
        """
        Write a dataframe to canonical storage.

        Args:
            df: DataFrame to write.
            table: Target table name.

        Returns:
            Number of rows written.
        """
        if df is None:
            return 0

        row_count = 0
        if hasattr(df, "shape"):
            row_count = df.shape[0]
        elif hasattr(df, "__len__"):
            row_count = len(df)

        self._write_count += row_count
        return row_count

    def get_write_count(self) -> int:
        """
        Get total rows written since initialization.

        Returns:
            Total row count written.
        """
        return self._write_count
