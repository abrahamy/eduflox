import Vue from "vue";
import Vuex from "vuex";
import * as K from "./constants.js";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    schools: [],
    services: [],
    columns: [],
    loading: false,
    error: "",
    [K.colunmTypes.SCHOOL]: [
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
      school: ""
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

      fetch(state.urls.school)
        .then(
          response =>
            response.ok ? response.json() : Promise.reject(response.statusText)
        )
        .then(data => {
          commit("setSchoolData", response.data);
          turnLoadingOff();
        })
        .catch(err => {
          turnLoadingOff();
          commit("updateErrorMessage", err.message);
        });
    },
    [K.SCHOOL_INIT]({ commit }) {
      commit("setTableColumns", K.colunmTypes.SCHOOL);
    },
    [K.CREATE_SCHOOL]({ commit, state }, data) {
      commit("setLoadingState", true);

      let payload = {
        method: "POST",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json; charset=utf-8"
        },
        body: JSON.stringify(data)
      };
      return fetch(state.urls.school, payload)
        .then(response => {
          commit("setLoadingState", false);
          return response.ok ? response : Promise.reject(response.statusText);
        })
        .catch(err => {
          commit("setLoadingState", false);
          return Promise.reject(err.message);
        });
    }
  }
});
