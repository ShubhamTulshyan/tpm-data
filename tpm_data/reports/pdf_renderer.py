"""PDF report rendering for TPM campaigns."""

from __future__ import annotations

from pathlib import Path


class PDFRenderer:
    """Render TPM reports as PDF documents."""

    def __init__(self, output_dir: Path | str | None = None) -> None:
        """
        Initialize the PDFRenderer.

        Args:
            output_dir: Directory for PDF output.
        """
        self.output_dir = Path(output_dir) if output_dir else Path.cwd()
        self._rendered_count = 0

    def render(
        self,
        campaign_id: str,
        content: dict,
        filename: str | None = None,
    ) -> str:
        """
        Render a campaign report as PDF.

        Args:
            campaign_id: Campaign identifier.
            content: Content dict with keys like "title", "narrative", etc.
            filename: Optional custom filename (without .pdf extension).

        Returns:
            Path to generated PDF file.
        """
        if not filename:
            filename = f"campaign_{campaign_id}_report"

        output_path = self.output_dir / f"{filename}.pdf"

        # In production, would use reportlab or similar to generate actual PDF
        # For now, create a placeholder file
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w") as f:
            f.write(f"Campaign Report: {campaign_id}\n")
            if "narrative" in content:
                f.write(content["narrative"])

        self._rendered_count += 1
        return str(output_path)

    def get_render_count(self) -> int:
        """
        Get number of rendered PDFs.

        Returns:
            Count of rendered reports.
        """
        return self._rendered_count
