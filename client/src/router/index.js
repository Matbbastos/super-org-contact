import Vue from "vue";
import Router from "vue-router";

import Root from "../components/Root.vue";
import Home from "../components/Home.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/home",
      name: "Home",
      component: Home
    },

    {
      path: "/",
      name: "Root",
      component: Root
    }
  ]
});
