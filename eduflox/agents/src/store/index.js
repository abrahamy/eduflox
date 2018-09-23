import Vue from "vue";
import Vuex from "vuex";
import * as K from "./constants";
import * as coreapi from "coreapi";

Vue.use(Vuex);

const client = new coreapi.Client({
  auth: new coreapi.auth.SessionAuthentication({
    csrfCookieName: "csrftoken",
    csrfHeaderName: "X-CSRFToken"
  })
});

export default new Vuex.Store({
  state: {
    schema: window.schema,
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
    ]
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

      let schema = state.schema;
      let action = ["schools", "list"];

      client
        .action(schema, action)
        .then(schools => {
          commit("setSchoolData", schools);
          // eslint-disable-next-line
          console.log(schools);
          turnLoadingOff();
        })
        .catch(err => {
          turnLoadingOff();
          commit("updateErrorMessage", err.message);
        });
    },
    [K.SCHOOL_INIT]({ commit }) {
      commit("setTableColumns", K.columnTypes.SCHOOL);
    },
    [K.CREATE_SCHOOL]({ commit, state }, data) {
      let schema = state.schema;
      let action = ["schools", "create"];

      commit("setLoadingState", true);
      return client
        .action(schema, action, data)
        .then(school => {
          commit("setLoadingState", false);
          return Promise.resolve(school);
        })
        .catch(err => {
          commit("setLoadingState", false);
          return Promise.reject(err);
        });
    }
  }
});
