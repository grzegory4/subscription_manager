<template>
  <div class="grow flex flex-col py-10 px-4 md:px-8 text-white">
    <div class="max-w-4xl mx-auto w-full">
      
      <div class="mb-10 flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h1 class="text-4xl font-extrabold tracking-tight mb-2">
            <i class="pi pi-cog text-3xl mr-2 text-indigo-400"></i> Ustawienia
          </h1>
          <p class="text-indigo-400">Zarządzaj swoimi preferencjami i bezpieczeństwem konta.</p>
        </div>
        <router-link to="/dashboard">
          <button class="bg-indigo-900/50 hover:bg-indigo-800 text-indigo-300 border border-indigo-700 py-3 px-6 rounded-2xl transition-all flex items-center gap-2 text-sm font-bold">
            <i class="pi pi-arrow-left"></i> Wróć do dashboardu
          </button>
        </router-link>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        
        <div class="lg:col-span-1 space-y-2">
          <button @click="activeSection = 'general'" 
            class="w-full text-left px-6 py-4 rounded-2xl transition-all flex items-center gap-3"
            :class="activeSection === 'general' ? 'bg-indigo-600 text-white font-bold shadow-lg shadow-indigo-600/20' : 'bg-indigo-900/30 text-indigo-400 hover:bg-indigo-900/50'">
            <i class="pi pi-sliders-h"></i> Ogólne
          </button>
          <button @click="activeSection = 'security'" 
            class="w-full text-left px-6 py-4 rounded-2xl transition-all flex items-center gap-3"
            :class="activeSection === 'security' ? 'bg-indigo-600 text-white font-bold shadow-lg shadow-indigo-600/20' : 'bg-indigo-900/30 text-indigo-400 hover:bg-indigo-900/50'">
            <i class="pi pi-lock"></i> Bezpieczeństwo
          </button>
        </div>

        <div class="lg:col-span-2 space-y-6">
          
          <div v-if="activeSection === 'general'" class="bg-indigo-900 border border-indigo-800 rounded-3xl p-8 shadow-xl animate-fade-in">
            <h2 class="text-2xl font-bold mb-6 flex items-center gap-2">
              <i class="pi pi-sliders-h text-indigo-400"></i> Preferencje wyświetlania
            </h2>
            
            <div class="space-y-6">
              <div>
                <label class="block text-sm font-bold text-indigo-300 mb-3 ml-1">Domyślna waluta przeliczeń</label>
                <p class="text-xs text-indigo-400 mb-4 ml-1">Wybierz walutę, w której chcesz widzieć podsumowania na Dashboardzie.</p>
                <Select v-model="settings.default_currency" :options="['PLN', 'USD', 'EUR']" class="w-full max-w-xs"
                  :pt="{
                    root: { class: 'rounded-3xl bg-indigo-950 w-full p-1 transition-all border border-indigo-800 focus-within:ring-[5px] focus-within:ring-indigo-500/50' },
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

              <div v-if="settingsError" class="p-4 bg-red-500/20 border border-red-500/50 rounded-2xl text-red-200 text-sm">
                {{ settingsError }}
              </div>

              <div v-if="settingsSuccess" class="p-4 bg-emerald-500/20 border border-emerald-500/50 rounded-2xl text-emerald-200 text-sm">
                Ustawienia zostały zapisane!
              </div>

              <div class="pt-6 border-t border-indigo-800">
                <button @click="saveGeneralSettings" :disabled="saving"
                  class="bg-indigo-600 hover:bg-indigo-500 text-white font-bold py-3 px-8 rounded-2xl shadow-lg transition-all flex items-center gap-2 disabled:opacity-50">
                  <i v-if="saving" class="pi pi-spin pi-spinner"></i>
                  {{ saving ? 'Zapisywanie...' : 'Zapisz zmiany' }}
                </button>
              </div>
            </div>
          </div>

          <div v-if="activeSection === 'security'" class="bg-indigo-900 border border-indigo-800 rounded-3xl p-8 shadow-xl animate-fade-in">
            <h2 class="text-2xl font-bold mb-6 flex items-center gap-2">
              <i class="pi pi-lock text-indigo-400"></i> Zmiana hasła
            </h2>
            
            <form @submit.prevent="handleChangePassword" class="space-y-5">
              <div>
                <label class="block text-sm font-bold text-indigo-300 mb-2 ml-1">Obecne hasło</label>
                <input v-model="passwordForm.old_password" type="password" required
                  class="rounded-3xl bg-indigo-950 w-full p-4 border border-indigo-800 focus:outline-none focus:ring-[5px] focus:ring-indigo-500/50 transition-all" />
              </div>

              <div>
                <label class="block text-sm font-bold text-indigo-300 mb-2 ml-1">Nowe hasło</label>
                <input v-model="passwordForm.new_password" type="password" required
                  class="rounded-3xl bg-indigo-950 w-full p-4 border border-indigo-800 focus:outline-none focus:ring-[5px] focus:ring-indigo-500/50 transition-all" />
              </div>

              <div>
                <label class="block text-sm font-bold text-indigo-300 mb-2 ml-1">Powtórz nowe hasło</label>
                <input v-model="passwordForm.confirm_password" type="password" required
                  class="rounded-3xl bg-indigo-950 w-full p-4 border border-indigo-800 focus:outline-none focus:ring-[5px] focus:ring-indigo-500/50 transition-all"
                  :class="{'border-red-500': passwordForm.confirm_password && !passwordsMatch}" />
                <p v-if="passwordForm.confirm_password && !passwordsMatch" class="text-red-400 text-xs mt-2 ml-4">Hasła nie są identyczne.</p>
              </div>

              <div v-if="passwordError" class="p-4 bg-red-500/20 border border-red-500/50 rounded-2xl text-red-200 text-sm">
                {{ passwordError }}
              </div>

              <div v-if="passwordSuccess" class="p-4 bg-emerald-500/20 border border-emerald-500/50 rounded-2xl text-emerald-200 text-sm">
                Hasło zostało pomyślnie zmienione!
              </div>

              <div class="pt-4">
                <button type="submit" :disabled="changingPassword || !passwordsMatch"
                  class="bg-indigo-600 hover:bg-indigo-500 text-white font-bold py-3 px-8 rounded-2xl shadow-lg transition-all flex items-center gap-2 disabled:opacity-50">
                  <i v-if="changingPassword" class="pi pi-spin pi-spinner"></i>
                  {{ changingPassword ? 'Zmienianie...' : 'Zmień hasło' }}
                </button>
              </div>
            </form>
          </div>

        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, computed } from 'vue';
