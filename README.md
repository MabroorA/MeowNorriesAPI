# Meow Norris API 🐱

A Chuck Norris joke API that replaces "Chuck Norris" with "Meow Norris".

## Quick Start

### Prerequisites

Make sure you have Python 3.8+ installed:

```bash
python3 --version
```

### 1. Setup

**Mac/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run

```bash
python run.py
```

### 3. Test

**Mac/Linux:**

```bash
PYTHONPATH=$(pwd) pytest tests/
```

**Windows:**

```bash
set PYTHONPATH=%cd% && pytest tests/
```

Visit: http://127.0.0.1:8000

## API Endpoints

### `GET /`

```json
{ "message": "Are you ready to be entertained?" }
```

### `GET /joke`

```json
{ "joke": "Meow Norris can divide by zero." }
```

## Project Structure

```
app/
├── main.py           # FastAPI app
├── config.py         # Settings
├── api/joke.py       # Joke endpoint
└── services/joke_service.py  # Business logic
tests/test_joke.py    # Tests
```

## Tests Covered

- ✅ Home endpoint
- ✅ Basic joke transformation
- ✅ Case-insensitive replacement
- ✅ Multiple Chuck Norris in one joke
- ✅ Error handling
- ✅ Missing data handling
- Many more can be added but as was instructed to keep project lean, this was limited.
