//import Vue from "vue";
import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import WeatherView from "@/views/WeatherView.vue";
import CreateAccountView from "@/views/CreateAccountView.vue";
import AccountManagerView from "@/views/AccountManagerView.vue";
import WeatherDetailsView from "@/views/WeatherDetailsView.vue";

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
  {
    path: "/Account",
    name: "Account",
    component: AccountManagerView,
  },
  {
    path: "/WeatherDetails/:itemCity/:itemDt",
    name: "WeatherDetails",
    component: WeatherDetailsView,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
