<template>
  <div class="create-account-container">
    <form @submit.prevent="register" class="account-item">
      <h3>Create an Account</h3>
      <input type="text" v-model="username" placeholder="Username" required />
      <input type="email" v-model="email" placeholder="Email" required />
      <input
        type="password"
        v-model="password"
        placeholder="Password"
        required
      />
      <input
        type="address"
        v-model="address"
        placeholder="Enter your home address"
        required
      />
      <button type="submit">Register</button>
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
        <button @click="recoverPassword">Forgot Password?</button>
      </div>
    </form>
  </div>
</template>

<script>
//import axios from "axios";

export default {
  name: "CreateAccountView",
  data() {
    return {
      username: "",
      email: "",
      password: "",
      address: "",
      loginUsername: "",
      loginPassword: "",
    };
  },
  methods: {
    register() {},
    login() {},
    recoverPassword() {},
  },
};
</script>

<style scoped>
.create-account-container {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  justify-content: flex-start;
  align-items: center;
  margin-top: 20px;
  gap: 30px;
}

.account-item {
  background-color: var(--color-white);
  box-shadow: var(--header-footer-shadow);
  border: 2px solid var(--color-light-grey);
  border-radius: var(--header-footer-border);
  margin: 10px;
  padding: 20px;
  width: 350px;
  min-height: 100px;
  text-align: center;
  font-size: var(--font-size-medium);
}

input {
  padding: 10px;
  margin-bottom: 10px;
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
  background-color: var(--color-header-footer);
  border-radius: var(--header-footer-border);
  font-family: var(--font-family);
  color: var(--color-white);
}
</style>
