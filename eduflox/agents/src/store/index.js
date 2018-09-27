import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import { API, Actions as A, Mutations as M } from "./constants";

Vue.use(Vuex);

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

export default new Vuex.Store({
  state: {
    schema: window.schema,
    schools: [],
    services: [],
    loading: false,
    errorMessage: ""
  },
  mutations: {
    [M.SetIsLoading](state, isLoading) {
      state.loading = isLoading;
    },
    [M.SetSchools](state, schools) {
      state.schools = [...schools];
    },
    [M.SetErrorMessage](state, errorMessage) {
      state.errorMessage = errorMessage;
    }
  },
  actions: {
    [A.HandleAsyncAError]({ commit }, err) {
      commit(M.SetIsLoading, false);

      let message = err.message;
      if (err.response && err.response.data) {
        message = err.response.data.detail || err.response.statusText;
      }

      commit(M.SetErrorMessage, message);
      setTimeout(commit, [M.SetErrorMessage, ""], 5000);
    },
    [A.GetAllSchools]({ commit, dispatch }) {
      commit(M.SetIsLoading, true);
      axios
        .get(API.schools)
        .then(response => {
          commit(M.SetIsLoading, false);
          commit(M.SetSchools, response.data.results);
        })
        .catch(err => {
          dispatch(A.HandleAsyncAError, err);
        });
    },
    [A.AddNewSchool]({ commit, dispatch }, data) {
      commit(M.SetIsLoading, true);
      axios
        .post(API.schools, data)
        .then(() => {
          commit(M.SetIsLoading, false);
          // wait for 2 seconds and reload schools
          setTimeout(dispatch, [A.GetAllSchools], 2000);
        })
        .catch(err => {
          dispatch(A.HandleAsyncAError, err);
        });
    }
  }
});
