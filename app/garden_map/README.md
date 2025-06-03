# Garden Map Application

This directory contains a simple Flask application demonstrating an interactive map of gardening services.

## Running locally

```bash
pip install -r requirements.txt
python main.py
```

The application listens on port `8080` and exposes two endpoints:

- `/` – serves the interactive map page.
- `/services` – returns service locations in JSON format.

A `Dockerfile` is included for containerized deployment.
