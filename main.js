const fileSelector = document.querySelector("#teeth-photos");
const submit_button = document.querySelector("#submit")
const preview = document.querySelector(".preview")
const email = document.querySelector("#email")



const getSize = (item) => {
  if (item < 1e3) {
    return `${item} Bytes`
  }
  else if (item < 1e6) {
    return `${Math.round((item / 1e3) * 10) / 10} KBytes`
  }
  else if (item < 1e9) {
    return `${Math.round((item / 1e6) * 10) / 10} MBytes`

  }
}

function arrayBufferToBase64(arrBuffer) {

  //convert to uint8 since arrayBuffer is generic binary buffer
  const uint8Buffer = new Uint8Array(arrBuffer)
  
  //convert each byte to string from specified utf-16 code units
  let binary = '';

  uint8Buffer.forEach((byte)=> {binary+=String.fromCharCode(byte)});

  //craetes a Base64-encoded ASCII string from binary string (= string whose characters are treated as binary data)
  return window.btoa(binary)

}



submit_button.addEventListener('click', async (event) => {
  event.preventDefault()

  const formData = new FormData();
  // Add data to the FormData object
  formData.append('username', 'John Doe');
  formData.append('password', 'randompwd')
  formData.append('files', fileSelector.files)
  // get the data that were attached
  console.log("sending axios request")

  console.log(fileSelector.files)


  for (let file of fileSelector.files) {
    try {

      const arrBuffer = await file.arrayBuffer()
      /*
      ArrayBuffer is not a JSON-compatible structure: JSON itself cannot directly serialize ArrayBuffer (or binary data). 
      Binary data needs to be either encoded (e.g., with Base64 encoding) or transmitted as part of a multipart form (multipart/form-data).
      */
      console.log(file)
      const postObj = {"email": email.value, "filename": file.name, "images": arrayBufferToBase64(arrBuffer)}
       // buffer array containing raw binary data
      //const objToSend = {"filename": file.name, "bytedata": arrBuffer}
      //const bytes = new Uint8Array(arrBuffer) // convert every 8 bits to integer
      //console.log("Trying to send...", objToSend.filename, arrBuffer)
      const response = await axios.post("http://localhost:8000/upload", postObj, {headers:{
        "Content-Type": "application/json"
      }});



      console.log(response.data);
    } catch (error) {
      console.error(error);
    }

  }


})




email.addEventListener('change', async() => {

  if (fileSelector.files.length != 0){
    submit_button.disabled = false

  }
})



fileSelector.addEventListener('change', async (event) => {


  // Tasks to manage while there are changes in the fileSelctor
  // 1. Get FileList
  const selectedFiles = fileSelector.files  //object "FileList" w/list of selected files

  if (selectedFiles.length == 0) {
   submit_button.disabled = true

  } else {  // files were selected
    console.log("creating list")
    createListPhotos()
  
    if (email.value){
      console.log(email.value)
      submit_button.disabled = false
    }


  }


function createListPhotos(){
  // 2. Loops through the FileList and create a list of uploaded items (not styled yet)

  const itemList = document.createElement("item-list")


  for (let file of selectedFiles) {

    console.log("Looping through :", file)
    let newItem = document.createElement("item")

    let contentItem = document.createElement("div")
    contentItem.className = "item-el"
    contentItem.innerText = `${file.name} (${getSize(file.size)})`

    newItem.appendChild(contentItem)


    let img = document.createElement("img");
    img.className = "item-el"
    img.src = URL.createObjectURL(file);

    img.onload = () => {
      console.log("Onload", img.naturalHeight, img.naturalWidth)
    }
    newItem.appendChild(img)


    itemList.append(newItem)


  }
  // 3. Add a list item with overview abouyt the filename (filesize) and image (url)
  preview.innerText = "Files uploaded:"
  preview.append()
  preview.append(itemList)
}



});

