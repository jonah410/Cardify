import React, { useState } from 'react';
import { useDropzone } from 'react-dropzone';

const FileUpload = () => {
  const [uploadedFileName, setUploadedFileName] = useState(null);

  const onDrop = (acceptedFiles) => {
    // Handle the uploaded files here
    console.log(acceptedFiles);
    // Assume the upload was successful for demonstration purposes
    const uploadedFile = acceptedFiles[0]; // Assuming only one file is uploaded
    setUploadedFileName(uploadedFile.name);
    const formData = new FormData();
    formData.append('file', uploadedFile);
    fetch('http://your-backend-api/upload', {
      method: 'POST',
      body: formData,
    })
    .then(response => response.json())
    .then(data => {
      console.log(data); // Handle the response from the backend
    })
    .catch(error => {
      console.error(error); // Handle errors
    });
  };

  const { getRootProps, getInputProps } = useDropzone({ onDrop });

  return (
    <div>
      <div {...getRootProps()} style={dropzoneStyles}>
        <input {...getInputProps()} />
        <p>Drag & drop PDF files here, or click to select files</p>
      </div>
      {uploadedFileName && <p>File '{uploadedFileName}' uploaded successfully!</p>}
    </div>
  );
};

const dropzoneStyles = {
  border: '2px dashed #cccccc',
  borderRadius: '4px',
  padding: '20px',
  textAlign: 'center',
  cursor: 'pointer',
};

export default FileUpload;
