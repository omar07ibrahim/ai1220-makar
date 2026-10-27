"""Collaborative Playlist: the backend. Backend person: write the API here, following CONTRACT.md.

    uv run python backend.py

The server runs on http://127.0.0.1:8000. It also serves index.html at that address, so
the page and the API share one address. API documentation: http://127.0.0.1:8000/docs.
Saving this file restarts the server, and the songs go back to the starting three.

Keep create_app(), the route for "/" and the line app = create_app(): the marking builds
a fresh app with create_app() and opens the page at "/".
"""
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

HERE = Path(__file__).resolve().parent


def create_app() -> FastAPI:
    app = FastAPI(title="Collaborative Playlist")

    # The starting playlist. Rename the keys to the field names of your contract.
    songs = [
        {"id": 1, "title": "Blue Monday", "artist": "New Order", "votes": 3},
        {"id": 2, "title": "Clocks", "artist": "Coldplay", "votes": 1},
        {"id": 3, "title": "Dancing Queen", "artist": "ABBA", "votes": 0},
    ]

    @app.get("/", include_in_schema=False)
    def page():
        return FileResponse(HERE / "index.html")

    # Write your three endpoints here, inside create_app(), for example:
    #
    # @app.get("/...")
    # def all_songs():
    #     return songs

    return app


app = create_app()

if __name__ == "__main__":
    print("Playlist: http://127.0.0.1:8000    API documentation: http://127.0.0.1:8000/docs", flush=True)
    uvicorn.run("backend:app", host="127.0.0.1", port=8000, reload=True)
