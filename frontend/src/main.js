import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios'
import router from './router'
import App from './App.vue'

axios.defaults.baseURL = 'http://localhost:8000';

const app = createApp(App)
app.use(createPinia())
app.use(router)
app.mount('#app')
