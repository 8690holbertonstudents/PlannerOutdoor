<template>
  <header class="header-container">
    <div id="app-logo">
      <img src="/images/po_white.png" alt="app-logo" @click="goToHome" />
    </div>
    <div id="locate-item">
      <LocateView />
    </div>
    <div id="login-item">
      <LoginView />
    </div>
  </header>
</template>

<script>
import LocateView from "@/components/LocateView.vue";
import LoginView from "@/components/LoginView.vue";

export default {
  name: "PageHeader",
  components: {
    LocateView,
    LoginView,
  },
  methods: {
    goToHome() {
      this.$router.push("/");
    },
  },
};
</script>

<style scoped>
.header-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: var(--header-footer-height);
  width: var(--header-footer-width);
  background-color: var(--color-header-footer);
  color: var(--color-white);
  border-radius: var(--header-footer-border);
  box-shadow: var(--header-footer-shadow);
}

#login-item {
  padding-right: 10px;
}

#locate-item {
  position: center;
}

#app-logo img {
  padding-left: 10px;
  padding-top: 8%;
  height: 20px;
  cursor: pointer;
}
</style>
