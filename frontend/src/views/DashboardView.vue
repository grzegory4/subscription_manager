<template>
  <div class="dashboard">
    <h1>Twoje Subskrypcje</h1>
    <div v-if="loading">Ładowanie...</div>
    <div v-else>
      <table v-if="subscriptions.length">
        <thead>
          <tr>
            <th>Nazwa</th>
            <th>Cena</th>
            <th>Cykl</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="sub in subscriptions" :key="sub.id">
            <td>{{ sub.name }}</td>
            <td>{{ sub.price }} {{ sub.currency }}</td>
            <td>{{ sub.billing_cycle }}</td>
          </tr>
        </tbody>
      </table>
      <p v-else>Brak subskrypcji. Dodaj pierwszą!</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useAuthStore } from '../stores/auth';

const subscriptions = ref([]);
const loading = ref(true);
const auth = useAuthStore();

onMounted(async () => {
  try {
    const response = await axios.get('/api/subscriptions/', {
      headers: {
        Authorization: `Bearer ${auth.token}`
      }
    });
    subscriptions.value = response.data;
  } catch (error) {
    console.error("Błąd pobierania danych", error);
  } finally {
    loading.value = false;
  }
});
</script>

<style scoped>
.dashboard { padding: 20px; }
table { width: 100%; border-collapse: collapse; margin-top: 20px; }
th, td { border: 1px solid #ddd; padding: 12px; text-align: left; }
th { background-color: #f2f2f2; }
</style>