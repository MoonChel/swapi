import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import CsvFile from '../views/CsvFile.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/csv-file/:id',
    name: 'CsvFile',
    component: CsvFile
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
