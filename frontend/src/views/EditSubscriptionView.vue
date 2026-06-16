<template>
  <div class="grow flex items-center justify-center py-12 px-4"> 
    
    <div class="bg-indigo-900 w-full max-w-lg flex flex-col rounded-3xl p-8 text-white shadow-2xl border border-indigo-800">
      
      <div class="text-center mb-8">
        <h1 class="text-3xl font-bold tracking-tight">Edytuj subskrypcję</h1>
      </div>

      <form @submit.prevent="handleUpdate" class="w-full flex flex-col">
        
        <label class="ml-4 mb-1 text-sm text-indigo-300">Nazwa usługi</label>
        <div class="relative mb-6">
          <i class="pi pi-tag absolute left-4 top-1/2 -translate-y-1/2 text-indigo-400 z-10"></i>
          <input 
            v-model="form.name" 
            type="text" 
            placeholder="np. Netflix" 
            required 
            class="rounded-3xl bg-indigo-950 w-full p-4 pl-12 focus:outline-none focus:ring-[5px] focus:ring-indigo-500 transition-all border border-transparent shadow-inner" 
          />
        </div>

        <div class="flex gap-4 mb-6">
          <div class="grow">
            <label class="ml-4 mb-1 text-sm text-indigo-300">Kwota</label>
            <div class="relative">
              <i class="pi pi-money-bill absolute left-4 top-5.5 text-indigo-400 z-10"></i>
              <InputNumber v-model="form.price" mode="decimal" :minFractionDigits="2" :maxFractionDigits="2" :min="0" showButtons buttonLayout="stacked"
                class="w-full"
                :pt="{
                  pcInputText: {
                    root: { class: 'rounded-3xl bg-indigo-950 w-full p-4 pl-12 pr-16 border-none focus:ring-[5px] focus:ring-indigo-500 transition-all shadow-inner' }
                  },
                  buttonGroup: { class: 'p-1 text-gray-400' },
                  incrementButton: { class: 'hover:text-indigo-400 transition-colors' },
                  decrementButton: { class: 'hover:text-indigo-400 transition-colors' }
                }"
              />
            </div>
          </div>
          <div class="w-1/3">
            <label class="ml-4 mb-1 text-sm text-indigo-300">Waluta</label>
              <Select v-model="form.currency" :options="['PLN', 'USD', 'EUR']" class="w-full"
              :pt="{
                root: { class: `rounded-3xl bg-indigo-950 w-full p-1 transition-all border border-transparent focus-within:ring-[5px] focus-within:ring-indigo-500 shadow-inner` },
                label: { class: 'text-white p-3 pl-5' },
                dropdown: { class: 'pr-4' },
                overlay: { class: 'bg-indigo-950 border border-indigo-500/30 shadow-2xl rounded-2xl mt-1 overflow-hidden' },
                list: { class: 'p-2' },
                option: ({ context }) => ({
                  class: [
                    'p-3 rounded-xl transition-all cursor-pointer mb-1',
                    context.focused ? 'bg-indigo-800' : '',
                    context.selected ? 'bg-indigo-600' : '',
                  ]
                })
              }" 
              />
          </div>
        </div>
          
        <label class="ml-4 mb-1 text-sm text-indigo-300">Cykl rozliczeniowy</label>
        <div class="relative">
          <i class="pi pi-calendar-clock absolute left-4 top-5.5 text-indigo-400 z-10"></i>
          <Select v-model="form.billing_cycle" :options="[{label: 'Miesięcznie', value: 'monthly'}, {label: 'Rocznie', value: 'yearly'}]" optionLabel="label" optionValue="value" placeholder="Wybierz cykl" class="mb-5"
              :pt="{
                root: { class: `rounded-3xl bg-indigo-950 w-full p-1 pl-7 transition-all border border-transparent focus-within:ring-[5px] focus-within:ring-indigo-500 shadow-inner` },
                label: { class: 'text-white p-3 pl-5' },
                dropdown: { class: 'pr-4' },
                overlay: { class: 'bg-indigo-950 border border-indigo-500/30 shadow-2xl rounded-2xl mt-1 overflow-hidden' },
                list: { class: 'p-2' },
                option: ({ context }) => ({
                  class: [
                    'p-3 rounded-xl transition-all cursor-pointer mb-1',
                    context.focused ? 'bg-indigo-800 text-white' : 'text-indigo-100',
                    context.selected ? '!bg-indigo-600 !text-white font-bold' : 'hover:bg-indigo-900'
                  ]
                  })
                }" 
              />
        </div>
        <label class="ml-4 mb-1 text-sm text-indigo-300">Data rozpoczęcia</label>
        <div class="relative mb-6">
          <i class="pi pi-calendar absolute left-4 top-1/2 -translate-y-1/2 text-indigo-400 z-10 pointer-events-none"></i>
          <DatePicker v-model="form.start_date" dateFormat="dd/mm/yy" class="w-full"
              :pt="{
                  pcInputText: { 
                      root: { class: 'rounded-3xl bg-indigo-950 w-full p-4 pl-12 text-white border-none focus:ring-[5px] focus:ring-indigo-500 transition-all shadow-inner' } 
                  },
                  inputIcon: {
                    class: 'absolute right-4 top-1/2 -translate-y-1/2 pointer-events-none text-indigo-400'
                  },
                  panel: { 
                      class: 'bg-indigo-950 border border-indigo-500/30 text-white shadow-2xl rounded-3xl p-4' 
                  },
                  header: { 
                      class: 'bg-transparent text-white border-b border-indigo-800/50 pb-4 mb-2 flex items-center justify-between' 
                  },  
                  title: { class: 'font-bold' },
                  day: ({ context }) => ({
                    class: [
                        'flex items-center justify-center p-0',
                        'w-10 h-10 rounded-full transition-all duration-300 text-sm',
                        context.selected ? '!bg-indigo-500 text-white font-bold' : '',
                        !context.selected ? 'hover:bg-indigo-800/50' : '',
                        context.today ? 'bg-indigo-950 border-[3px] border-indigo-500/50' : '',
                        context.otherMonth ? 'text-gray-400' : '',
                      ]
                    }),
                  month: ({ context }) => ({
                    class: [
                        'hover:bg-indigo-800/50 text-sm p-2 rounded-xl transition-all',
                        context.selected ? 'bg-indigo-500 text-white font-bold' : '',
                      ]
                    }),
                  year: ({ context }) => ({
                    class: [
                        'hover:bg-indigo-800/50 text-sm p-2 rounded-xl transition-all',
                        context.selected ? 'bg-indigo-500 text-white font-bold' : '',
                      ]
                    }),
              }">
            </DatePicker>
        </div>
  
        <label class="ml-4 mb-1 text-sm text-indigo-300">Kategoria</label>
        <div class="relative">
          <i class="pi pi-hashtag absolute left-4 top-5.5 text-indigo-400 z-10"></i>
          <Select 
              v-model="form.category" 
              :options="categories" 
              optionLabel="name" 
              optionValue="id" 
              placeholder="Wybierz kategorię"
              required 
              class="w-full mb-8"
              :pt="{
                root: ({ state }) => ({ 
                  class: [
                    'rounded-3xl bg-indigo-950 w-full p-1 pl-7 transition-all border outline-none shadow-inner',
                    state.focused 
                      ? 'border-indigo-500 ring-[5px] ring-indigo-500/50' 
                      : 'border-transparent'
                  ]
                }),
                label: { class: 'text-white p-3 pl-5 focus:outline-none' },
                dropdown: { class: 'pr-4' },
                overlay: { class: 'bg-indigo-950 border border-indigo-500/30 shadow-2xl rounded-2xl mt-1 overflow-hidden' },
                list: { class: 'p-2' },
                option: ({ context }) => ({
                  class: [
                    'p-3 rounded-xl transition-all cursor-pointer mb-1',
                    context.focused ? 'bg-indigo-800 text-white' : 'text-indigo-100',
                    context.selected ? '!bg-indigo-600 !text-white font-bold' : 'hover:bg-indigo-900'
                  ]
                })
              }" 
            />
        </div>
        <div v-if="errorMessage" class="mb-6 p-4 bg-red-500/20 border border-red-500/50 rounded-2xl flex items-center gap-3 text-red-200">
          <i class="pi pi-exclamation-triangle"></i>
          <span class="text-sm font-medium">{{ errorMessage }}</span>
        </div>

        <div class="flex flex-col gap-3">
          <button type="submit" :disabled="loading"
            class="bg-indigo-600 rounded-2xl py-4 w-full text-xl font-bold hover:bg-indigo-500 transition duration-300 shadow-lg shadow-indigo-500/20 focus:outline-none focus:ring-[5px] focus:ring-indigo-500 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-3">
            <i v-if="loading" class="pi pi-spin pi-spinner text-xl"></i>
            {{ loading ? 'Zapisywanie...' : 'Zaktualizuj dane' }}
          </button>
          
          <button type="button" @click="$router.push('/dashboard')" 
            class="bg-transparent border border-indigo-700 rounded-2xl py-3 w-full text-sm font-medium hover:bg-indigo-800 transition duration-300 text-indigo-300">
            Anuluj zmiany
          </button>
        </div>
      </form>
      
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  import { useRouter, useRoute } from 'vue-router';
  import { useAuthStore } from '../stores/auth';
  import DatePicker from 'primevue/datepicker';
  import InputNumber from 'primevue/inputnumber';
  import Select from 'primevue/select';

  const router = useRouter();
  const route = useRoute();
  const auth = useAuthStore();
  
  const loading = ref(false);
  const categories = ref([]);
  const errorMessage = ref('');

  const form = ref({
    name: '',
    price: 0,
    currency: 'PLN',
    billing_cycle: 'monthly',
    start_date: new Date(),
    category: null
  });

  onMounted(async () => {
    try {
      const catRes = await axios.get('/api/categories/', {
        headers: { Authorization: `Bearer ${auth.token}` }
      });
      categories.value = catRes.data;

      const subId = route.params.id;
      const subRes = await axios.get(`/api/subscriptions/${subId}/`, {
        headers: { Authorization: `Bearer ${auth.token}` }
      });
      
      const subData = subRes.data;
      form.value = {
        ...subData,
        price: parseFloat(subData.price),
        start_date: new Date(subData.start_date),
        category: subData.category
      };
    } catch (error) {
      console.error("Błąd ładowania danych:", error);
      errorMessage.value = "Nie udało się pobrać danych subskrypcji. Spróbuj odświeżyć stronę.";
    }
  });

  const handleUpdate = async () => {
    loading.value = true;
    errorMessage.value = '';
    const subId = route.params.id;

    try {
      const payload = {
        ...form.value,
        start_date: form.value.start_date instanceof Date 
                    ? form.value.start_date.toISOString().split('T')[0] 
                    : form.value.start_date
      };

      await axios.put(`/api/subscriptions/${subId}/`, payload, {
        headers: { Authorization: `Bearer ${auth.token}` }
      });
      router.push('/dashboard');
    } catch (error) {
      if (error.response && error.response.data) {
        const serverErrors = error.response.data;
        errorMessage.value = Object.entries(serverErrors)
          .map(([key, value]) => `${key}: ${value}`)
          .join(' | ');
      } else {
        errorMessage.value = "Wystąpił nieoczekiwany błąd podczas aktualizacji.";
      }
    } finally {
      loading.value = false;
    }
  };
</script>

<style scoped>
@import "primeicons/primeicons.css";

.shadow-inner {
  box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.3);
}
</style>
