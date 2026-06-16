<template>
  <nav class="bg-indigo-950/80 backdrop-blur-md border-b border-indigo-800/50 px-4 md:px-8 py-4 flex items-center justify-between shadow-2xl sticky top-0 z-[100]">
      
      <router-link :to="{ name: auth.isAuthenticated ? 'dashboard' : 'app-page' }" 
        class="group flex items-center gap-2 text-2xl font-black tracking-tighter text-white hover:text-indigo-200 transition-all duration-500">
        <div class="bg-indigo-600 group-hover:bg-indigo-700 py-2 px-3 rounded-xl group-hover:rotate-12 group-hover:scale-110 transition-all duration-500 shadow-lg shadow-indigo-600/20">
          <i class="pi pi-wallet text-xl"></i>
        </div>
        <span>SubManager</span>
      </router-link>

      <div class="flex items-center gap-1 md:gap-3">
        
        <template v-if="auth.isAuthenticated">
          <router-link :to="{ name: 'settings' }" 
            class="flex items-center gap-2 px-4 py-2 rounded-xl text-indigo-300 hover:text-white hover:bg-indigo-800/50 transition-all font-medium text-sm group"
            title="Ustawienia">
            <i class="pi pi-cog group-hover:rotate-90 transition-all duration-500"></i>
            <span class="hidden md:inline">Ustawienia</span>
          </router-link>

          <button @click="handleLogout" 
            class="flex items-center gap-2 px-4 py-2 rounded-xl text-indigo-400 hover:text-red-400 hover:bg-red-500/10 transition-all font-medium text-sm group">
            <i class="pi pi-sign-out"></i>
            <span class="hidden md:inline">Wyloguj</span>
          </button>
        </template>

        <template v-else>
          <router-link :to="{ name: 'login' }" 
            class="px-5 py-2.5 text-sm font-bold text-indigo-300 hover:text-white transition-colors">
            Logowanie
          </router-link>

          <router-link :to="{ name: 'register' }">
            <button class="bg-indigo-600 hover:bg-indigo-500 text-white px-6 py-2.5 rounded-xl text-sm font-bold transition-all shadow-lg shadow-indigo-600/20 active:scale-95">
              Załóż konto
            </button>
          </router-link>
        </template>

      </div>
  </nav>
</template>

<script setup>
import { useAuthStore } from '../stores/auth';
import { useRouter } from 'vue-router';

const auth = useAuthStore();
const router = useRouter();

const handleLogout = () => {
  auth.logout();
  router.push('/login');
};
</script>

<style scoped>
    @import "primeicons/primeicons.css";
    @import "tailwindcss";
</style>
