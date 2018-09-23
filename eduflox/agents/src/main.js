import Vue from "vue";
import components from "./components";
import store from "./store";
import plugins from "./plugins";

Vue.config.productionTip = false;
Vue.use(plugins);

/* eslint no-new: off */
new Vue({
  el: "#app",
  store,
  components
});
