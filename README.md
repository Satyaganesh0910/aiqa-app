# 🤖 Aiqa - AI-Powered File Q&A Platform

Aiqa is a full-stack web application that allows users to upload documents (PDFs, images, text files) and ask questions about their content using AI. Built with FastAPI backend and React frontend.

## ✨ Features

- **🔐 User Authentication**: Secure signup/login with JWT tokens
- **📁 File Upload**: Support for PDF, PNG, JPG, JPEG, and TXT files
- **🤖 AI Text Extraction**: Automatic text extraction from uploaded files
- **💬 Chat Interface**: ChatGPT-style Q&A about uploaded documents
- **🎨 Modern UI**: Beautiful Material-UI design with responsive layout
- **🔒 Protected Routes**: Secure access to authenticated features

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - Database ORM
- **SQLite** - Database (can be upgraded to PostgreSQL)
- **PyPDF2** - PDF text extraction
- **Pillow** - Image processing
- **pytesseract** - OCR for images
- **JWT** - Authentication

### Frontend
- **React** - UI framework
- **TypeScript** - Type safety
- **Material-UI** - Component library
- **React Router** - Navigation
- **Formik + Yup** - Form handling and validation
- **Axios** - HTTP client

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

### Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the FastAPI server**:
   ```bash
   uvicorn app.main:app --reload
   ```

   The backend will be available at: http://localhost:8000
   API documentation: http://localhost:8000/docs

### Frontend Setup

1. **Navigate to frontend directory**:
   ```bash
   cd backend/frontend
   ```

2. **Install Node.js dependencies**:
   ```bash
   npm install
   ```

3. **Start the React development server**:
   ```bash
   npm start
   ```

   The frontend will be available at: http://localhost:3000

## 📖 Usage

1. **Sign Up/Login**: Create an account or login with existing credentials
2. **Upload Files**: Drag and drop or select files (PDF, images, text)
3. **Chat with AI**: Ask questions about your uploaded documents
4. **Get Answers**: Receive AI-powered responses based on your files

## 🔧 API Endpoints

### Authentication
- `POST /auth/signup` - User registration
- `POST /auth/login` - User login

### File Management
- `POST /files/upload` - Upload files with text extraction

### Chat
- `POST /chat/ask` - Ask questions about uploaded files

## 🏗️ Project Structure

```
Aiqa/
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI app entry point
│   │   ├── models.py        # Database models
│   │   ├── database.py      # Database configuration
│   │   ├── auth.py          # Authentication logic
│   │   ├── file_upload.py   # File upload endpoints
│   │   ├── ai.py            # AI and text extraction
│   │   ├── chat.py          # Chat endpoints
│   │   └── utils.py         # Utility functions
│   ├── uploads/             # Uploaded files storage
│   └── requirements.txt     # Python dependencies
└── frontend/
    ├── src/
    │   ├── pages/           # React page components
    │   ├── components/      # Reusable UI components
    │   ├── api/             # API integration
    │   └── App.tsx          # Main app component
    └── package.json         # Node.js dependencies
```

## 🔮 Future Enhancements

- [ ] Real AI integration (OpenAI API)
- [ ] Vector search for better Q&A
- [ ] File management and deletion
- [ ] Conversation history
- [ ] User profile management
- [ ] Multi-language support
- [ ] Advanced file processing

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

---

**Aiqa** - Making document Q&A intelligent and accessible! 🚀 