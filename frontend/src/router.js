import { createRouter, createWebHistory } from "vue-router";
import App from "./App.vue";
import Home from "./components/Home.vue"
import LogIn from "./components/LogIn.vue"
import SignUp from "./components/SignUp.vue"
import Services from "./components/Services.vue";


const routes = [
  {
    path: "/",
    name: "root",
    component: App,
  },
  {
    path:"/home",
    name: "home",
    component: Home,
  },
  {
    path:"/login",
    name: "login",
    component: LogIn,
  },
  {
    path:"/signup",
    name: "signup",
    component: SignUp,
  },
  {
    path:"/user/home",
    name: "user-home",
    component: Home,
    meta: { requiresAuth: true }, 
  },
  {
    path:"/user/services",
    name: "user-services",
    component: Services,
    meta: { requiresAuth: true }, 
  },

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
