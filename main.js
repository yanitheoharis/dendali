const fileSelector = document.querySelector("#teeth-photos");
const submit_button = document.querySelector("#submit")
const preview = document.querySelector(".preview")




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


submit_button.addEventListener('click', async (event) => {


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

      const arrBuffer = await file.arrayBuffer() // buffer array containing raw binary data
      //const objToSend = {"filename": file.name, "bytedata": arrBuffer}
      //const bytes = new Uint8Array(arrBuffer) // convert every 8 bits to integer
      //console.log("Trying to send...", objToSend.filename, arrBuffer)
      const response = await axios.post("http://localhost:8000/upload", arrBuffer);


      console.log(response.data);
    } catch (error) {
      console.error(error);
    }

  }


})

fileSelector.addEventListener('change', async (event) => {


  // Tasks to manage while there are changes in the fileSelctor
  // 1. Get FileList
  const selectedFiles = fileSelector.files  //object "FileList" w/list of selected files

  if (selectedFiles.length == 0) {
    // If no files, show "no files selected" - this is already provided by default, is it needed here?

    /*
    const noFilesEl = document.createElement("no-files")
    noFilesEl.innerHTML = "No files selected"
    preview.append(noFilesEl)
    */

  } else {  // files were selected

    // 2. Loops through the FileList and 

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





  /*
  console.log(selectedFiles)

  const fileReader = new FileReader()

  const arrBuffer = await selectedFiles[0].arrayBuffer() // buffer array containing raw binary data
  const bytes = new Int8Array(arrBuffer) // convert every 8 bits to integer

  console.log(bytes)

  const img = document.createElement("img");
  img.src = URL.createObjectURL(selectedFiles[0]);
  img.height = 60;
  preview.appendChild(img)
  //const fileList = event.target.files;
  //console.log(fileList);
  */
});



/*
const getFileName = () => {uploaded_file.value.split("\\").at(-1) }


const getFileData = () => { console.log(uploaded_file.value) }
submit_button.addEventListener('click', getFileData)


console.log(uploaded_file.value)

*/