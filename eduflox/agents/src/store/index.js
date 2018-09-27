import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import { API, Actions as A, Mutations as M } from "./constants";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    schema: window.schema,
    schools: [],
    services: [],
    loading: false,
    error: ""
  },
  mutations: {
    [M.SetIsLoading](state, isLoading) {
      state.loading = isLoading;
    },
    [M.SetSchools](state, schools) {
      state.schools = [...schools];
    },
    [M.SetErrorMessage](state, error) {
      state.error = error;
    }
  },
  actions: {
    [A.HandleAsyncAError]({ commit }, err) {
      commit(M.SetIsLoading, false);
      commit(
        M.SetErrorMessage,
        err.response ? err.response.statusText : err.message
      );
    },
    [A.GetAllSchools]({ commit, dispatch }) {
      commit(M.SetIsLoading, true);
      axios
        .get(API.schools)
        .then(response => {
          commit(M.SetIsLoading, false);
          commit(M.SetSchools, response.data);
        })
        .catch(err => {
          dispatch(A.HandleAsyncAError, err);
        });
    },
    [A.AddNewSchool]({ commit, dispatch }, data) {
      commit(M.SetIsLoading, true);
      axios
        .post(API.schools)
        .then(response => {
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
