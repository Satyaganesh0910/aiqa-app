import React from 'react';
import { Box, Typography } from '@mui/material';

function App() {
  return (
    <Box sx={{ p: 4, textAlign: 'center' }}>
      <Typography variant="h2" color="primary">
        🤖 Aiqa - AI File Q&A Platform
      </Typography>
      <Typography variant="h5" sx={{ mt: 2 }}>
        Welcome to Aiqa!
      </Typography>
      <Typography variant="body1" sx={{ mt: 2 }}>
        This is the Aiqa application, not the default React app.
      </Typography>
    </Box>
  );
}

export default App; 