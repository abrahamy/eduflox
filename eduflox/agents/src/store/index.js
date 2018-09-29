import Vue from "vue";
import Vuex from "vuex";
import { Actions as A, Mutations as M } from "./constants";
import schoolActions from "./actions/school";
import serviceActions from "./actions/service";

Vue.use(Vuex);

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
    [M.SetServices](state, services) {
      state.services = [...services];
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
      setTimeout(commit, 5000, M.SetErrorMessage, "");
    },
    ...schoolActions,
    ...serviceActions
  }
});
