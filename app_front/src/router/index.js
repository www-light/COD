import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import AboutPage from '../views/AboutPage.vue';
import DetectPage from '../views/DetectPage.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomePage
    },
    {
      path: '/about',
      name: 'About',
      component: AboutPage,
      children: [
        {
          path: 'introduction',
          name: 'AboutIntroduction',
          component: AboutPage,
          beforeEnter(to, from, next) {
            to.params.activeSection = 'introduction';
            next();
          }
        },
        {
          path: 'importance',
          name: 'AboutImportance',
          component: AboutPage,
          beforeEnter(to, from, next) {
            to.params.activeSection = 'importance';
            next();
          }
        },
        {
          path: 'protection',
          name: 'AboutProtection',
          component: AboutPage,
          beforeEnter(to, from, next) {
            to.params.activeSection = 'protection';
            next();
          }
        }
      ]
    },
    {
      path: '/detect',
      name: 'Detect',
      component: DetectPage
    }
  ]
});

export default router;