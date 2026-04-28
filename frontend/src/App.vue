<template>
  <nav>
    <router-link to="/login">Logowanie</router-link> |
    <router-link to="/dashboard">Dashboard</router-link>
  </nav>
  
  <router-view></router-view>
</template>

<style>
nav { padding: 30px; text-align: center; }
body { font-family: sans-serif; background: #f4f4f4; }
</style>