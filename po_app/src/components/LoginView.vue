<template>
  <div>
    <span>
      <a
        v-if="userLoggedIn"
        @click.prevent="goToAccountManager"
        class="login-item"
      >
        {{ username }} connected
      </a>
    </span>
    <span class="login-item">
      <img
        src="/images/logout_white.png"
        alt="logout-img"
        v-if="userLoggedIn"
        @click.prevent="openLogoutModal"
      />
      <a v-else @click.prevent="goToLogin" class="login-link"> LOGIN </a>
      <LogoutPrompt
        v-if="showModal"
        :show="showModal"
        @close="showModal = false"
      />
    </span>
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
  text-decoration: none;
  cursor: pointer;
}

.login-item {
  vertical-align: middle;
}

img {
  padding-right: 1rem;
  padding-left: 1rem;
  padding-top: 2px;
  height: 25px;
  cursor: pointer;
}
</style>
