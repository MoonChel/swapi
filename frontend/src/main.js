// This is the main.js file. Import global CSS and scripts here.
// The Client API can be used here. Learn more: gridsome.org/docs/client-api
import '~/assets/pico.min.css'
import '~/assets/notifications.css'

import DefaultLayout from '~/layouts/Default.vue'
import Notifications from 'vue-notification/dist/ssr.js'

export default function (Vue, { router, head, isClient }) {
  Vue.use(Notifications)

  // Set default layout as a global component
  Vue.component('Layout', DefaultLayout)
}
