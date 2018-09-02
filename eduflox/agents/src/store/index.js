import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import * as K from "./constants";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    schools: [],
    services: [],
    columns: [],
    loading: false,
    error: "",
    [K.columnTypes.SCHOOL]: [
      {
        field: "name",
        label: "Name",
        sortable: true
      },
      {
        field: "code",
        label: "Code",
        sortable: true
      },
      {
        field: "location",
        label: "Location",
        sortable: true
      },
      {
        field: "district",
        label: "District",
        sortable: true
      },
      {
        field: "status",
        label: "Status",
        sortable: true
      },
      {
        field: "created_at",
        label: "Date Created",
        sortable: true,
        centered: true
      }
    ],
    urls: {
      school: "/api/schools/"
    }
  },
  mutations: {
    setLoadingState(state, isLoading) {
      state.loading = isLoading;
    },
    setSchoolData(state, schools) {
      state.schools = [...schools];
    },
    updateErrorMessage(state, error) {
      state.error = error;
    },
    setTableColumns(state, columnType) {
      state.columns = [...state[columnType]];
    }
  },
  actions: {
    [K.FETCH_SCHOOLS]({ commit, state }, toggleLoading = true) {
      if (toggleLoading) {
        commit("setLoadingState", true);
      }

      let turnLoadingOff = () => {
        if (toggleLoading) {
          commit("setLoadingState", false);
        }
      };

      axios
        .get(state.urls.school)
        .then(response => {
          commit("setSchoolData", response.data);
          console.log(response.data);
          turnLoadingOff();
        })
        .catch(err => {
          turnLoadingOff();
          commit(
            "updateErrorMessage",
            err.response ? err.response.statusText : err.message
          );
        });
    },
    [K.SCHOOL_INIT]({ commit }) {
      commit("setTableColumns", K.columnTypes.SCHOOL);
    },
    [K.CREATE_SCHOOL]({ commit, state }, data) {
      commit("setLoadingState", true);
      return axios
        .post(state.urls.school, data)
        .then(response => {
          commit("setLoadingState", false);
          return Promise.resolve(response);
        })
        .catch(err => {
          commit("setLoadingState", false);
          return Promise.reject(err);
        });
    }
  }
});
