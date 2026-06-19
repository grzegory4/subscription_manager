<template>
  <div class="py-10 px-2 md:px-4 text-white">
    <div class="max-w-6xl mx-auto flex flex-row justify-between items-center mb-10 gap-4">
      <div>
        <h1 class="text-4xl font-extrabold tracking-tight">Dashboard</h1>
      </div>
      
    </div>

    <div v-if="loading" class="flex justify-center items-center h-64">
      <i class="pi pi-spin pi-spinner text-4xl text-indigo-500"></i>
    </div>

    <div v-else class="max-w-6xl mx-auto space-y-8">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div class="lg:col-span-1 flex flex-col flex-wrap justify-between gap-5">
          <div class="bg-indigo-900 border border-indigo-800 p-6 rounded-3xl shadow-xl flex flex-col justify-center">
            <span class="text-indigo-400 text-sm uppercase font-bold tracking-widest mb-2">Suma miesięczna</span>
            <h3 class="text-3xl font-black text-emerald-400">{{ Number(stats?.total_monthly_cost || 0).toFixed(2) }} <span class="text-lg">{{ stats?.currency || 'PLN' }}</span></h3>
          </div>
          <div class="bg-indigo-900 border border-indigo-800 p-6 rounded-3xl shadow-xl flex flex-col justify-center">
  <span class="text-indigo-400 text-sm uppercase font-bold tracking-widest mb-2">Suma roczna</span>
  <h3 class="text-3xl font-black text-blue-400">
    {{ displayYearlyCost }} <span class="text-lg">{{ stats?.currency || 'PLN' }}</span>
  </h3>
</div>
        </div>

        <div class="lg:col-span-2 bg-indigo-900 border border-indigo-800 p-6 rounded-3xl shadow-xl flex flex-col items-center">
          <h3 class="text-indigo-300 mb-4 font-bold uppercase text-xs tracking-widest">Rozkład kategorii</h3>
          <div class="h-48 w-full flex justify-center">
            <Pie v-if="chartData.datasets[0].data.length" :data="chartData" :options="chartOptions" />
            <p v-else class="text-indigo-700 italic flex items-center">Brak danych do wykresu</p>
          </div>
        </div>
      </div>

      <div class="space-y-4">
        <div class="flex justify-between">

          <h2 class="text-xl font-bold ml-2 flex items-center gap-2">
            Twoje subskrypcje
          </h2>

          <router-link to="/add">
            <button class="bg-indigo-600 hover:bg-indigo-500 text-white font-bold py-3 px-6 rounded-2xl shadow-lg transition-all flex items-center gap-2">
              <i class="pi pi-plus-circle"></i> Dodaj nową
            </button>
          </router-link>

        </div>
        <div v-if="subscriptions.length" class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
          <div v-for="sub in subscriptions" :key="sub.id" 
            class="bg-indigo-900 border border-indigo-800 p-6 rounded-3xl shadow-lg hover:border-indigo-500 transition-all group">
            <div class="flex justify-between items-start mb-4">
              <div>
                <div class="flex items-center gap-2 mb-1">
                  <h3 class="text-xl font-bold group-hover:text-indigo-300 transition-colors">{{ sub.name }}</h3>
                  <span v-if="sub.is_trial" class="bg-indigo-500/30 text-indigo-300 text-[10px] font-black px-2 py-0.5 rounded-full border border-indigo-500/50 tracking-widest">TRIAL</span>
                </div>
                <span class="text-xs text-indigo-400 uppercase font-semibold tracking-tighter">
                  {{ translateBillingCycle(sub.billing_cycle) }}
                </span>
              </div>
              <div class="text-right">
                <p class="text-xl font-black text-white">{{ parseFloat(sub.price).toFixed(2) }} <span class="text-sm font-normal text-indigo-400">{{ sub.currency }}</span></p>
              </div>
            </div>

            <div class="bg-indigo-950/50 rounded-2xl p-4 mb-4 border border-indigo-800/50">
              <div class="flex justify-between items-center text-sm">
                <span class="text-indigo-500">Następna płatność:</span>
                <span class="font-mono">{{ sub.next_billing_date }}</span>
              </div>
              <div class="mt-2 text-sm font-bold" :class="getStatusClass(sub.days_until_payment, sub.is_trial)">
                <i class="pi pi-clock mr-1 text-[10px]"></i> {{ getStatusText(sub.days_until_payment, sub.is_trial) }}
              </div>
            </div>

            <div class="flex gap-2">
              <router-link :to="{ name: 'edit-subscription', params: { id: sub.id } }" class="grow">
                <button class="w-full bg-indigo-500 hover:bg-indigo-700 text-indigo-200 py-2 rounded-xl text-sm font-bold transition-all">
                  Edytuj
                </button>
              </router-link>
              <button @click="prepareDelete(sub.id)" class="px-4 bg-transparent hover:bg-red-500/10 text-red-500/70 hover:text-red-500 border border-red-500/20 rounded-xl transition-all">
                <i class="pi pi-trash"></i>
              </button>
            </div>
          </div>
        </div>
        <div v-else class="bg-indigo-900/30 border border-dashed border-indigo-800 p-12 rounded-3xl text-center">
          <p class="text-indigo-500 italic mb-4">Brak aktywnych subskrypcji.</p>
          <router-link to="/add" class="text-indigo-400 underline hover:text-indigo-300 transition-all">
            Dodaj swoją pierwszą usługę
          </router-link>
        </div>
      </div>
    </div>
  </div>
