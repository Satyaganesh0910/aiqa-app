import React, { useState, useCallback } from 'react';
import {
  Box,
  Button,
  Typography,
  Paper,
  Container,
  Alert,
  LinearProgress,
  List,
  ListItem,
  ListItemText,
  ListItemIcon,
  IconButton,
} from '@mui/material';
import {
  CloudUpload,
  InsertDriveFile,
  Delete,
  CheckCircle,
  Error,
} from '@mui/icons-material';
import { useDropzone } from 'react-dropzone';
import { fileAPI } from '../api/api';

interface UploadedFile {
  id: string;
  name: string;
  status: 'uploading' | 'success' | 'error';
  error?: string;
}

const FileUpload: React.FC = () => {
  const [uploadedFiles, setUploadedFiles] = useState<UploadedFile[]>([]);
  const [error, setError] = useState<string>('');

  const onDrop = useCallback(async (acceptedFiles: File[]) => {
    setError('');
    
    for (const file of acceptedFiles) {
      const fileId = Math.random().toString(36).substr(2, 9);
      
      // Add file to list with uploading status
      setUploadedFiles(prev => [...prev, {
        id: fileId,
        name: file.name,
        status: 'uploading'
      }]);

      try {
        await fileAPI.upload(file);
        
        // Update file status to success
        setUploadedFiles(prev => prev.map(f => 
          f.id === fileId ? { ...f, status: 'success' } : f
        ));
      } catch (err: any) {
        // Update file status to error
        setUploadedFiles(prev => prev.map(f => 
          f.id === fileId ? { 
            ...f, 
            status: 'error', 
            error: err.response?.data?.detail || 'Upload failed' 
          } : f
        ));
        setError('Some files failed to upload. Please try again.');
      }
    }
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'application/pdf': ['.pdf'],
      'image/*': ['.png', '.jpg', '.jpeg'],
      'text/plain': ['.txt'],
    },
    multiple: true,
  });

  const removeFile = (fileId: string) => {
    setUploadedFiles(prev => prev.filter(f => f.id !== fileId));
  };

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'uploading':
        return <LinearProgress sx={{ width: 20, height: 20 }} />;
      case 'success':
        return <CheckCircle color="success" />;
      case 'error':
        return <Error color="error" />;
      default:
        return <InsertDriveFile />;
    }
  };

  return (
    <Container maxWidth="md">
      <Box sx={{ mt: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom>
          Upload Files
        </Typography>
        <Typography variant="body1" color="text.secondary" sx={{ mb: 3 }}>
          Upload PDFs, images, or text files to ask questions about their content
        </Typography>

        {error && (
          <Alert severity="error" sx={{ mb: 2 }}>
            {error}
          </Alert>
        )}

        <Paper
          {...getRootProps()}
          sx={{
            border: '2px dashed',
            borderColor: isDragActive ? 'primary.main' : 'grey.300',
            borderRadius: 2,
            p: 4,
            textAlign: 'center',
            cursor: 'pointer',
            backgroundColor: isDragActive ? 'action.hover' : 'background.paper',
            transition: 'all 0.2s ease',
            '&:hover': {
              borderColor: 'primary.main',
              backgroundColor: 'action.hover',
            },
          }}
        >
          <input {...getInputProps()} />
          <CloudUpload sx={{ fontSize: 48, color: 'primary.main', mb: 2 }} />
          <Typography variant="h6" gutterBottom>
            {isDragActive ? 'Drop files here' : 'Drag & drop files here'}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            or click to select files
          </Typography>
          <Typography variant="caption" display="block" sx={{ mt: 1 }}>
            Supported formats: PDF, PNG, JPG, JPEG, TXT
          </Typography>
        </Paper>

        {uploadedFiles.length > 0 && (
          <Paper sx={{ mt: 3, p: 2 }}>
            <Typography variant="h6" gutterBottom>
              Uploaded Files
            </Typography>
            <List>
              {uploadedFiles.map((file) => (
                <ListItem
                  key={file.id}
                  secondaryAction={
                    <IconButton
                      edge="end"
                      onClick={() => removeFile(file.id)}
                      disabled={file.status === 'uploading'}
                    >
                      <Delete />
                    </IconButton>
                  }
                >
                  <ListItemIcon>
                    {getStatusIcon(file.status)}
                  </ListItemIcon>
                  <ListItemText
                    primary={file.name}
                    secondary={file.error || (file.status === 'success' ? 'Upload successful' : 'Uploading...')}
                  />
                </ListItem>
              ))}
            </List>
          </Paper>
        )}
      </Box>
    </Container>
  );
};

export default FileUpload; 