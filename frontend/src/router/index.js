import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Bookings from '../views/Bookings.vue'
import PageFindVol from '../views/PageFindVol.vue'
import PageFindTrain from '../views/PageFindTrain.vue'

import Offres from "../views/Offres.vue";

import DetailBook from "../views/DetailBook.vue";



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/bookings",
      name: "bookings",
      component: Bookings,
    },
    {
      path: "/bookings/:id",
      name: "detailBooking",
      component: DetailBook,
    },

    {
      path: "/trouver-mon-vol",
      name: "findVol",
      component: PageFindVol,
    },
    {
      path: "/trouver-mon-train",
      name: "findTrain",
      component: PageFindTrain,
    },
    {
      path: "/offres",
      name: "offres",
      component: Offres,
    },
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/AboutView.vue')
    // }
  ],
});

export default router
