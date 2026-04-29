import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: () => import('../views/DashboardView.vue')
    },
    {
      path: '/add',
      name: 'add-subscription',
      component: () => import('../views/AddSubscriptionView.vue')
    },
    {
      path: '/edit/:id',
      name: 'edit-subscription',
      component: () => import('../views/EditSubscriptionView.vue')
    },
  ]
})

export default router