import axios from 'axios';

const apiUrl = 'http://127.0.0.1:8000/api/projects/';

export const getProjects = async () => {
    try {
        const response = await axios.get(apiUrl);
        return response.data;
    } catch (error) {
        console.error('Error fetching projects:', error);
        throw error;
    }
};
