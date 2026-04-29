<template>
  <div class="dashboard">
    <router-link to="/add">
    <button class="add-btn">+ Dodaj nową</button>
    </router-link>
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
            <td>{{ parseFloat(sub.price).toFixed(2) }} {{ sub.currency }}</td>
            <td>{{ sub.billing_cycle }}</td>
            <td>
              <router-link :to="{ name: 'edit-subscription', params: { id: sub.id } }">
                <button style="margin-right: 5px">Edytuj</button>
              </router-link>
              <button @click="deleteSub(sub.id)" style="color: red">Usuń</button>
            </td>
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
const deleteSub = async (id) => {
  if (confirm("Czy na pewno chcesz usunąć tę subskrypcję?")) {
    try {
      await axios.delete(`/api/subscriptions/${id}/`, {
        headers: { Authorization: `Bearer ${auth.token}` }
      });
      // Odśwież listę po usunięciu
      subscriptions.value = subscriptions.value.filter(s => s.id !== id);
    } catch (error) {
      console.error("Błąd usuwania", error);
    }
  }
};
</script>

<style scoped>
.dashboard { padding: 20px; }
table { width: 100%; border-collapse: collapse; margin-top: 20px; }
th, td { border: 1px solid #ddd; padding: 12px; text-align: left; }
th { background-color: #f2f2f2; }
.add-btn {
  background: #007bff;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  margin-bottom: 20px;
  cursor: pointer;
}
</style>