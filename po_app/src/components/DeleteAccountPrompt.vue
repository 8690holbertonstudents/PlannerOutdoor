<template>
  <Teleport to="body">
    <div v-if="show" class="modal">
      <div class="modal-content">
        <p>{{ defaultMsg || errorMsg }}</p>
        <div class="button-container">
          <button v-if="showDeleteButton" @click="handleActionClick">
            {{ buttonMsg }}
          </button>
          <button v-if="showCloseButton" @click="closeModal">Close</button>
          <button v-if="showCancelButton" @click="cancelModal">Cancel</button>
        </div>
      </div>
    </div>
  </Teleport>
</template>

<script>
import axios from "axios";

export default {
  name: "DeleteAccountPrompt",
  props: {
    show: Boolean,
  },
  data() {
    return {
      defaultMsg: "Confirm to delete your account",
      buttonMsg: "Erase account!",
      errorMsg: "",
      showDeleteButton: true,
      showCloseButton: false,
      showCancelButton: true,
      confirmDelete: false,
    };
  },
  methods: {
    cancelModal() {
      this.$emit("close");
    },
    closeModal() {
      this.$emit("close");
      this.resetModal();
    },
    handleActionClick() {
      if (!this.confirmDelete) {
        this.defaultMsg = "Are you sure? This action cannot be undone!";
        this.buttonMsg = "OK";
        this.confirmDelete = true;
      } else {
        this.deleteUserAccount();
      }
    },
    async deleteUserAccount() {
      try {
        await axios.delete(
          "http://localhost:8020/po_app/Users/DeleteAccount/",
          {
            headers: {
              Authorization: `Bearer ${this.$store.getters.getAccessToken}`,
            },
          }
        );
        this.defaultMsg = "Account deleted successfully.";
        this.showDeleteButton = false;
        this.showCancelButton = false;
        this.showCloseButton = true;
        this.$store.commit("clearUserData");
        this.$router.push("/").then(() => window.location.reload());
      } catch (error) {
        this.errorMsg = "Error appeared while deleting your account";
        this.defaultMsg = "";
        this.showDeleteButton = false;
        this.showCancelButton = false;
        this.showCloseButton = true;
      }
    },
    resetModal() {
      this.defaultMsg = "Confirm to delete your account";
      this.errorMsg = "";
      this.buttonMsg = "Erase account!";
      this.showDeleteButton = true;
      this.showCloseButton = false;
      this.showCancelButton = true;
      this.confirmDelete = false;
    },
  },
  watch: {
    show(newValue) {
      if (newValue) this.resetModal();
    },
  },
};
</script>

<style scoped>
.modal {
  position: fixed;
  inset: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: var(--font-family);
  font-size: var(--font-size-medium);
  background-color: var(--color-background-modal);
}

.modal-content {
  box-shadow: 8px 8px 3px 0px var(--color-dark-grey);
  border-radius: var(--default-radius);
  background: var(--color-light-grey);
  padding: 30px;
  text-align: center;
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
</style>
