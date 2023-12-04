import React, { useState } from 'react';
import { useDropzone } from 'react-dropzone';

const FileUpload = ({ onFileUpload }) => {
  const [uploadedFileName, setUploadedFileName] = useState(null);

  const onDrop = (acceptedFiles) => {
    console.log(acceptedFiles);
    const uploadedFile = acceptedFiles[0]; // single file uploaded
    setUploadedFileName(uploadedFile.name);
    onFileUpload(uploadedFile);
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
