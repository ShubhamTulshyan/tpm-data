"""Tests for format detector module."""

from __future__ import annotations

import pytest

from tpm_data.ingestion.format_detector import FormatDetector


class TestFormatDetector:
    """Test suite for FormatDetector."""

    def test_instantiation(self) -> None:
        """Test that FormatDetector can be instantiated."""
        detector = FormatDetector()
        assert detector is not None

    def test_detect_csv(self, tmp_path) -> None:
        """Test detection of CSV format."""
        detector = FormatDetector()
        csv_file = tmp_path / "data.csv"
        csv_file.touch()

        result = detector.detect(csv_file)
        assert isinstance(result, str)
        assert result == "csv"

    def test_detect_xlsx(self, tmp_path) -> None:
        """Test detection of XLSX format."""
        detector = FormatDetector()
        xlsx_file = tmp_path / "data.xlsx"
        xlsx_file.touch()

        result = detector.detect(xlsx_file)
        assert isinstance(result, str)
        assert result == "xlsx"

    def test_detect_parquet(self, tmp_path) -> None:
        """Test detection of Parquet format."""
        detector = FormatDetector()
        parquet_file = tmp_path / "data.parquet"
        parquet_file.touch()

        result = detector.detect(parquet_file)
        assert isinstance(result, str)
        assert result == "parquet"

    def test_detect_unsupported_format(self, tmp_path) -> None:
        """Test that unsupported format raises ValueError."""
        detector = FormatDetector()
        unknown_file = tmp_path / "data.unknown"
        unknown_file.touch()

        with pytest.raises(ValueError, match="Unsupported file format"):
            detector.detect(unknown_file)

    def test_detect_returns_string(self, tmp_path) -> None:
        """Test that detect always returns a string type."""
        detector = FormatDetector()
        json_file = tmp_path / "data.json"
        json_file.touch()

        result = detector.detect(json_file)
        assert isinstance(result, str)
