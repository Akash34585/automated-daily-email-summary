import argparse
from src.summary_reader import get_summary_path, read_summary
from src.email_sender import send_email



def main():
    parser = argparse.ArgumentParser(
        description="Send a daily summary email from a text file."
    )
    parser.add_argument(
        "--file",
        "-f",
        help="Path to the summary file. If omitted, uses summaries/YYYY-MM-DD.txt for today's date.",
    )
    parser.add_argument(
        "--subject",
        "-s",
        help="Email subject. Default: 'Daily Summary YYYY-MM-DD'.",
    )

    args = parser.parse_args()

    # Get file path (either custom or today)
    summary_path = get_summary_path(args.file)
    summary_text = read_summary(summary_path)

    # Default subject if not provided
    if args.subject:
        subject = args.subject
    else:
        subject = f"Daily Summary - {summary_path.stem}"

    # Send email
    send_email(subject, summary_text)
    print(f"Email sent using summary file: {summary_path}")


if __name__ == "__main__":
    main()
