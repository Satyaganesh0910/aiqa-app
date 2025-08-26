import React, { useState } from 'react';
import { Box, Typography, Paper, Tabs, Tab } from '@mui/material';
import Signup from './pages/Signup';
import Login from './pages/Login';

function App() {
  const [tab, setTab] = useState(0);

  return (
    <Box sx={{ p: 4, maxWidth: 520, mx: 'auto' }}>
      <Typography variant="h4" color="primary" sx={{ textAlign: 'center', mb: 2 }}>
        🤖 Aiqa - AI File Q&A
      </Typography>
      <Paper elevation={3} sx={{ p: 2 }}>
        <Tabs value={tab} onChange={(_, v) => setTab(v)} centered>
          <Tab label="Sign Up" />
          <Tab label="Sign In" />
        </Tabs>
        <Box sx={{ mt: 2 }}>
          {tab === 0 ? (
            <Signup onSignupSuccess={() => setTab(1)} onSwitchToLogin={() => setTab(1)} />
          ) : (
            <Login onLoginSuccess={() => { /* TODO: route to app */ }} onSwitchToSignup={() => setTab(0)} />
          )}
        </Box>
      </Paper>
    </Box>
  );
}

export default App; 