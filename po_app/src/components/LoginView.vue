<template>
  <div>
    <a
      v-if="userLoggedIn"
      @click.prevent="goToAccountManager"
      class="login-link"
    >
      {{ username }} connected
    </a>
    <img
      src="/images/logout_white.png"
      alt="logout-img"
      v-if="userLoggedIn"
      class="logout-link"
      @click.prevent="openLogoutModal"
    />
    <a v-else @click.prevent="goToLogin" class="login-link"> LOGIN </a>
    <LogoutPrompt
      v-if="showModal"
      :show="showModal"
      @close="showModal = false"
    />
  </div>
</template>

<script>
import LogoutPrompt from "@/components/LogoutPrompt.vue";

export default {
  name: "LoginView",
  components: { LogoutPrompt },
  data() {
    return {
      showModal: false,
    };
  },
  computed: {
    userLoggedIn() {
      return this.$store.getters.isLoggedIn;
    },
    username() {
      return this.$store.getters.getUsername;
    },
  },
  methods: {
    goToLogin() {
      this.$router.push("/Login");
    },
    goToAccountManager() {
      this.$router.push("/Account");
    },
    openLogoutModal() {
      this.showModal = true;
    },
  },
};
</script>

<style scoped>
.login-link {
  padding-bottom: 5px;
  text-decoration: none;
  cursor: pointer;
}
#login-item img {
  padding-right: 10px;
  padding-left: 10px;
  padding-top: 2px;
  height: 15px;
  cursor: pointer;
}
</style>
