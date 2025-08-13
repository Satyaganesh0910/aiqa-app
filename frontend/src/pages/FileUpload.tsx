import React, { useState } from 'react';
import { Box, Typography, Button, Paper, LinearProgress, List, ListItem, ListItemText, AppBar, Toolbar } from '@mui/material';
import { CloudUpload, Chat, Logout } from '@mui/icons-material';
import { useNavigate } from 'react-router-dom';
import api from '../api';

interface UploadedFile {
  filename: string;
  file_id: string;
  extracted_text: string;
}

const FileUpload: React.FC = () => {
  const [uploading, setUploading] = useState(false);
  const [uploadedFiles, setUploadedFiles] = useState<UploadedFile[]>([]);
  const navigate = useNavigate();

  const handleFileUpload = async (files: FileList | null) => {
    if (!files) return;
    
    setUploading(true);
    const newFiles: UploadedFile[] = [];
    
    for (let i = 0; i < files.length; i++) {
      const file = files[i];
      const formData = new FormData();
      formData.append('file', file);
      
      try {
        const response = await api.post('/files/upload', formData, {
          headers: { 'Content-Type': 'multipart/form-data' }
        });
        newFiles.push(response.data);
      } catch (error) {
        console.error('Upload failed:', error);
      }
    }
    
    setUploadedFiles(prev => [...prev, ...newFiles]);
    setUploading(false);
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    handleFileUpload(e.dataTransfer.files);
  };

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    navigate('/login');
  };

  return (
    <Box sx={{ minHeight: '100vh', backgroundColor: '#f5f5f5' }}>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            🤖 Aiqa
          </Typography>
          <Button color="inherit" startIcon={<Chat />} onClick={() => navigate('/chat')}>
            Chat
          </Button>
          <Button color="inherit" startIcon={<Logout />} onClick={handleLogout}>
            Logout
          </Button>
        </Toolbar>
      </AppBar>

      <Box maxWidth={800} mx="auto" mt={4} p={2}>
        <Typography variant="h4" mb={3}>Upload Files</Typography>
        
        <Paper
          sx={{
            p: 3,
            textAlign: 'center',
            border: '2px dashed #ccc',
            mb: 3
          }}
          onDrop={handleDrop}
          onDragOver={handleDragOver}
        >
          <CloudUpload sx={{ fontSize: 48, color: 'primary.main', mb: 2 }} />
          <Typography variant="h6" mb={2}>
            Drag and drop files here or click to select
          </Typography>
          <Typography variant="body2" color="textSecondary" mb={2}>
            Supported formats: PDF, PNG, JPG, JPEG, TXT
          </Typography>
          <Button
            variant="contained"
            component="label"
            disabled={uploading}
          >
            Select Files
            <input
              type="file"
              multiple
              accept=".pdf,.png,.jpg,.jpeg,.txt"
              style={{ display: 'none' }}
              onChange={(e) => handleFileUpload(e.target.files)}
            />
          </Button>
        </Paper>

        {uploading && (
          <Box mb={3}>
            <Typography variant="body2" mb={1}>Uploading...</Typography>
            <LinearProgress />
          </Box>
        )}

        {uploadedFiles.length > 0 && (
          <Box>
            <Typography variant="h6" mb={2}>Uploaded Files</Typography>
            <List>
              {uploadedFiles.map((file, index) => (
                <ListItem key={index} divider>
                  <ListItemText
                    primary={file.filename}
                    secondary={
                      <Box>
                        <Typography variant="body2" color="textSecondary">
                          File ID: {file.file_id}
                        </Typography>
                        {file.extracted_text && (
                          <Typography variant="body2" sx={{ mt: 1 }}>
                            Extracted Text: {file.extracted_text}
                          </Typography>
                        )}
                      </Box>
                    }
                  />
                </ListItem>
              ))}
            </List>
            <Button
              variant="contained"
              startIcon={<Chat />}
              onClick={() => navigate('/chat')}
              sx={{ mt: 2 }}
            >
              Start Chatting
            </Button>
          </Box>
        )}
      </Box>
    </Box>
  );
};

export default FileUpload; 