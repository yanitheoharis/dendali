15 Dec 2024:

- Initial commit with basic functionality for uploading and viewing photo



12 Jan 2024:

- Frontend:
    - Can support sending image data to server using axios
- Setup backend
    - Can receive uploaded images on the client side as byte stream (both as raw byte and form/file data)
    - Saves the uploaded images locally




ToDo
- send one request with multiple images instead of individual request per image
- save and check unique filename (w/ shape info?)
- pass also name/email of user who uploaded
- validation (security checks)