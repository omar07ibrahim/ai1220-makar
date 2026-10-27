# Playlist API contract

Write this file together, before any code. You both follow it exactly.
Change it later only if you both agree, and send the new file to your partner.

Fill in every line. Write each status as its number, such as 201. Bodies are JSON, in
a ```json block under their line; write none for an empty body. Use the same field
names everywhere. The server runs on http://127.0.0.1:8000 and serves the
page at the same address, so paths are written without host or port, such as /things.

## 1. Get all songs

Method:
Path:
Request body: none
Response status:
Response body (the three starting songs):

## 2. Add a song

Method:
Path:
Request body:
Response status:
Response body:
Error status (title or artist missing or empty):
Error body:

## 3. Vote for a song

Method:
Path (write the song's id as {id}, for example /things/{id}/likes):
Request body: none
Response status:
Response body:
Error status (no song with that id):
Error body:
