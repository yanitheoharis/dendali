15 Dec 2024:

- Initial commit with basic functionality for uploading and viewing photo



12 Jan 2025:

- Frontend:
    - Can support sending image data to server using axios
- Setup backend
    - Can receive uploaded images on the client side as byte stream (both as raw byte and form/file data)
    - Saves the uploaded images locally

18 Jan 2025:
- Frontend
    - Submit button ui (disabling by default until all info is there)
    - Updated axios request to include email, filename and base64 encoded binary data
- Backend
    - Receive updated request structure
    - Create unique folder for each user & saved images by filename


ToDo
- datamodels
- testing of encoding steps
- multiple post requests served (i.e., multiple images) -> single or multiple request
- check uniqueness of uploaded image (w/ shape info?) -> done by 
- validation (security checks)