<template>
  <div class="min-h-screen flex items-center justify-center ">
    
    <div class="bg-indigo-900 w-full max-w-lg flex flex-col rounded-3xl p-8 text-white shadow-2xl border border-indigo-800">
      
      <div class="text-center mb-8">
        <h1 class="text-3xl font-bold mb-2">Resetuj hasło</h1>
        <p class="text-indigo-300 text-sm px-4">
          Wprowadź adres email powiązany z Twoim kontem, a wyślemy Ci instrukcje resetowania hasła.
        </p>
      </div>

      <form @submit.prevent="handleResetRequest" class="w-full flex flex-col">
        
        <label class="ml-4 mb-1 text-sm text-indigo-300">Adres E-mail</label>
        <div class="relative mb-8">
          <i class="pi pi-envelope absolute left-4 top-1/2 -translate-y-1/2 "></i>
          <input 
            v-model="email" 
            type="email" 
            placeholder="twoj@email.pl" 
            required 
            class="rounded-3xl bg-indigo-950 w-full p-4 pl-12 focus:outline-none focus:ring-[5px] focus:ring-indigo-500 transition-all border border-transparent" 
          />
        </div>

        <button 
          type="submit" 
          :disabled="loading"
          class="bg-indigo-600 rounded-2xl py-4 mb-6 w-full text-xl font-bold hover:bg-indigo-500 transition duration-300 shadow-lg shadow-indigo-500/20 focus:outline-none focus:ring-[5px] focus:ring-indigo-500 disabled:opacity-50 flex items-center justify-center gap-3"
        >
          <i v-if="loading" class="pi pi-spin pi-spinner"></i>
          {{ loading ? 'Wysyłanie...' : 'Wyślij link' }}
        </button>

        <div v-if="successMessage" class="mb-6 p-4 bg-emerald-500/20 border border-emerald-500/50 rounded-2xl flex items-center gap-3 text-emerald-200 text-sm">
          <i class="pi pi-check-circle"></i>
          <span>{{ successMessage }}</span>
        </div>

        <div v-if="errorMessage" class="mb-6 p-4 bg-red-500/20 border border-red-500/50 rounded-2xl flex items-center gap-3 text-red-200 text-sm">
          <i class="pi pi-exclamation-circle"></i>
          <span>{{ errorMessage }}</span>
        </div>

      </form>

      <div class="text-center">
        <router-link 
          to="/login" 
          class="inline-flex items-center gap-2 text-indigo-400 hover:text-indigo-200 transition-colors text-sm font-medium p-2"
        >
          <i class="pi pi-arrow-left text-[10px]"></i>
          Wróć do logowania
        </router-link>
      </div>
      
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const email = ref('');
const loading = ref(false);
const successMessage = ref('');
const errorMessage = ref('');

const handleResetRequest = async () => {
  loading.ref = true;
  successMessage.value = '';
  errorMessage.value = '';

  try {
    await axios.post('/api/password-reset/', { email: email.value });
    successMessage.value = 'Jeśli adres znajduje się w naszej bazie, wysłaliśmy wiadomość z linkiem.';
  } catch (error) {
    errorMessage.value = 'Wystąpił błąd. Spróbuj ponownie później.';
    console.error(error);
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