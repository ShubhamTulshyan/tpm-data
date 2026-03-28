"""Data validation for TPM pipeline."""

from __future__ import annotations

from typing import Any


class DataValidator:
    """Validate TPM data frames and raise validation errors."""

    def __init__(self) -> None:
        """Initialize the DataValidator."""
        self.required_columns: set[str] = {"product_id", "date", "sales", "promo_flag"}

    def validate(self, df: Any) -> list[str]:
        """
        Validate a data frame.

        Args:
            df: DataFrame to validate (pandas or polars).

        Returns:
            List of validation error messages. Empty if valid.
        """
        errors: list[str] = []

        # Check if it's a dataframe
        if df is None:
            errors.append("DataFrame is None")
            return errors

        # Check for required columns (duck typing)
        if hasattr(df, "columns"):
            columns = set(df.columns)
            missing = self.required_columns - columns
            if missing:
                errors.append(f"Missing required columns: {missing}")
        else:
            errors.append("Input does not appear to be a DataFrame")
            return errors

        # Check for empty dataframe
        if hasattr(df, "shape"):
            if df.shape[0] == 0:
                errors.append("DataFrame is empty")

        # Check for null values in critical columns
        if hasattr(df, "isnull"):
            for col in self.required_columns:
                if col in columns:
                    if df[col].isnull().any():
                        errors.append(f"Column '{col}' contains null values")

        return errors

    def set_required_columns(self, columns: set[str]) -> None:
        """
        Set the required columns for validation.

        Args:
            columns: Set of required column names.
        """
        self.required_columns = columns
