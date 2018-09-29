import Vue from "vue";
import Vuex from "vuex";
import { Actions as A, Mutations as M } from "./constants";
import schoolActions from "./actions/school";
import serviceActions from "./actions/service";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    isAdminUser: window.isAdminUser || false,
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
    [M.SetServices](state, services) {
      state.services = [...services];
    },
    [M.SetErrorMessage](state, errorMessage) {
      state.errorMessage = errorMessage;
    }
  },
  actions: {
    [A.SendError]({ commit }, errorMessage) {
      commit(M.SetErrorMessage, errorMessage);
      // clear the error message after 5 seconds
      setTimeout(commit, 5000, M.SetErrorMessage, "");
    },
    [A.HandleAsyncAError]({ commit, dispatch }, err) {
      commit(M.SetIsLoading, false);

      let message = err.message;
      if (err.response && err.response.data) {
        message = err.response.data.detail || err.response.statusText;
      }

      dispatch(A.SendError, message);
    },
    ...schoolActions,
    ...serviceActions
  }
});
