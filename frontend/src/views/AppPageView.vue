<template>
  <div class="flex grow flex-col">
    
    <section class="py-16 md:py-24 lg:py-32 relative overflow-hidden">
      <div class="absolute top-10 left-10 w-96 h-96 bg-indigo-600/20 rounded-full blur-[120px]"></div>
      <div class="absolute bottom-20 right-20 w-96 h-96 bg-emerald-500/10 rounded-full blur-[120px]"></div>

      <div class="max-w-6xl mx-auto px-4 md:px-8 grid grid-cols-1 lg:grid-cols-2 items-center relative z-10">
        
        <div class="text-center lg:text-left space-y-8 animate-slide-in-left order-2 lg:order-1">
          
          <h1 class="text-5xl md:text-7xl font-black tracking-tighter leading-[1.1] text-white">
            Przejmij kontrolę nad <br/>
            <span class="text-transparent bg-clip-text bg-linear-to-r from-indigo-400 to-emerald-400">
              subskrypcjami.
            </span>
          </h1>
          
          <p class="text-lg md:text-xl text-indigo-200/80 leading-relaxed max-w-xl mx-auto lg:mx-0 font-medium">
            Wszystkie Twoje usługi streamingowe, abonamenty i płatności w jednym miejscu. Śledź wydatki, przeliczaj waluty i nigdy nie przegap terminu płatności.
          </p>
          
          <div class="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start pt-4">
            <router-link :to="{ name: 'register' }">
              <button class="w-full sm:w-auto bg-indigo-600 hover:bg-indigo-500 text-white font-black py-5 px-10 rounded-2xl shadow-2xl shadow-indigo-600/30 transition-all hover:-translate-y-1 active:scale-95 text-lg">
                Rozpocznij za darmo
              </button>
            </router-link>
            <router-link :to="{ name: 'login' }">
              <button class="w-full sm:w-auto bg-indigo-900/30 hover:bg-indigo-900/50 text-indigo-200 border border-indigo-700/50 py-5 px-10 rounded-2xl font-bold transition-all text-lg">
                Zaloguj się
              </button>
            </router-link>
          </div>
        </div>

        <div class="relative animate-slide-in-right order-1 lg:order-2 px-4 lg:px-0">
          <div class="relative z-10 perspective-1000 group">
            <div class="relative transform transition-all duration-700 group-hover:rotate-x-2 group-hover:rotate-y-2deg group-hover:scale-[1.03] animate-float flex justify-center">
              <img 
                src="../assets/hero.png" 
                alt="SubManager Dashboard" 
                class="max-h-100 lg:max-h-137.5 w-auto object-contain select-none pointer-events-none"
              />
            
            </div>

            <div class="absolute -inset-4 bg-indigo-500/10 rounded-[3.5rem] blur-2xl -z-10 opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>
          </div>

        </div>

      </div>
    </section>

    <section class="py-20 bg-indigo-950/50 relative overflow-hidden">
      <div class="max-w-6xl mx-auto px-4 md:px-8">
        <div class="text-center mb-16 space-y-4">
          <h2 class="text-3xl md:text-4xl font-black text-white tracking-tight">Wszystko, czego potrzebujesz</h2>
          <p class="text-indigo-400 font-medium max-w-2xl mx-auto">Skup się na tym, co oglądasz lub czego słuchasz, a my zajmiemy się resztą.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div class="bg-indigo-900/40 border border-indigo-800/50 p-10 rounded-[2.5rem] hover:border-indigo-500/50 transition-all group">
            <div class="w-16 h-16 bg-indigo-600 rounded-3xl flex items-center justify-center mb-8 shadow-lg shadow-indigo-600/20 group-hover:rotate-12 transition-transform duration-500">
              <i class="pi pi-chart-line text-2xl text-white"></i>
            </div>
            <h3 class="text-2xl font-bold text-white mb-4">Analiza budżetu</h3>
            <p class="text-indigo-300/80 leading-relaxed font-medium">
              Przejrzyste statystyki miesięczne i roczne. Zobacz dokładnie, gdzie trafiają Twoje pieniądze każdego miesiąca.
            </p>
          </div>

          <div class="bg-indigo-900/40 border border-indigo-800/50 p-10 rounded-[2.5rem] hover:border-indigo-500/50 transition-all group">
            <div class="w-16 h-16 bg-emerald-600 rounded-3xl flex items-center justify-center mb-8 shadow-lg shadow-emerald-600/20 group-hover:rotate-12 transition-transform duration-500">
              <i class="pi pi-sync text-2xl text-white"></i>
            </div>
            <h3 class="text-2xl font-bold text-white mb-4">Przeliczanie walut</h3>
            <p class="text-indigo-300/80 leading-relaxed font-medium">
              Automatyczne przeliczanie subskrypcji w USD i EUR na Twoją domyślną walutę. Żadnych niespodzianek przy kursach bankowych.
            </p>
          </div>

          <div class="bg-indigo-900/40 border border-indigo-800/50 p-10 rounded-[2.5rem] hover:border-indigo-500/50 transition-all group">
            <div class="w-16 h-16 bg-orange-600 rounded-3xl flex items-center justify-center mb-8 shadow-lg shadow-orange-600/20 group-hover:rotate-12 transition-transform duration-500">
              <i class="pi pi-bell text-2xl text-white"></i>
            </div>
            <h3 class="text-2xl font-bold text-white mb-4">Powiadomienia</h3>
            <p class="text-indigo-300/80 leading-relaxed font-medium">
              Bądź na bieżąco z terminami płatności. System poinformuje Cię o nadchodzących rachunkach z wyprzedzeniem.
            </p>
          </div>
        </div>
      </div>
    </section>

    <section class="py-20 relative px-4">
      <div class="max-w-6xl mx-auto bg-linear-to-r from-indigo-600 to-indigo-800 rounded-[3rem] p-12 md:p-20 shadow-2xl relative overflow-hidden">
        <div class="absolute top-0 right-0 w-64 h-64 bg-white/5 rounded-full -mr-32 -mt-32 blur-3xl"></div>
        
        <div class="relative z-10 flex flex-col md:flex-row items-center justify-between gap-10">
          <div class="text-center md:text-left space-y-4">
            <h2 class="text-3xl md:text-5xl font-black text-white leading-tight">Gotowy, aby zacząć oszczędzać?</h2>
            <p class="text-indigo-100 text-lg font-medium opacity-80">Dołącz do użytkowników, którzy już optymalizują swoje wydatki.</p>
          </div>
          <router-link :to="{ name: 'register' }">
            <button class="bg-white text-indigo-700 hover:bg-indigo-50 font-black py-5 px-12 rounded-2xl transition-all shadow-xl hover:-translate-y-1 active:scale-95 text-xl">
              Utwórz konto
            </button>
          </router-link>
        </div>
      </div>
    </section>

  </div>
</template>

<script setup>
</script>

<style scoped>
@import "primeicons/primeicons.css";

.animate-slide-in-left {
  animation: slideInLeft 1s cubic-bezier(0.16, 1, 0.3, 1);
}

.animate-slide-in-right {
  animation: slideInRight 1.2s cubic-bezier(0.16, 1, 0.3, 1);
}

.animate-float {
  animation: float 6s ease-in-out infinite;
}

@keyframes slideInLeft {
  from { opacity: 0; transform: translateX(-40px); }
  to { opacity: 1; transform: translateX(0); }
}

@keyframes slideInRight {
  from { opacity: 0; transform: translateX(40px); }
  to { opacity: 1; transform: translateX(0); }
}

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(15px); }
}

.perspective-1000 {
  perspective: 1000px;
}

/* Custom rotate utility if Tailwind version doesn't support it directly */
.group:hover .group-hover\:rotate-x-2 {
  transform: rotateX(4deg);
}

@media (min-width: 1024px) {
  .group:hover .group-hover\:rotate-y-\[-2deg\] {
    transform: rotateX(4deg) rotateY(-4deg);
  }
}
</style>
