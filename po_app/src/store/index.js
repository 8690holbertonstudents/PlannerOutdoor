import { createStore } from "vuex";

export default createStore({
  state: {
    accessToken: null,
    userLoggedIn: false,
    username: null,
    userId: null,
  },
  getters: {
    isLoggedIn(state) {
      return state.userLoggedIn;
    },
    getUsername(state) {
      return state.username;
    },
    getUserId(state) {
      return state.userId;
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
    setUserId(state, userId) {
      state.userId = userId;
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
    login({ commit }, { username, userId, token }) {
      commit("setUserLoggedIn", true);
      commit("setUsername", username);
      commit("setUserId", userId);
      commit("setAccessToken", token);
    },
    logout({ commit }) {
      commit("logout");
    },
  },
  modules: {},
});
