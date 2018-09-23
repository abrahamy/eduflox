import * as coreapi from "coreapi";

const API_SCHEMA_PATH = "/api/docs/schema.js";

export const CoreAPI = {
  install(Vue) {
    let auth = new coreapi.auth.SessionAuthentication({
      csrfCookieName: "csrftoken",
      csrfHeaderName: "X-CSRFToken"
    });

    Object.defineProperty(Vue, "$client", {
      value: new coreapi.Client({ auth: auth }),
      writable: false
    });
  }
};

const plugins = [CoreAPI];

export default {
  install(Vue) {
    plugins.map(plugin => Vue.use(plugin));
  }
};
