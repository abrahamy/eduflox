import Vue from "vue";
import Buefy from "buefy";
import VSchool from "./school/List";
import VSchoolForm from "./school/Form";
import "@mdi/font/css/materialdesignicons.min.css";
import "../assets/scss/app.scss";

Vue.use(Buefy);

const components = {
  VSchool,
  VSchoolForm
};

export default components;
