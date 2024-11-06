<template>
  <Teleport to="body">
    <div v-if="show" class="modal-container">
      <form @submit.prevent="recoveryPassword" class="modal-item">
        <input v-model="recoveryUsername" placeholder="Enter your username" />
        <input
          v-model="recoveryEmail"
          type="email"
          placeholder="Enter your email"
        />
        <input
          v-model="newPassword"
          type="password"
          placeholder="Enter new password"
        />
        <p v-if="recoveryMsg">{{ recoveryMsg }}</p>
        <p v-if="errorMsg" class="error">{{ errorMsg }}</p>
        <div class="button-container">
          <button v-show="!recoverySuccess" type="submit">
            Recover Password
          </button>
          <button @click="closeModal">Close</button>
        </div>
      </form>
    </div>
  </Teleport>
</template>

<script>
import axios from "axios";

export default {
  name: "RecoveryPrompt",
  props: {
    show: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      recoveryUsername: "",
      recoveryEmail: "",
      newPassword: "",
      recoveryMsg: "",
      errorMsg: "",
      recoverySuccess: false,
    };
  },
  methods: {
    async recoveryPassword() {
      try {
        const recoveryResponse = await axios.post(
          "http://localhost:8020/po_app/Users/RecoverPassword/",
          {
            username: this.recoveryUsername,
            email: this.recoveryEmail,
            newPassword: this.newPassword,
          }
        );

        if (recoveryResponse.status === 200) {
          this.recoveryMsg =
            "Password has been reset successfully. You can login again";
          this.clearForm();
          this.recoverySuccess = true;
          this.$forceUpdate();
        } else {
          this.errorMsg = "Bad couple username & password";
        }
      } catch (error) {
        this.errorMsg = "An error occurred. Please try again";
      }
    },
    clearForm() {
      this.recoveryUsername = "";
      this.recoveryEmail = "";
      this.newPassword = "";
    },
    closeModal() {
      this.$emit("close");
      this.recoverySuccess = false;
    },
  },
};
</script>

<style scoped>
.modal-container {
  position: fixed;
  inset: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: var(--font-family);
  font-size: var(--font-size-medium);
  background-color: var(--color-background-modal);
}

.modal-item {
  box-shadow: 8px 8px 3px 0px var(--color-dark-grey);
  border-radius: var(--default-radius);
  background: var(--color-light-grey);
  margin: 10px;
  padding: 20px;
  width: 400px;
  text-align: center;
}

input {
  padding: 10px;
  margin-bottom: 20px;
  width: 85%;
  border-radius: var(--default-radius);
  border: 1px solid var(--color-white);
  font-size: var(--font-size-small);
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
  border-radius: var(--default-radius);
  font-family: var(--font-family);
  color: var(--color-white);
  cursor: pointer;
}

.error {
  color: var(--color-error-msg);
}
</style>
