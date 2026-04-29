<template>
  <div class="container">
    <h1>Dodaj nową subskrypcję</h1>
    <form @submit.prevent="handleSubmit" class="sub-form">
      <input v-model="form.name" type="text" placeholder="Nazwa usługi (np. Netflix)" required />
      <input v-model="form.price" type="number" step="0.01" min="0" placeholder="Cena" required />
      <select v-model="form.currency">
        <option value="PLN">PLN</option>
        <option value="USD">USD</option>
        <option value="EUR">EUR</option>
      </select>
      <select v-model="form.billing_cycle">
        <option value="monthly">Miesięcznie</option>
        <option value="yearly">Rocznie</option>
      </select>
      <label>Kategoria:</label>
        <select v-model="form.category" required>
        <option v-for="cat in categories" :key="cat.id" :value="cat.id">
            {{ cat.name }}
        </option>
        </select>
      <input v-model="form.start_date" type="date" required />
      
      <input v-model="form.category" type="number" placeholder="ID Kategorii" required />

      <button type="submit" :disabled="loading">
        {{ loading ? 'Dodawanie...' : 'Dodaj subskrypcję' }}
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth';

const router = useRouter();
const auth = useAuthStore();
const loading = ref(false);
const categories = ref([]); // Tu wylądują kategorie z bazy

const form = ref({
  name: '',
  price: '',
  currency: 'PLN',
  billing_cycle: 'monthly',
  start_date: new Date().toISOString().substr(0, 10),
  category: '' // Zmieniamy na pusty ciąg na start
});

// Pobieramy kategorie z API po załadowaniu komponentu
onMounted(async () => {
  try {
    const response = await axios.get('/api/categories/');
    categories.value = response.data;
    if (categories.value.length > 0) {
        form.value.category = categories.value[0].id; // Ustaw domyślnie pierwszą
    }
  } catch (error) {
    console.error("Nie udało się pobrać kategorii", error);
  }
});

const handleSubmit = async () => {
  loading.value = true;
  try {
    await axios.post('/api/subscriptions/', form.value, {
      headers: { Authorization: `Bearer ${auth.token}` }
    });
    router.push('/dashboard');
  } catch (error) {
    alert("Błąd: " + JSON.stringify(error.response?.data));
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
.sub-form { display: flex; flex-direction: column; gap: 10px; max-width: 400px; }
input, select, button { padding: 10px; border-radius: 5px; border: 1px solid #ccc; }
button { background: #28a745; color: white; cursor: pointer; }
</style>