import Vue from "vue";
import Router from "vue-router";

import Root from "../components/Root.vue";
import Home from "../components/Home.vue";
import NotFound from "../components/NotFound.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  // base: process.env.BASE_URL,
  base: "https://superorgcontact-1614087097383.firebaseapp.com",
  routes: [
    {
      path: "/",
      name: "Root",
      component: Root
    },

    {
      path: "/home",
      name: "Home",
      component: Home
    },

    {
      path: '*',
      component: NotFound
    }

  ]
});
