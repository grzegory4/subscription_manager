<template>
  <div class="container">
    <h1>Edytuj subskrypcję</h1>
    <form @submit.prevent="handleUpdate" class="sub-form">
      <input v-model="form.name" type="text" placeholder="Nazwa" required />
      <input v-model="form.price" type="number" step="0.01" required />
      <select v-model="form.currency">
        <option value="PLN">PLN</option>
        <option value="USD">USD</option>
        <option value="EUR">EUR</option>
      </select>
      <select v-model="form.billing_cycle">
        <option value="monthly">Miesięcznie</option>
        <option value="yearly">Rocznie</option>
      </select>
      <input v-model="form.start_date" type="date" required />
      
      <label>Kategoria:</label>
      <select v-model="form.category" required>
        <option v-for="cat in categories" :key="cat.id" :value="cat.id">
          {{ cat.name }}
        </option>
      </select>

      <button type="submit" :disabled="loading">
        {{ loading ? 'Zapisywanie...' : 'Zaktualizuj' }}
      </button>
      <button type="button" @click="$router.push('/dashboard')" style="background: gray">Anuluj</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter, useRoute } from 'vue-router';
import { useAuthStore } from '../stores/auth';

const router = useRouter();
const route = useRoute();
const auth = useAuthStore();
const loading = ref(false);
const categories = ref([]);

const form = ref({
  name: '',
  price: '',
  currency: 'PLN',
  billing_cycle: 'monthly',
  start_date: '',
  category: null
});

onMounted(async () => {
  try {
    // 1. Get Category
    const catRes = await axios.get('/api/categories/');
    categories.value = catRes.data;

    // 2. Get subbscriptionn data for editing (using id from URL) 
    const subId = route.params.id;
    const subRes = await axios.get(`/api/subscriptions/${subId}/`, {
      headers: { Authorization: `Bearer ${auth.token}` }
    });
    
    // Fill form with data from database
    form.value = {
      ...subRes.data,
      category: subRes.data.category
    };
  } catch (error) {
    console.error("Błąd ładowania danych:", error);
    alert("Nie udało się pobrać danych subskrypcji.");
  }
});

const handleUpdate = async () => {
  loading.value = true;
  const subId = route.params.id;
  try {
    await axios.put(`/api/subscriptions/${subId}/`, form.value, {
      headers: { Authorization: `Bearer ${auth.token}` }
    });
    router.push('/dashboard');
  } catch (error) {
    alert("Błąd podczas aktualizacji: " + JSON.stringify(error.response?.data));
  } finally {
    loading.value = false;
  }
};
</script>