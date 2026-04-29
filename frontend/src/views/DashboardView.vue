<template>
  <div class="dashboard">
    <router-link to="/add">
    <button class="add-btn">+ Dodaj nową</button>
    </router-link>
    <h1>Twoje Subskrypcje</h1>
    <div v-if="loading">Ładowanie...</div>
    <div v-else>
      <div class="stats-container" v-if="stats">
        <div class="stat-card">
          <h3>Miesięcznie: {{ stats.total_monthly_cost }} PLN</h3>
        </div>
        
        <div class="chart-wrapper">
          <Pie v-if="chartData.datasets[0].data.length" :data="chartData" />
        </div>
    </div>
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
            <td>
              {{ sub.next_billing_date }}
              <br>
              <span :class="getStatusClass(sub.days_until_payment)">
                {{ getStatusText(sub.days_until_payment) }}
              </span>
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
import { Pie } from 'vue-chartjs';
import axios from 'axios';
import { useAuthStore } from '../stores/auth';
import { ArcElement, Legend, Tooltip, Chart as ChartJS, } from 'chart.js';

ChartJS.register(ArcElement, Tooltip, Legend);
const stats = ref(null);
const chartData = ref({
  labels: [],
  datasets: [{ data: [], backgroudColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF'] }]
});

const subscriptions = ref([]);
const loading = ref(true);
const auth = useAuthStore();

onMounted(async () => {
  try {
    const subRes = await axios.get('/api/subscriptions/');
    subscriptions.value = subRes.data;

    const statsRes = await axios.get('/api/stats/');
    stats.value = statsRes.data;

    if (statsRes.data.category_distribution.length > 0) {
      chartData.value = {
        labels: statsRes.data.category_distribution.map(item => item.category__name),
        datasets: [{
          data: statsRes.data.category_distribution.map(item => item.total),
          backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#C9CBCF']
        }]
      };
    }
  } catch (error) {
    console.error("Błąd pobierania danych z API:", error);
    // Jeśli dostaniesz 401, możesz tu dodać przekierowanie do logowania
    if (error.response?.status === 401) {
      router.push('/login');
    }
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
const getStatusText = (days) => {
  if (days < 0) return "Termin minął!";
  if (days === 0) return "Płatność dzisiaj!";
  if (days === 1) return "Płatność jutro!";
  return `Za ${days} dni`;
};

const getStatusClass = (days) => {
  if (days <= 3) return 'text-danger fw-bold'; // Czerwony dla bliskich terminów
  return 'text-muted'; // Szary dla odległych
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
.urgent { color: red; font-weight: bold; }
.text-danger { color: #d9534f; font-weight: bold; }
.text-muted { color: #6c757d; font-size: 0.85em; }
</style>