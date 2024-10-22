//import Vue from "vue";
import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import WeatherView from "@/views/WeatherView.vue";
import CreateAccountView from "@/views/CreateAccountView.vue";

//import WeatherView from "@/views/WeatherView.vue";
//import WeatherDetailsView from "@/views/WeatherDetailsView.vue";
//import AccountManageView from "@/views/AccountManageView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/Weather",
    name: "Weather",
    component: WeatherView,
  },
  {
    path: "/Login",
    name: "Login",
    component: CreateAccountView,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

/*
Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    { path: "/", name: "home", component: HomeView },
    { path: "/weather", name: "weather", component: WeatherView },
    {
      path: "/create-account",
      name: "createAccount",
      component: CreateAccountView,
    },
    {
      path: "/weather-details",
      name: "weatherDetails",
      component: WeatherDetailsView,
    },
    {
      path: "/account-manage",
      name: "accountManage",
      component: AccountManageView,
    },
  ],
});
*/
