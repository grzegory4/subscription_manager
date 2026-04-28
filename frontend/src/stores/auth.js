import { defineStore } from 'pinia';
import axios from 'axios';

export const useAuthStore = defineStore('auth', {
    state: () => ({
        token: localStorage.getItem('token') || null,
        isAuthenticated: !!localStorage.getItem('token'),
    }),
    actions: {
        async login(username, password) {
        try {
            const response = await axios.post('http://localhost:8000/api/token/', {
            username, password 
        });
            this.token = response.data.access;
            this.isAuthenticated = true;
            localStorage.setItem('token', this.token);
            axios.defaults.headers.common['Authorization'] = `Bearer ${this.token}`;
            return true;
        } catch (error) {
            console.error("Błąd logowania", error);
            return false;
        }
    },
    logout() {
        this.token = null;
        this.isAuthenticated = false;
        localStorage.removeItem('token');
        delete axios.defaults.headers.common['Authorization'];
        }
    }
});