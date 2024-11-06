<template>
  <Teleport to="body">
    <div v-if="show" class="modal">
      <div class="modal-content">
        <p>Are you sure you want to logout ?</p>
        <div class="button-container">
          <button @click="goToLogOut">Logout</button>
          <button @click="cancelModal">Cancel</button>
        </div>
      </div>
    </div>
  </Teleport>
</template>

<script>
export default {
  name: "LogoutPrompt",
  props: {
    show: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    cancelModal() {
      this.$emit("close");
    },
    goToLogOut() {
      document.cookie =
        "po_app_access_token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; secure;";
      this.$store.commit("logout");
      this.$emit("close");
      this.$router.push({ path: "/" });
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
  height: 30px;
  width: 80px;
  row-gap: 50 px;
  border: 0;
  background-color: var(--color-header-footer);
  border-radius: var(--default-radius);
  font-family: var(--font-family);
  color: var(--color-white);
  cursor: pointer;
}
</style>
