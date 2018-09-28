import Vue from "vue";
import components from "./components";
import store from "./store";
import plugin from "./plugin";

Vue.config.productionTip = false;
Vue.use(plugin);

/* eslint no-new: off */
new Vue({
  el: "#app",
  store,
  components
});
