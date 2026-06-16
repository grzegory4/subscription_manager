<template>
  <div class="min-h-screen flex items-center justify-center p-4 bg-indigo-950">
    
    <div class="bg-indigo-900 w-full max-w-lg flex flex-col items-center justify-center rounded-3xl p-12 text-white shadow-2xl border border-indigo-800">
      
      <div class="mb-8 relative">
        <i class="pi pi-exclamation-circle text-8xl text-indigo-500 opacity-20 absolute inset-0 scale-150 blur-lg"></i>
        <i class="pi pi-map text-7xl text-indigo-400 relative z-10"></i>
      </div>

      <h1 class="text-6xl font-black text-indigo-300 mb-2">404</h1>
      <h2 class="text-2xl font-bold mb-6 text-center">Nie odnaleziono strony</h2>
      
      <p class="text-indigo-300 text-center mb-10 leading-relaxed">
        Strona, której szukasz, prawdopodobnie wygasła lub została przeniesiona pod inny adres. Nie martw się, Twoje subskrypcje są bezpieczne!
      </p>

      <router-link to="/dashboard" class="w-full">
        <button class="bg-indigo-600 rounded-2xl py-4 w-full text-xl font-bold hover:bg-indigo-500 transition duration-300 shadow-lg shadow-indigo-500/20 focus:outline-none focus:ring-[5px] focus:ring-indigo-500 flex items-center justify-center gap-3">
          <i class="pi pi-home"></i>
          Wróć do Dashboardu
        </button>
      </router-link>

      <p class="mt-8 text-indigo-400 text-sm">
        Jeśli uważasz, że to błąd, 
        <a href="mailto:support@submanager.pl" class="underline hover:text-indigo-200 transition-colors">skontaktuj się z nami</a>.
      </p>
      
    </div>

  </div>
</template>

<script setup>
</script>

<style scoped>
@import "primeicons/primeicons.css";

</style>