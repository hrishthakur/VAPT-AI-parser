import axios from 'axios';

const API_BASE_URL = "http://localhost:5000/api";

const apiClient = axios.create({
    baseURL: API_BASE_URL,
    withCredentials: true,
    headers: {
        'Accept': 'application/json',
    }
});

export const uploadFile = async (formData) => {
    try {
        const response = await apiClient.post('/upload', formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            }
        });

        if (response.status !== 200) {
            throw new Error(response.data.error || 'Upload failed');
        }

        return response.data;
    } catch (error) {
        console.error('Upload error details:', {
            message: error.message,
            response: error.response?.data,
            status: error.response?.status
        });
        throw error;
    }
};

export const fetchVulnerabilities = async () => {
    try {
        const response = await apiClient.get('/vulnerabilities');
        return response.data || { vulnerabilities: [] };
    } catch (error) {
        console.error('Error fetching vulnerabilities:', error);
        throw error;
    }
};