import Vue from "vue";
import Buefy from "buefy";
import VApp from "./App";
import VSchool from "./school/List";
import "@mdi/font/css/materialdesignicons.min.css";
import "../assets/scss/app.scss";

Vue.use(Buefy);

const components = {
  VApp,
  VSchool
};

export default components;
