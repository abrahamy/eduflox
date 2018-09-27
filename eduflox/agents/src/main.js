import Vue from "vue";
import components from "./components";
import store from "./store";

Vue.config.productionTip = false;

/* eslint no-new: off */
new Vue({
  el: "#app",
  store,
  components
});
