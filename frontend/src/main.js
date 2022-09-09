import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from "./store";
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";

import './assets/main.css'

const app = createApp(App)

app.use(router)
const options = {
  position: "top-right",
  timeout: 5000,
  closeOnClick: true,
  pauseOnFocusLoss: true,
  pauseOnHover: true,
  draggable: true,
  draggablePercent: 0.6,
  showCloseButtonOnHover: false,
  hideProgressBar: false,
  closeButton: "button",
  icon: true,
  rtl: false
};
app.use(Toast,options)

app.use(store)

app.mount('#app')
