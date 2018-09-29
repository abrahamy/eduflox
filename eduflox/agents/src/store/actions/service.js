import axios from "axios";
import { API, Actions as A, Mutations as M } from "../constants";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

// create CRUD actions for services
export default {
  [A.GetAllServices]({ commit, dispatch }) {
    commit(M.SetIsLoading, true);
    axios
      .get(API.services)
      .then(response => {
        commit(M.SetIsLoading, false);
        commit(M.SetServices, response.data.results);
      })
      .catch(err => {
        dispatch(A.HandleAsyncAError, err);
      });
  },
  [A.AddNewService]({ commit, dispatch }, data) {
    commit(M.SetIsLoading, true);
    axios
      .post(API.services, data)
      .then(() => {
        commit(M.SetIsLoading, false);
        // wait for 2 seconds and reload schools
        setTimeout(dispatch, 2000, A.GetAllServices);
      })
      .catch(err => {
        dispatch(A.HandleAsyncAError, err);
      });
  },
  [A.UpdateExistingService]({ commit, dispatch }, service) {
    commit(M.SetIsLoading, true);
    let url = `${API.services}${service.id}/`;
    axios
      .put(url, service)
      .then(() => {
        commit(M.SetIsLoading, false);
        // wait for 2 seconds and reload schools
        setTimeout(dispatch, 2000, A.GetAllServices);
      })
      .catch(err => {
        dispatch(A.HandleAsyncAError, err);
      });
  },
  [A.DeleteExistingService]({ commit, dispatch }, service) {
    commit(M.SetIsLoading, true);
    let url = `${API.services}${service.id}/`;
    axios
      .delete(url)
      .then(() => {
        commit(M.SetIsLoading, false);
        // wait for 2 seconds and reload schools
        setTimeout(dispatch, 2000, A.GetAllServices);
      })
      .catch(err => {
        dispatch(A.HandleAsyncAError, err);
      });
  }
};
