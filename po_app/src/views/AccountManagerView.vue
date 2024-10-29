<template>
  <div class="account-container">
    <form @submit.prevent="updateUserAccountInfo" class="account-item">
      <h3 class="title-item">Account informations</h3>
      <label>Username:</label>
      <input v-model="username" />

      <label>Email:</label>
      <input v-model="email" type="email" />

      <label>Address:</label>
      <input v-model="address" />
      <p v-if="successMsg">{{ successMsg }}</p>
      <p v-if="errorMsg" class="error">{{ errorMsg }}</p>
      <div class="button-container">
        <button type="submit">Update Account</button>
        <button @click="openDeleteAccountModal">Delete Account</button>
      </div>
      <DeleteAccountPrompt
        v-if="showDeleteAccountModal"
        :show="showDeleteAccountModal"
        @close="showDeleteAccountModal = false"
      />
    </form>
  </div>
</template>

<script>
import axios from "axios";
import DeleteAccountPrompt from "@/components/DeleteAccountPrompt.vue";

export default {
  components: { DeleteAccountPrompt },
  data() {
    return {
      username: "",
      email: "",
      address: "",
      successMsg: "",
      errorMsg: "",
      showDeleteAccountModal: false,
    };
  },
  async created() {
    await this.getUserAccountInfo();
  },
  methods: {
    openDeleteAccountModal() {
      this.errorMsg = "";
      this.successMsg = "";
      this.showDeleteAccountModal = true;
    },
    async getUserAccountInfo() {
      try {
        const response = await axios.get(
          "http://localhost:8020/po_app/Users/Account/",
          {
            headers: {
              Authorization: `Bearer ${this.$store.getters.getAccessToken}`,
            },
          }
        );
        this.username = response.data.username;
        this.email = response.data.email;
        this.address = response.data.address;
      } catch (error) {
        this.errorMsg = "Failed to load account information";
      }
    },
    async updateUserAccountInfo() {
      try {
        await axios.put(
          "http://localhost:8020/po_app/Users/Account/",
          {
            username: this.username,
            email: this.email,
            address: this.address,
          },
          {
            headers: {
              Authorization: `Bearer ${this.$store.getters.getAccessToken}`,
            },
          }
        );
        this.errorMsg = "";
        this.successMsg = "Account information updated successfully!";
      } catch (error) {
        this.successMsg = "";
        if (!this.showDeleteAccountModal) {
          this.errorMsg = "Error appear while updating your information";
        } else {
          this.errorMsg = "";
        }
      }
    },
  },
};
</script>

<style scoped>
.account-container {
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
  cursor: pointer;
}

.error {
  color: var(--color-error-msg);
}
</style>
