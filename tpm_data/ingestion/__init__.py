"""Ingestion module for TPM data pipeline."""

from __future__ import annotations

from tpm_data.ingestion.canonical_writer import CanonicalWriter
from tpm_data.ingestion.format_detector import FormatDetector
from tpm_data.ingestion.product_resolver import ProductResolver
from tpm_data.ingestion.validator import DataValidator

__all__ = [
    "CanonicalWriter",
    "FormatDetector",
    "ProductResolver",
    "DataValidator",
]
