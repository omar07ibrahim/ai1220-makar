# Playlist API contract

Write this file together, before any code. You both follow it exactly.
Change it later only if you both agree, and send the new file to your partner.

Fill in every line. Write each status as its number, such as 201. Bodies are JSON, in
a ```json block under their line; write none for an empty body. Use the same field
names everywhere. The server runs on http://127.0.0.1:8000 and serves the
page at the same address, so paths are written without host or port, such as /things.

Field names (snake_case, the same in every request and response): `id` (integer),
`title` (string), `artist` (string), `votes` (integer), `error` (string).

## 1. Get all songs

Method: GET
Path: /songs
Request body: none
Response status: 200
Response body (the three starting songs):
```json
[
  {"id": 1, "title": "Blue Monday", "artist": "New Order", "votes": 3},
  {"id": 2, "title": "Clocks", "artist": "Coldplay", "votes": 1},
  {"id": 3, "title": "Dancing Queen", "artist": "ABBA", "votes": 0}
]
```

## 2. Add a song

Method: POST
Path: /songs
Request body:
```json
{"title": "Hey Jude", "artist": "The Beatles"}
```
Response status: 201
Response body:
```json
{"id": 4, "title": "Hey Jude", "artist": "The Beatles", "votes": 0}
```
Error status (title or artist missing or empty): 400
Error body:
```json
{"error": "Please enter both a title and an artist"}
```

## 3. Vote for a song

Method: POST
Path (write the song's id as {id}, for example /things/{id}/likes): /songs/{id}/votes
Request body: none
Response status: 200
Response body:
```json
{"id": 1, "title": "Blue Monday", "artist": "New Order", "votes": 4}
```
Error status (no song with that id): 404
Error body:
```json
{"error": "There is no song 99999"}
```
