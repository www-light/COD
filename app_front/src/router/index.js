import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import AboutPage from '../views/AboutPage.vue'
import DetectPage from '../views/DetectPage.vue'
<<<<<<< HEAD
// import AnimalsList from '../components/AnimalsList.vue' 
=======
//import AnimalsList from '../components/AnimalsList.vue' 
>>>>>>> homepage

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
      component: AboutPage  
    },  
    {  
      path: '/detect',  
      name: 'Detect',  
      component: DetectPage  
    },    
<<<<<<< HEAD
    // {  
    //   path: '/animals',  
    //   name: 'Animals',  
    //   component: AnimalsList  
    // },  
=======
    
  //{  
  //    path: '/animals',  
     // name: 'Animals',  
      //component: AnimalsList  
    //},  
>>>>>>> homepage
  ]
})

export default router
