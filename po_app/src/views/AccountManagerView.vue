<template>
  <div class="account-container">
    <form @submit.prevent="updateUserAccountInfo" class="account-item">
      <h3 class="title-item">Account informations</h3>
      <div class="input-container">
        <label>Username:</label>
        <input v-model="username" @focus="clearMessages" />

        <label>Email:</label>
        <input v-model="email" type="email" @focus="clearMessages" />

        <label>Address:</label>
        <input v-model="address" @focus="clearMessages" />
      </div>
      <p v-if="successAccountMsg" class="success">{{ successAccountMsg }}</p>
      <p v-if="errorAccountMsg" class="error">{{ errorAccountMsg }}</p>
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
    <FetchActivities :userIdUrl="userIdUrl" />
    <FetchAllergens :userIdUrl="userIdUrl" />
  </div>
</template>

<script>
import axios from "axios";
import DeleteAccountPrompt from "@/components/DeleteAccountPrompt.vue";
import FetchActivities from "@/components/FetchActivities.vue";
import FetchAllergens from "@/components/FetchAllergens.vue";

export default {
  name: "AccountManagerView",
  components: { DeleteAccountPrompt, FetchActivities, FetchAllergens },
  data() {
    return {
      username: "",
      email: "",
      address: "",
      successAccountMsg: "",
      errorAccountMsg: "",
      showDeleteAccountModal: false,
    };
  },
  created() {
    this.getUserAccountInfo();
  },
  methods: {
    openDeleteAccountModal() {
      this.errorAccountMsg = "";
      this.successAccountMsg = "";
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
        this.userIdUrl = response.data.data.url;
        this.userId = response.data.data.id;
        this.username = response.data.data.username;
        this.email = response.data.data.email;
        this.address = response.data.data.address;
        this.currentUsername = this.username;
        this.currentEmail = this.email;
        this.currentAddress = this.address;
        this.errorAccountMsg = "";
      } catch (error) {
        this.errorAccountMsg =
          error.response?.data?.error || "An unexpected error occurred";
      }
    },
    async updateUserAccountInfo() {
      try {
        const dataToUpdate = {};
        if (this.username !== this.currentUsername)
          dataToUpdate.username = this.username;
        if (this.email !== this.currentEmail) dataToUpdate.email = this.email;
        if (this.address !== this.currentAddress)
          dataToUpdate.address = this.address;
        const response = await axios.patch(
          "http://localhost:8020/po_app/Users/Account/",
          dataToUpdate,
          {
            headers: {
              Authorization: `Bearer ${this.$store.getters.getAccessToken}`,
            },
          }
        );
        this.errorAccountMsg = "";
        this.successAccountMsg = response.data.message;
        this.$store.commit("setUsername", response.data.data.username);
        this.currentUsername = response.data.data.username;
        this.currentEmail = response.data.data.email;
        this.currentAddress = response.data.data.address;
      } catch (error) {
        this.successAccountMsg = "";
        let errorsSerializer = "";
        if (!this.showDeleteAccountModal) {
          if (error.response?.data?.errors) {
            errorsSerializer = Object.values(error.response.data.errors)
              .flat()
              .join("\n");
          }
          this.errorAccountMsg =
            errorsSerializer ||
            error.response?.data?.error ||
            "An unexpected error occurred";
        } else {
          this.errorAccountMsg = "";
        }
      }
    },
    showAllergenDesc(allergen) {
      allergen.showDescription = true;
    },
    hideAllergenDesc(allergen) {
      allergen.showDescription = false;
    },
    clearMessages() {
      this.successAccountMsg = "";
      this.errorAccountMsg = "";
    },
  },
};
</script>

<style scoped>
.account-container {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  overflow-y: auto;
  justify-content: center;
  align-items: flex-start;
  margin-top: var(--margin-header-footer);
  margin-bottom: var(--margin-header-footer);
  gap: 25px;
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

.input-container {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.input-container > label {
  padding-left: 0.6em;
  margin-bottom: 0.6em;
  font-size: var(--font-size-medium);
}

input {
  border-radius: var(--default-radius);
  border: solid 0px;
  padding: 10px;
  margin-bottom: 10px;
  width: 90%;
}

label {
  text-align: left;
}

.button-container {
  display: flex;
  flex-direction: row;
  padding-top: 1em;
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

.success {
  color: var(--color-success-msg);
}

.error {
  color: var(--color-error-msg);
}
</style>
