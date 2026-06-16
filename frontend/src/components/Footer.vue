<template>
    <footer class="bg-indigo-950 border-t border-indigo-900 py-8 mt-auto shadow-2xl">
      <div class="container mx-auto px-4 flex flex-col md:flex-row justify-between items-center text-indigo-400 text-sm">
        <div class="mb-4 md:mb-0">
          <span class="font-semibold text-indigo-300">SubManager</span> 
          &copy; 2026. Wszystkie prawa zastrzeżone.
        </div>

        <div class="flex items-center space-x-4">
          <a href="https://github.com/grzegory4/subscription_manager" target="_blank"><i class="pi pi-github text-indigo-300 hover:text-indigo-100 transition-colors"></i></a>
          <span class="text-indigo-800">|</span>
          <div class="flex gap-2">
            <span class="px-2 py-0.5 bg-indigo-900 text-indigo-300 border border-indigo-800 rounded text-[10px] uppercase font-bold tracking-tighter">Django 5</span>
            <span class="px-2 py-0.5 bg-indigo-900 text-indigo-300 border border-indigo-800 rounded text-[10px] uppercase font-bold tracking-tighter">Vue 3</span>
            <span class="px-2 py-0.5 bg-indigo-900 text-indigo-300 border border-indigo-800 rounded text-[10px] uppercase font-bold tracking-tighter">Tailwind</span>
          </div>
        </div>
      </div>
    </footer>
</template>

<style scoped>
  @import "primeicons/primeicons.css";
  @import "tailwindcss";
</style>