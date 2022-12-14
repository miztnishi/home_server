import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import HomeView from "../views/HomeView.vue";
import GraphView from "../views/GraphView.vue";
import AirConditionerSettingView from "../views/AirConditionerSetting.vue"
import LedSettingVue from '@/views/LedSetting.vue';
const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/homeGraph",
    name: "homeGraph",
    component: GraphView,
  },
  {
    path: "/airConditionerSetting",
    name: "airConditionerSetting",
    component: AirConditionerSettingView,
  },
  {
    path: "/ledSetting",
    name: "ledSetting",
    component: LedSettingVue,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
