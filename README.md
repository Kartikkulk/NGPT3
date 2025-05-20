# NeuroGPT Chainlit Chat Interface

A modern chat interface for NeuroGPT built with Chainlit.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file (if needed):
```bash
WEBHOOK_URL=your_webhook_url
```

## Running the Application

1. Start the Chainlit server:
```bash
chainlit run app.py
```

2. Open your browser and navigate to:
```
http://localhost:8000
```

## Features

- Modern chat interface
- Real-time responses
- Markdown support
- Table rendering
- Code block formatting
- Context-aware conversations
- Session management

## Configuration

The application uses the following configuration:

- Webhook URL: Configured in `app.py`
- Session management: Automatic session ID generation
- Context window: Last 5 messages
- Message formatting: Markdown support

## Development

To modify the application:

1. Edit `app.py` for main functionality
2. Edit `chainlit.md` for welcome page content
3. Edit `requirements.txt` for dependencies 