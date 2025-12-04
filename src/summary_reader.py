from pathlib import Path
from datetime import date


def get_summary_path(custom_path: str | None = None) -> Path:
    """
    If custom_path is given, use that.
    Otherwise default to summaries/YYYY-MM-DD.txt for today's date.
    """
    if custom_path:
        return Path(custom_path)

    today_str = date.today().isoformat()  # e.g. "2025-12-04"
    return Path("summaries") / f"{today_str}.txt"


def read_summary(summary_path: Path) -> str:
    if not summary_path.exists():
        raise FileNotFoundError(f"Summary file not found: {summary_path}")

    return summary_path.read_text(encoding="utf-8")
