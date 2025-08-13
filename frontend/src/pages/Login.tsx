import React from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';
import { TextField, Button, Box, Typography, Link } from '@mui/material';
import { Link as RouterLink } from 'react-router-dom';
import api from '../api';

const Login: React.FC = () => {
  const formik = useFormik({
    initialValues: { username: '', password: '' },
    validationSchema: Yup.object({
      username: Yup.string().required('Required'),
      password: Yup.string().required('Required'),
    }),
    onSubmit: async (values, { setSubmitting, setStatus }) => {
      try {
        const form = new FormData();
        form.append('username', values.username);
        form.append('password', values.password);
        const res = await api.post('/auth/login', form);
        localStorage.setItem('token', res.data.access_token);
        setStatus({ success: true });
        window.location.href = '/upload';
      } catch (err: any) {
        setStatus({ error: err.response?.data?.detail || 'Login failed' });
      } finally {
        setSubmitting(false);
      }
    },
  });
  return (
    <Box maxWidth={400} mx="auto" mt={8} p={2}>
      <Typography variant="h4" mb={2} textAlign="center">🤖 Aiqa</Typography>
      <Typography variant="h5" mb={3} textAlign="center">Login to Your Account</Typography>
      <form onSubmit={formik.handleSubmit}>
        <TextField
          fullWidth
          margin="normal"
          id="username"
          name="username"
          label="Username"
          value={formik.values.username}
          onChange={formik.handleChange}
          error={formik.touched.username && Boolean(formik.errors.username)}
          helperText={formik.touched.username && formik.errors.username}
        />
        <TextField
          fullWidth
          margin="normal"
          id="password"
          name="password"
          label="Password"
          type="password"
          value={formik.values.password}
          onChange={formik.handleChange}
          error={formik.touched.password && Boolean(formik.errors.password)}
          helperText={formik.touched.password && formik.errors.password}
        />
        <Button color="primary" variant="contained" fullWidth type="submit" disabled={formik.isSubmitting} sx={{ mt: 2 }}>
          Login
        </Button>
        {formik.status?.error && <Typography color="error" mt={2}>{formik.status.error}</Typography>}
      </form>
      <Box mt={3} textAlign="center">
        <Typography variant="body2">
          Don't have an account?{' '}
          <Link component={RouterLink} to="/signup" variant="body2">
            Sign up here
          </Link>
        </Typography>
      </Box>
    </Box>
  );
};
export default Login;