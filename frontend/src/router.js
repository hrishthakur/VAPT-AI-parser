import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from './components/Dashboard.vue';
import UploadFile from './components/UploadFile.vue';

const routes = [
  { path: '/dashboard', component: Dashboard },
  { path: '/upload', component: UploadFile },
  { path: '/', redirect: '/dashboard' } // Redirect to dashboard by default
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;