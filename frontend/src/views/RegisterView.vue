<template>
  <div class="grow flex items-center justify-center py-12 px-4"> 
    
    <div class="bg-indigo-900 w-full max-w-lg flex flex-col items-center justify-center rounded-3xl p-8 text-white shadow-2xl border border-indigo-800">
      <h1 class="text-3xl font-bold text-center mb-8">Rejestracja</h1>

      <div v-if="errorMessage" class="mb-6 w-full p-4 bg-red-500/20 border border-red-500/50 rounded-2xl flex items-center gap-3 text-red-200 text-sm">
        <i class="pi pi-exclamation-circle text-lg"></i>
        <span>{{ errorMessage }}</span>
      </div>

      <div v-if="successMessage" class="mb-6 w-full p-4 bg-emerald-500/20 border border-emerald-500/50 rounded-2xl flex items-center gap-3 text-emerald-200 text-sm">
        <i class="pi pi-check-circle text-lg"></i>
        <span>{{ successMessage }}</span>
      </div>

      <form @submit.prevent="handleRegister" class="w-full flex flex-col">

        <label class="ml-4 mb-1 text-sm text-indigo-300">Nazwa użytkownika</label>
        <div class="relative mb-4">
          <i class="pi pi-user absolute left-4 top-1/2 -translate-y-1/2 text-indigo-400"></i>
          <input 
            v-model="form.username" 
            type="text" 
            placeholder="uzytkownik123" 
            required 
            class="rounded-3xl bg-indigo-950 w-full py-4 pl-12 focus:outline-none transition-all border border-indigo-800 focus-within:ring-[5px] focus-within:ring-indigo-500/50" 
          />
        </div>

        <label class="ml-4 mb-1 text-sm text-indigo-300">Adres e-mail</label>
        <div class="relative mb-4">
          <i class="pi pi-envelope absolute left-4 top-1/2 -translate-y-1/2 text-indigo-400"></i>
          <input 
            v-model="form.email" 
            type="email" 
            placeholder="adres@email.com" 
            required 
            class="rounded-3xl bg-indigo-950 w-full py-4 pl-12 focus:outline-none transition-all border border-indigo-800 focus-within:ring-[5px] focus-within:ring-indigo-500/50" 
          />
        </div>

        <div class="flex justify-between items-center ml-4 mb-1">
          <label class="text-sm text-indigo-300">Hasło</label>
          <div class="cursor-help text-indigo-400 hover:text-white transition-colors text-xs flex items-center">
            <div class="relative group">
              <span>Wymagania <i class="pi pi-info-circle"></i></span>

              <div class="absolute right-0 bottom-full mb-2 w-64 bg-indigo-950 border border-indigo-500 p-4 rounded-2xl shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all z-50">
                <h3 class="text-xs font-bold mb-3 border-b border-indigo-800 pb-2 uppercase tracking-widest text-indigo-400">
                  Zasady bezpieczeństwa
                </h3>
                <ul class="space-y-2 text-[11px]">
                  <li :class="passwordRequirements.length8 ? 'text-emerald-400' : 'text-gray-400'" class="flex items-center gap-2">
                    <i :class="passwordRequirements.length8 ? 'pi pi-check-circle' : 'pi pi-circle'"></i>
                    Minimum 8 znaków (wymagane)
                  </li>
                  <li :class="passwordRequirements.length12 ? 'text-emerald-400' : 'text-gray-400'" class="flex items-center gap-2">
                    <i :class="passwordRequirements.length12 ? 'pi pi-check-circle' : 'pi pi-circle'"></i>
                    Dłuższe niż 12 znaków
                  </li>
                  <li :class="passwordRequirements.number ? 'text-emerald-400' : 'text-gray-400'" class="flex items-center gap-2">
                    <i :class="passwordRequirements.number ? 'pi pi-check-circle' : 'pi pi-circle'"></i>
                    Co najmniej jedna cyfra
                  </li>
                  <li :class="passwordRequirements.special ? 'text-emerald-400' : 'text-gray-400'" class="flex items-center gap-2">
                    <i :class="passwordRequirements.special ? 'pi pi-check-circle' : 'pi pi-circle'"></i>
                    Znak specjalny (!@#$)
                  </li>
                  <li :class="passwordRequirements.upper ? 'text-emerald-400' : 'text-gray-400'" class="flex items-center gap-2">
                    <i :class="passwordRequirements.upper ? 'pi pi-check-circle' : 'pi pi-circle'"></i>
                    Wielka litera
                  </li>
                </ul>
                <div class="mt-3 pt-2 border-t border-indigo-800 text-[10px] italic text-indigo-500">
                  Twoje hasło powinno mieć ≥8 znaków oraz spełniać co najmniej 2 inne warunki. 
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="relative mb-2">
          <i class="pi pi-lock absolute left-4 top-1/2 -translate-y-1/2 text-indigo-400"></i>
          <input 
            v-model="form.password" 
            :type="showPassword ? 'text' : 'password'" 
            placeholder="••••••••" 
            required 
            class="rounded-3xl bg-indigo-950 w-full py-4 pl-12 focus:outline-none transition-all border border-indigo-800 focus-within:ring-[5px] focus-within:ring-indigo-500/50" 
          />
          <button 
            type="button" 
            @click="showPassword = !showPassword"
            class="absolute right-4 top-1/2 -translate-y-1/2 text-indigo-400 hover:text-indigo-200 transition-colors focus:outline-none"
          >
            <i :class="showPassword ? 'pi pi-eye-slash' : 'pi pi-eye'"></i>
          </button>
        </div>
        
        <div class="mb-4">
          <div class="flex gap-1.5 px-4 mb-2">
            <div v-for="i in 5" :key="i" 
                class="h-1.5 flex-1 rounded-full transition-all duration-500"
                :class="strengthScore >= i ? strengthColorClass : 'bg-indigo-950'">
            </div>
          </div>
          <p class="text-[10px] text-indigo-300/60 px-4 tracking-wider">
            Siła hasła: 
            <span v-if="strengthScore <= 1" class="text-red-400">Zbyt słabe</span>
            <span v-else-if="strengthScore == 2" class="text-orange-400">Słabe</span>
            <span v-else-if="strengthScore == 3" class="text-yellow-400">Dobre</span>
            <span v-else-if="strengthScore == 4" class="text-lime-400">Silne</span>
            <span v-else class="text-emerald-400">Bardzo silne</span>
          </p>
        </div>

        <label class="ml-4 mb-1 text-sm text-indigo-300">Powtórz hasło</label>
        <div class="relative mb-2">
          <i class="pi pi-check-square absolute left-4 top-1/2 -translate-y-1/2 text-indigo-400"></i>
          <input 
            v-model="form.confirmPassword" 
            :type="showPassword ? 'text' : 'password'" 
            placeholder="••••••••" 
            required 
            class="rounded-3xl bg-indigo-950 w-full py-4 pl-12 focus:outline-none transition-all border border-indigo-800 focus-within:ring-[5px] focus-within:ring-indigo-500/50"
            :class="{'focus:ring-red-500 border-red-900/50': form.confirmPassword && !passwordsMatch}" 
          />
        </div>
        <p v-if="form.confirmPassword && !passwordsMatch" class="text-red-400 text-[10px] ml-4 mb-4">Hasła muszą być identyczne!</p>

        <button 
          type="submit" 
          :disabled="!isFormValid || loading"
          class="mt-6 bg-indigo-600 rounded-2xl py-4 mb-6 w-full text-xl font-bold hover:bg-indigo-500 transition duration-300 shadow-lg shadow-indigo-500/20 focus:outline-none focus:ring-[5px] focus:ring-indigo-500 disabled:opacity-50 flex items-center justify-center gap-3"
        >
          <i v-if="loading" class="pi pi-spin pi-spinner text-xl"></i>
          <span>{{ loading ? 'Trwa rejestracja...' : 'Zarejestruj się!' }}</span>
        </button>
        
      </form>

      <div class="text-center text-sm">
        <router-link 
          :to="{ name: 'login' }" 
          class="text-indigo-300 p-1 rounded focus:outline-none focus:ring-2 focus:ring-indigo-500"
        >
          Masz już konto? <span class="text-white font-semibold underline decoration-indigo-400/30 hover:text-indigo-100 transition-all">Zaloguj się!</span>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, computed } from 'vue';
  import { useAuthStore } from '../stores/auth';
  import { useRouter } from 'vue-router';

  const authStore = useAuthStore();
  const router = useRouter();

  const form = ref({
    username: '',
    email: '',
    password: '',
    confirmPassword: ''
  });

  const showPassword = ref(false);
  const loading = ref(false);
  const errorMessage = ref('');
  const successMessage = ref('');

  const passwordRequirements = computed(() => {
    const p = form.value.password;
    return {
      length8: p.length >= 8,
      length12: p.length >= 12,
      number: /[0-9]/.test(p),
      special: /[!@#$%^&*]/.test(p),
      upper: /[A-Z]/.test(p)
    };
  });

  const strengthScore = computed(() => {
    if (!form.value.password) return 0;
    return Object.values(passwordRequirements.value).filter(Boolean).length;
  });

  const strengthColorClass = computed(() => {
    if (strengthScore.value === 0) return 'bg-indigo-950'; 
    if (strengthScore.value === 1) return 'bg-red-500 shadow-[0_0_8px_#ef4444]';
    if (strengthScore.value === 2) return 'bg-orange-500 shadow-[0_0_8px_#f97316]';
    if (strengthScore.value === 3) return 'bg-yellow-500 shadow-[0_0_8px_#eab308]';
    if (strengthScore.value === 4) return 'bg-lime-400 shadow-[0_0_8px_#a3e635]';
    return 'bg-emerald-400 shadow-[0_0_8px_#34d399]';
  });

  const passwordsMatch = computed(() => 
    form.value.password === form.value.confirmPassword && form.value.password !== ''
  );

  const isBasicLengthMet = computed(() => form.value.password.length >= 8);

  const isFormValid = computed(() => {
    return (
      form.value.username.length >= 3 && 
      form.value.email.includes('@') && 
      isBasicLengthMet.value &&
      strengthScore.value >= 3 &&
      passwordsMatch.value
    );
  });

  const handleRegister = async () => {
    if (!isFormValid.value) return;
    
    loading.value = true;
    errorMessage.value = '';
    successMessage.value = '';

    const result = await authStore.register(
      form.value.username,
      form.value.email,
      form.value.password
    );

    loading.value = false;

    if (result.success) {
      successMessage.value = 'Rejestracja zakończona sukcesem! Przekierowanie do logowania...';
      setTimeout(() => {
        router.push('/login');
      }, 2000);
    } else {
      errorMessage.value = result.error;
    }
  };
</script>

<style scoped>
@import "primeicons/primeicons.css";

.shadow-inner {
  box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.3);
}
</style>
