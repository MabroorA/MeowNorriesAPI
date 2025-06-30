# Meow Norris API 🐱

A Chuck Norris joke API that replaces "Chuck Norris" with "Meow Norris".

## Quick Start

### Prerequisites

**Check if Python is installed:**

```bash
python --version
```

If that doesn't work, try:

```bash
python3 --version
```

**If Python is not installed:**

- **Mac**: Install from [python.org](https://python.org) or use `brew install python`
- **Windows**: Download from [python.org](https://python.org) and check "Add to PATH"

### 1. Setup

**If you have `python3` command:**

```bash
python3 -m venv .venv
```

**If you only have `python` command:**

```bash
python -m venv .venv
```

**Activate virtual environment:**

**Mac/Linux:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**If `pip` command fails, try:**

```bash
python -m pip install -r requirements.txt
```

### 2. Run

```bash
python3 run.py
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
