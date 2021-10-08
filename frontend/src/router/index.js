import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '../views/Main.vue'
import Detail from '../views/Detail.vue'
import Checkair from '../views/Checkair.vue'
import Workoutscheduler from '../views/Workoutscheduler.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Main',
    component: Main
  },
  {
    path: '/details/:city',
    name: 'Detail',
    component: Detail,
    props: r => ({city: r.params.city}),
  },
  {
    path: '/checkair',
    name: 'Check air',
    component: Checkair
  },
  {
    path: '/workoutscheduler',
    name: 'Workout scheduler',
    component: Workoutscheduler
  },
]

const router = new VueRouter({
  routes
})

export default router
