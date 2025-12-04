Automated Daily Summary Email Sender

A simple Python tool to email yourself (or someone else) a daily summary from a text file.

How it works

- You write your daily summary in a `.txt` file (e.g. `summaries/2025-12-04.txt`)
- The script reads the file content
- It sends the content as an email using SMTP (Gmail by default)

Setup

1. Create and activate a virtual environment:

```
python -m venv .venv
.venv\Scripts\activate  # Windows
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:

```
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=465
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password_here
EMAIL_TO=receiver_email@gmail.com
```

> Use an **app password** if you're using Gmail.

4. Create a summary file, for example:

`summaries/2025-12-04.txt`

5. Run the script:

```
python -m src.main --file summaries/2025-12-04.txt --subject "Daily Summary - 2025-12-04"
```

If `--file` is not provided, the script will look for:

`summaries/YYYY-MM-DD.txt` for today's date.

Future ideas

- Automatically generate summary from logs or todo app
- Schedule it via cron / Windows Task Scheduler
- HTML email formatting

