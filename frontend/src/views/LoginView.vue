<template>
  <div class="login-container">
    <h1>Logowanie</h1>
    <form @submit.prevent="handleLogin">
      <input v-model="username" type="text" placeholder="Użytkownik" required />
      <input v-model="password" type="password" placeholder="Hasło" required />
      <button type="submit">Zaloguj</button>
    </form>
    <p v-if="error" style="color: red">Błędne dane logowania!</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '../stores/auth';
import { useRouter } from 'vue-router';

const username = ref('');
const password = ref('');
const error = ref(false);
const auth = useAuthStore();
const router = useRouter();

const handleLogin = async () => {
  const success = await auth.login(username.value, password.value);
  if (success) {
    router.push('/dashboard');
  } else {
    error.value = true;
  }
};
</script>