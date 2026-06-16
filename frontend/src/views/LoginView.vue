<template>
  <div class="grow flex items-center justify-center py-12 px-4"> 
    
    <div class="bg-indigo-900 w-full max-w-lg flex flex-col items-center justify-center rounded-3xl p-8 text-white shadow-2xl border border-indigo-800">
      <h1 class="text-3xl font-bold text-center mb-8">Logowanie</h1>

      <div v-if="error" class="mb-6 w-full p-4 bg-red-500/20 border border-red-500/50 rounded-2xl flex items-center gap-3 text-red-200 text-sm">
        <i class="pi pi-exclamation-circle text-lg"></i>
        <span>Błędne dane logowania! Sprawdź nazwę użytkownika i hasło.</span>
      </div>

      <div v-if="sessionExpired" class="mb-6 w-full p-4 bg-orange-500/20 border border-orange-500/50 rounded-2xl flex items-center gap-3 text-orange-200 text-sm">
        <i class="pi pi-info-circle text-lg"></i>
        <span>Twoja sesja wygasła. Zaloguj się ponownie.</span>
      </div>

      <form @submit.prevent="handleLogin" class="w-full flex flex-col">

        <label class="ml-4 mb-1 text-sm text-indigo-300">Nazwa użytkownika</label>
        <div class="relative mb-6">
          <i class="pi pi-user absolute left-4 top-1/2 -translate-y-1/2 text-indigo-400"></i>
          <input 
            v-model="username" 
            type="text" 
            placeholder="Wpisz login" 
            required 
            class="rounded-3xl bg-indigo-950 w-full p-4 pl-12 focus:outline-none focus:ring-[5px] focus:ring-indigo-500 transition-all border border-transparent" 
          />
        </div>

        <label class="ml-4 mb-1 text-sm text-indigo-300">Hasło</label>
        <div class="relative mb-8">
          <i class="pi pi-lock absolute left-4 top-1/2 -translate-y-1/2 text-indigo-400"></i>
          <input 
            v-model="password" 
            :type="showPassword ? 'text' : 'password'" 
            placeholder="••••••••" 
            required 
            class="rounded-3xl bg-indigo-950 w-full p-4 pl-12 pr-12 focus:outline-none focus:ring-[5px] focus:ring-indigo-500 transition-all border border-transparent" 
          />
          <button 
            type="button" 
            @click="showPassword = !showPassword"
            class="absolute right-4 top-1/2 -translate-y-1/2 text-indigo-400 hover:text-indigo-200 transition-colors focus:outline-none"
          >
            <i :class="showPassword ? 'pi pi-eye-slash' : 'pi pi-eye'"></i>
          </button>
        </div>

        <button 
          type="submit" 
          :disabled="loading"
          class="bg-indigo-600 rounded-2xl py-4 mb-6 w-full text-xl font-bold hover:bg-indigo-500 transition duration-300 shadow-lg shadow-indigo-500/20 focus:outline-none focus:ring-[5px] focus:ring-indigo-500 disabled:opacity-50 flex items-center justify-center gap-3"
        >
          <i v-if="loading" class="pi pi-spin pi-spinner text-xl"></i>
          {{ loading ? 'Logowanie...' : 'Zaloguj się' }}
        </button>
        
      </form>

      <div class="flex flex-col items-center gap-4 text-sm">
        <router-link 
          :to="{ name: 'reset-password' }" 
          class="text-indigo-400 hover:text-indigo-200 underline decoration-indigo-400/30 hover:decoration-indigo-200 transition-all p-1 rounded focus:outline-none focus:ring-2 focus:ring-indigo-500"
        >
          Nie pamiętam hasła
        </router-link>
        
        <router-link 
          :to="{ name: 'register' }" 
          class="text-indigo-300 p-1 rounded focus:outline-none focus:ring-2 focus:ring-indigo-500"
        >
          Nie masz konta? <span class="text-white font-semibold underline decoration-indigo-400/30 hover:text-indigo-100 transition-all">Zarejestruj się!</span>
        </router-link>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useAuthStore } from '../stores/auth';
import { useRouter, useRoute } from 'vue-router';

const username = ref('');
const password = ref('');
const showPassword = ref(false);
const loading = ref(false);
const error = ref(false);
const sessionExpired = ref(false);

const auth = useAuthStore();
const router = useRouter();
const route = useRoute();

onMounted(() => {
  if (route.query.message === 'session_expired') {
    sessionExpired.value = true;
  }
});

const handleLogin = async () => {
  loading.value = true;
  error.value = false;
  sessionExpired.value = false;

  try {
    const success = await auth.login(username.value, password.value);
    if (success) {
      router.push('/dashboard');
    } else {
      error.value = true;
    }
  } catch (err) {
    error.value = true;
    console.error('Login error:', err);
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
@import "primeicons/primeicons.css";

.bg-indigo-950 {
  box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.3);
}
</style>
