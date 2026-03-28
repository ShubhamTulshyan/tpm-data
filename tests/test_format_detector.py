"""Tests for format detector module."""

from __future__ import annotations

from pathlib import Path

import pytest

from tpm_data.ingestion.format_detector import FormatDetector


class TestFormatDetector:
    """Test suite for FormatDetector."""

    def test_instantiation(self) -> None:
        """Test that FormatDetector can be instantiated."""
        detector = FormatDetector()
        assert detector is not None

    @pytest.mark.parametrize(
        ("extension", "expected_format"),
        [
            (".csv", "csv"),
            (".xlsx", "xlsx"),
            (".xls", "xls"),
            (".parquet", "parquet"),
            (".pq", "parquet"),
            (".json", "json"),
            (".jsonl", "jsonl"),
        ],
    )
    def test_detect_supported_formats(
        self, tmp_path: Path, extension: str, expected_format: str
    ) -> None:
        """Test detection of all supported file formats."""
        detector = FormatDetector()
        data_file = tmp_path / f"data{extension}"
        data_file.touch()

        result = detector.detect(data_file)
        assert isinstance(result, str)
        assert result == expected_format

    def test_detect_unsupported_format(self, tmp_path: Path) -> None:
        """Test that unsupported format raises ValueError."""
        detector = FormatDetector()
        unknown_file = tmp_path / "data.unknown"
        unknown_file.touch()

        with pytest.raises(ValueError, match="Unsupported file format"):
            detector.detect(unknown_file)

    def test_detect_accepts_string_path(self, tmp_path: Path) -> None:
        """Test that detect works with string paths, not just Path objects."""
        detector = FormatDetector()
        csv_file = tmp_path / "data.csv"
        csv_file.touch()

        result = detector.detect(str(csv_file))  # type: ignore[arg-type]
        assert result == "csv"

    def test_detect_case_insensitive_extension(self, tmp_path: Path) -> None:
        """Test that detection is case-insensitive for file extensions."""
        detector = FormatDetector()
        csv_file = tmp_path / "data.CSV"
        csv_file.touch()

        result = detector.detect(csv_file)
        assert result == "csv"
