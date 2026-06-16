import { defineStore } from 'pinia';
import axios from 'axios';

export const useAuthStore = defineStore('auth', {
    state: () => ({
        token: localStorage.getItem('token') || null,
        isAuthenticated: !!localStorage.getItem('token'),
        userProfile: null,
    }),

    actions: {
        async login(username, password) {
            try {
                const response = await axios.post('/api/token/', {
                    username, password 
                });
                
                this.token = response.data.access;
                this.isAuthenticated = true;
                
                localStorage.setItem('token', this.token);
                
                axios.defaults.headers.common['Authorization'] = `Bearer ${this.token}`;
                await this.fetchProfile();
                return true;
            } catch (error) {
                console.error("Błąd logowania", error);
                return false;
            }
        },

        async register(username, email, password) {
            try {
                await axios.post('/api/register/', {
                    username,
                    email,
                    password
                });
                return { success: true };
            } catch (error) {
                console.error("Błąd rejestracji", error);
                return { 
                    success: false, 
                    error: error.response?.data?.username?.[0] || 
                           error.response?.data?.email?.[0] || 
                           "Wystąpił błąd podczas rejestracji." 
                };
            }
        },

        async fetchProfile() {
            if (!this.token) return;
            try {
                const response = await axios.get('/api/profile/');
                this.userProfile = response.data;
            } catch (error) {
                console.error("Błąd pobierania profilu", error);
            }
        },

        async updateProfile(profileData) {
            try {
                const response = await axios.patch('/api/profile/', profileData);
                this.userProfile = response.data;
                return { success: true };
            } catch (error) {
                console.error("Błąd aktualizacji profilu", error);
                return { success: false, error: "Nie udało się zapisać ustawień." };
            }
        },

        async changePassword(old_password, new_password) {
            try {
                await axios.post('/api/change-password/', {
                    old_password,
                    new_password
                });
                return { success: true };
            } catch (error) {
                console.error("Błąd zmiany hasła", error);
                return { 
                    success: false, 
                    error: error.response?.data?.error || "Nie udało się zmienić hasła." 
                };
            }
        },

        logout() {
            this.token = null;
            this.isAuthenticated = false;
            this.userProfile = null;
            localStorage.removeItem('token');
            delete axios.defaults.headers.common['Authorization'];
        }
    }
});
