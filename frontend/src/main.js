import Vue from 'vue'
import App from './App.vue'
import router from './router'

import '@/assets/pico.min.css'
import '@/assets/notifications.css'

import Notifications from 'vue-notification/dist/ssr.js'


Vue.config.productionTip = false

Vue.use(Notifications)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