<div v-if="showDeleteModal" class="fixed inset-0 z-200 flex items-center justify-center p-4">
  <div class="absolute inset-0 bg-indigo-950/60 backdrop-blur-sm transition-opacity" @click="showDeleteModal = false"></div>
  
  <div class="bg-indigo-900 border border-indigo-700 w-full max-w-sm p-8 rounded-4xl shadow-2xl relative z-10 scale-in-center">
    <div class="text-center">
      <div class="bg-red-500/10 w-20 h-20 rounded-3xl flex items-center justify-center mx-auto mb-6">
        <i class="pi pi-exclamation-triangle text-4xl text-red-500"></i>
      </div>
      
      <h3 class="text-2xl font-bold text-white mb-2">Jesteś pewien?</h3>
      <p class="text-indigo-300 mb-8 leading-relaxed">
        Subskrypcja zostanie trwale usunięta. Nie będziesz mógł cofnąć tej operacji.
      </p>
      
      <div class="flex flex-col gap-3">
        <button @click="executeDelete" 
          class="w-full bg-red-600 hover:bg-red-500 text-white py-4 rounded-2xl font-bold transition-all shadow-lg shadow-red-600/20">
          Tak, usuń subskrypcję
        </button>
        <button @click="showDeleteModal = false" 
          class="w-full bg-indigo-800 hover:bg-indigo-700 text-indigo-200 py-4 rounded-2xl font-bold transition-all">
          Anuluj
        </button>
      </div>
    </div>
  </div>
</div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { Pie } from 'vue-chartjs';
import axios from 'axios';
import { useAuthStore } from '../stores/auth';
import { ArcElement, Legend, Tooltip, Chart as ChartJS, } from 'chart.js';
import { useRouter } from 'vue-router';

const router = useRouter();
const auth = useAuthStore();

ChartJS.register(ArcElement, Tooltip, Legend);

const stats = ref(null);
const subscriptions = ref([]);
const loading = ref(true);

const chartData = ref({
  labels: [],
  datasets: [{ data: [], backgroundColor: ['#818cf8', '#34d399', '#fbbf24', '#f87171', '#a78bfa', '#22d3ee'] }]
});

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      position: 'right',
      labels: { color: '#818cf8', font: { size: 10, weight: 'bold' }, usePointStyle: true }
    }
  }
};

