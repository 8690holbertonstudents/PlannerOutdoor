<template>
  <div><a @click.prevent="goToLogin" class="login-link">LOGIN</a></div>
</template>

<script>
export default {
  name: "LoginView",
  methods: {
    goToLogin() {
      this.$router.push("/Login");
    },
  },
};
</script>

<style scoped>
.login-link {
  text-decoration: none;
  cursor: pointer;
}
</style>
