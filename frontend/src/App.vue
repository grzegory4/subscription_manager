<template>
  <div class="min-h-screen flex flex-col bg-indigo-950 text-white">
    <Navbar/>

    <main class="container mx-auto px-4 grow flex flex-col">
      <router-view />
    </main>

    <Footer/>
    
  </div>
</template>
<script setup>
  import Navbar from './components/Navbar.vue';
  import Footer from './components/Footer.vue';
  import { useAuthStore } from './stores/auth';
  const auth = useAuthStore();
</script>
  
<style scoped>
  @import "primeicons/primeicons.css";
  @import "tailwindcss";
</style>