const handleLogout = () => {
  auth.logout();
  router.push('/login');
};

onMounted(async () => {
  try {
    const subRes = await axios.get('/api/subscriptions/');
    subscriptions.value = subRes.data;

    const statsRes = await axios.get('/api/stats/', {
      headers: { Authorization: `Bearer ${auth.token}` }
    });
    stats.value = statsRes.data;

    if (statsRes.data.category_distribution.length > 0) {
      chartData.value = {
        labels: statsRes.data.category_distribution.map(item => item.category__name),
        datasets: [{
          data: statsRes.data.category_distribution.map(item => item.total),
          backgroundColor: ['#6366f1', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6', '#06b6d4'],
          borderWidth: 0
        }]
      };
    }
  } catch (error) {
    console.error("Błąd API:", error);
    if (error.response?.status === 401) router.push('/login');
  } finally {
    loading.value = false;
  }
});

const showDeleteModal = ref(false);
const subIdToDelete = ref(null);

const prepareDelete = (id) => {
  subIdToDelete.value = id; 
  showDeleteModal.value = true; 
};

const executeDelete = async () => {
  if (!subIdToDelete.value) return;

  try {
    await axios.delete(`/api/subscriptions/${subIdToDelete.value}/`, {
      headers: { Authorization: `Bearer ${auth.token}` }
    });

    subscriptions.value = subscriptions.value.filter(s => s.id !== subIdToDelete.value);

    const statsRes = await axios.get('/api/stats/', {
      headers: { Authorization: `Bearer ${auth.token}` }
    });
    stats.value = statsRes.data;

    if (statsRes.data.category_distribution.length > 0) {
      chartData.value = {
        labels: statsRes.data.category_distribution.map(item => item.category__name),
        datasets: [{
          data: statsRes.data.category_distribution.map(item => item.total),
          backgroundColor: ['#6366f1', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6', '#06b6d4'],
          borderWidth: 0
        }]
      };
    } else {
      chartData.value.datasets[0].data = [];
    }

  } catch (error) {
    console.error("Błąd usuwania:", error);
  } finally {
    showDeleteModal.value = false;
    subIdToDelete.value = null;
  }
};

const getStatusText = (days, isTrial = false) => {
  if (days === undefined || days === null) return "Obliczanie...";
  if (isTrial) {
    if (days < 0) return "Okres próbny zakończony";
    if (days === 0) return "Trial kończy się dzisiaj!";
    return `Trial jeszcze przez ${days} dni`;
  }
  if (days < 0) return "Termin minął";
  if (days === 0) return "Płatność dzisiaj!";
  if (days === 1) return "Płatność jutro!";
  return `Za ${days} dni`;
};

const getStatusClass = (days, isTrial = false) => {
  if (isTrial && days >= 0) return 'text-indigo-400';
  if (days < 0) return 'text-red-400';
  if (days <= 3) return 'text-orange-400';
  return 'text-emerald-400';
};

const displayYearlyCost = computed(() => {
  if (!stats.value) return "0.00";

  const monthly = Number(stats.value.total_monthly_cost) || 0;
  const yearly = Number(stats.value.total_yearly_cost) || 0;

  if (yearly === 0 && monthly > 0) {
    return (monthly * 12).toFixed(2);
  }

  return yearly.toFixed(2);
});

const translateBillingCycle = (cycle) => {
  const map = { 'monthly': 'Miesięcznie', 'yearly': 'Rocznie' };
  return map[cycle] || cycle;
};
</script>

<style scoped>
@import "primeicons/primeicons.css";

::-webkit-scrollbar {
  width: 8px;
}
::-webkit-scrollbar-track {
  background: #0c0a2e;
}
::-webkit-scrollbar-thumb {
  background: #1e1b4b;
  border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover {
  background: #312e81;
}
</style>