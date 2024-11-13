<template>
  <div class="create-account-container">
    <form @submit.prevent="register" class="account-item">
      <h3>Create an Account</h3>
      <input
        type="text"
        v-model="username"
        placeholder="Username"
        title="Maximum 50 characters"
        required
      />
      <input
        type="email"
        v-model="email"
        placeholder="Email"
        title="Enter a valid email type xxx@xxxx.xx"
        required
      />
      <input
        type="password"
        v-model="password"
        placeholder="Password"
        title="Valid password: At least 8 characters, one uppercase, one lowercase, one number, one special character, and all different"
        required
      />
      <input
        type="address"
        v-model="address"
        placeholder="Enter your home address"
        title="Enter your home address"
        required
      />
      <button type="submit">Register</button>
      <p v-if="successMsg">{{ successMsg }}</p>
      <p v-if="errorMsg" class="error">{{ errorMsg }}</p>
    </form>
    <form @submit.prevent="login" class="account-item">
      <h3>Already have an account?</h3>
      <input
        type="text"
        v-model="loginUsername"
        placeholder="Username"
        required
      />
      <input
        type="password"
        v-model="loginPassword"
        placeholder="Password"
        required
      />
      <div class="button-container">
        <button type="submit">Login</button>
        <button @click="showRecoveryModal = true">Forgot Password?</button>
        <RecoveryPrompt
          v-if="showRecoveryModal"
          :show="showRecoveryModal"
          @close="showRecoveryModal = false"
        />
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import RecoveryPrompt from "@/components/RecoveryPrompt.vue";

export default {
  name: "CreateAccountView",
  components: { RecoveryPrompt },
  data() {
    return {
      username: "",
      email: "",
      password: "",
      address: "",
      loginUsername: "",
      loginPassword: "",
      successMsg: "",
      errorMsg: "",
      recoveryUsername: "",
      recoveryEmail: "",
      recoveryMsg: "",
      showRecoveryModal: false,
    };
  },
  methods: {
    async register() {
      try {
        const response = await axios.post(
          "http://localhost:8020/po_app/Users/Register/",
          {
            username: this.username,
            email: this.email,
            password: this.password,
            address: this.address,
          }
        );

        if (response.status === 201) {
          this.successMsg = `${this.username} account successfully created`;
          this.clearForm();
        }
      } catch (error) {
        this.errorMsg =
          "An error occurred during registration. Please try again.";
        console.error("Error registering user:", error);
      }
    },
    async login() {
      try {
        const response = await axios.post("http://localhost:8020/api/token/", {
          username: this.loginUsername,
          password: this.loginPassword,
        });
        const token = response.data.access;
        this.$store.dispatch("login", { username: this.loginUsername, token });
        const nextRoute = this.$route.query.next || "/Account";
        this.$router.push(nextRoute);
      } catch (error) {
        console.error("Login failed:", error);
        alert("Login failed. Bad username or password");
      }
    },
    clearForm() {
      this.username = "";
      this.email = "";
      this.password = "";
      this.address = "";
    },
  },
};
</script>

<style scoped>
.create-account-container {
  display: flex;
  flex-direction: column;
  /*flex-grow: 1;*/
  justify-content: flex-start;
  align-items: center;
  margin-top: 60px;
  gap: 30px;
}

.account-item {
  background-color: var(--color-background-item);
  border: 1px solid var(--color-light-grey);
  border-radius: var(--default-radius);
  margin: 10px;
  padding: 20px;
  width: 350px;
  min-height: 100px;
  text-align: center;
  font-size: var(--font-size-medium);
}

input {
  border-radius: var(--default-radius);
  border: solid 0px;
  padding: 10px;
  margin-bottom: 20px;
  width: 90%;
}

.button-container {
  display: flex;
  flex-direction: row;
  gap: 50px;
  justify-content: center;
  align-items: center;
}

button {
  height: 40px;
  width: 90px;
  row-gap: 50 px;
  border: 0;
  background-color: var(--color-button);
  border-radius: var(--default-radius);
  font-family: var(--font-family);
  color: var(--color-white);
  cursor: pointer;
}

.error {
  color: var(--color-error-msg);
}
</style>
