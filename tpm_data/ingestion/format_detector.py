"""Format detection for TPM data files."""

from __future__ import annotations

from pathlib import Path


class FormatDetector:
    """Detect file format based on extension and content."""

    def detect(self, file_path: Path) -> str:
        """
        Detect the format of a data file.

        Args:
            file_path: Path to the file to detect.

        Returns:
            Format string ("csv", "xlsx", "parquet", etc.).

        Raises:
            ValueError: If format cannot be determined.
        """
        if not isinstance(file_path, Path):
            file_path = Path(file_path)

        suffix = file_path.suffix.lower()

        format_map = {
            ".csv": "csv",
            ".xlsx": "xlsx",
            ".xls": "xls",
            ".parquet": "parquet",
            ".pq": "parquet",
            ".json": "json",
            ".jsonl": "jsonl",
        }

        if suffix not in format_map:
            raise ValueError(f"Unsupported file format: {suffix}")

        return format_map[suffix]
