import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

import Movie from '../views/MovieDetail.vue'
import AllMovies from '../views/AllMovies.vue'
import GenreMovie from '../views/GenreMovie.vue'
import SearchMovie from '../views/SearchMovie.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/movies',
    name: 'AllMovies',
    component: AllMovies
  },
  {
    path: '/movie/:movie_id',
    name: 'Movie',
    component: Movie
  },
  {
    path: '/movies/:genre_name',
    name: 'GenreMovie',
    component: GenreMovie
  },
  {
    path: '/search/:searchTerm',
    name: 'SearchMovie',
    component: SearchMovie
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
