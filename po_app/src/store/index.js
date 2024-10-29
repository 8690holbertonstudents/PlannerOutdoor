import { createStore } from "vuex";

export default createStore({
  state: {
    userLoggedIn: false,
    username: "",
  },
  getters: {
    isLoggedIn(state) {
      return state.userLoggedIn;
    },
    getUsername(state) {
      return state.username;
    },
    getAccessToken(state) {
      return state.accessToken;
    },
  },
  mutations: {
    setUserLoggedIn(state, status) {
      state.userLoggedIn = status;
    },
    setUsername(state, username) {
      state.username = username;
    },
    setAccessToken(state, token) {
      state.accessToken = token;
    },
    clearAccessToken(state) {
      state.accessToken = null;
    },
    logout(state) {
      state.userLoggedIn = false;
      state.username = "";
      state.accessToken = null;
    },
    clearUserData(state) {
      state.accessToken = null;
      state.user = null;
      state.isAuthenticated = false;
    },
  },
  actions: {
    login({ commit }, { username, token }) {
      commit("setUserLoggedIn", true);
      commit("setUsername", username);
      commit("setAccessToken", token);
    },
    logout({ commit }) {
      commit("logout");
    },
  },
  modules: {},
});
