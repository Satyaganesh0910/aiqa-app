import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'https://aiqa-app-7.onrender.com';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add token to requests if available
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Auth API
export const authAPI = {
  signup: async (email: string, password: string) => {
    // Backend requires username, email, password. Use email as username for simplicity.
    const response = await api.post('/auth/signup', { username: email, email, password });
    return response.data;
  },
  
  login: async (email: string, password: string) => {
    // Backend expects OAuth2PasswordRequestForm (form-encoded) with fields: username, password
    const form = new URLSearchParams();
    form.append('username', email);
    form.append('password', password);
    const response = await api.post('/auth/login', form, {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    });
    return response.data;
  },
};

// File Upload API
export const fileAPI = {
  upload: async (file: File) => {
    const formData = new FormData();
    formData.append('file', file);
    
    const response = await api.post('/files/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  },
};

// Chat API
export const chatAPI = {
  ask: async (question: string, fileId?: string) => {
    const response = await api.post('/chat/ask', { 
      question, 
      file_id: fileId 
    });
    return response.data;
  },
};

export default api;
