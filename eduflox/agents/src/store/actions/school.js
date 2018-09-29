import axios from "axios";
import { API, Actions as A, Mutations as M } from "../constants";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

// create CRUD actions for schools
export default {
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
        setTimeout(dispatch, 2000, A.GetAllSchools);
      })
      .catch(err => {
        dispatch(A.HandleAsyncAError, err);
      });
  },
  [A.UpdateExistingSchool]({ commit, dispatch }, school) {
    commit(M.SetIsLoading, true);
    let url = `${API.schools}${school.id}/`;
    axios
      .put(url, school)
      .then(() => {
        commit(M.SetIsLoading, false);
        // wait for 2 seconds and reload schools
        setTimeout(dispatch, 2000, A.GetAllSchools);
      })
      .catch(err => {
        dispatch(A.HandleAsyncAError, err);
      });
  },
  [A.DeleteExistingSchool]({ commit, dispatch }, school) {
    commit(M.SetIsLoading, true);
    let url = `${API.schools}${school.id}/`;
    axios
      .delete(url)
      .then(() => {
        commit(M.SetIsLoading, false);
        // wait for 2 seconds and reload schools
        setTimeout(dispatch, 2000, A.GetAllSchools);
      })
      .catch(err => {
        dispatch(A.HandleAsyncAError, err);
      });
  }
};