import { useAuthStore } from '../stores/auth';
import Select from 'primevue/select';

const auth = useAuthStore();
const activeSection = ref('general');
const saving = ref(false);
const settingsSuccess = ref(false);
const settingsError = ref('');
const changingPassword = ref(false);
const passwordError = ref('');
const passwordSuccess = ref('');

const settings = reactive({
  default_currency: 'PLN'
});

const passwordForm = reactive({
  old_password: '',
  new_password: '',
  confirm_password: ''
});

const passwordsMatch = computed(() => {
  return passwordForm.new_password === passwordForm.confirm_password && passwordForm.new_password !== '';
});

onMounted(async () => {
  if (!auth.userProfile) {
    await auth.fetchProfile();
  }
  if (auth.userProfile) {
    settings.default_currency = auth.userProfile.default_currency;
  }
});

const saveGeneralSettings = async () => {
  saving.value = true;
  settingsSuccess.value = false;
  settingsError.value = '';

  const result = await auth.updateProfile({ default_currency: settings.default_currency });
  saving.value = false;
  
  if (result.success) {
    settingsSuccess.value = true;
    setTimeout(() => { settingsSuccess.value = false; }, 5000);
  } else {
    settingsError.value = result.error;
  }
};

const handleChangePassword = async () => {
  if (!passwordsMatch.value) return;
  
  changingPassword.value = true;
  passwordError.value = '';
  passwordSuccess.value = '';
  
  const result = await auth.changePassword(passwordForm.old_password, passwordForm.new_password);
  
  changingPassword.value = false;
  
  if (result.success) {
    passwordSuccess.value = true;
    passwordForm.old_password = '';
    passwordForm.new_password = '';
    passwordForm.confirm_password = '';
    setTimeout(() => { passwordSuccess.value = false; }, 5000);
  } else {
    passwordError.value = result.error;
  }
};
</script>

<style scoped>
.animate-fade-in {
  animation: fadeIn 0.3s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
