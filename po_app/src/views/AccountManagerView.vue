<template>
  <div class="account-container">
    <form @submit.prevent="updateUserAccountInfo" class="account-item">
      <h3 class="title-item">Account informations</h3>
      <div class="input-container">
        <label>Username:</label>
        <input v-model="username" />

        <label>Email:</label>
        <input v-model="email" type="email" />

        <label>Address:</label>
        <input v-model="address" />
      </div>
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
    <div class="account-item">
      <h3>Your prefered activities</h3>
      <div
        v-for="activity in activitiesList"
        :key="activity.activity_id"
        class="checkbox-container"
      >
        <label>
          <input type="checkbox" :value="activity.activity_id" />
          <span
            @mouseover="showActivityDesc(activity)"
            @mouseleave="hideActivityDesc(activity)"
          >
            {{ activity.activity_name }}
          </span>
        </label>
        <p v-if="activity.showDescription" class="description">
          {{ activity.activity_desc }}
        </p>
      </div>
      <div class="button-container">
        <button type="submit">Validate</button>
        <!--button @click="openDeleteAccountModal">Delete Account</button-->
      </div>
    </div>
    <div class="account-item">
      <h3>Your knewn allergens</h3>
      <div
        v-for="allergen in allergensList"
        :key="allergen.allergen_id"
        class="checkbox-container"
      >
        <label>
          <input type="checkbox" :value="allergen.allergen_id" />
          <span
            @mouseover="showAllergenDesc(allergen)"
            @mouseleave="hideAllergenDesc(allergen)"
          >
            {{ allergen.allergen_name }}
          </span>
        </label>
        <p v-if="allergen.showDescription" class="description">
          {{ allergen.allergen_desc }}
        </p>
      </div>
      <div class="button-container">
        <button type="submit">Validate</button>
        <!--button @click="openDeleteAccountModal">Delete Account</button-->
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import DeleteAccountPrompt from "@/components/DeleteAccountPrompt.vue";

export default {
  name: "AccountManagerView",
  components: { DeleteAccountPrompt },
  data() {
    return {
      username: "",
      email: "",
      address: "",
      successMsg: "",
      errorMsg: "",
      showDeleteAccountModal: false,
      activitiesList: [],
      allergensList: [],
    };
  },
  created() {
    this.getUserAccountInfo();
    this.fetchActivitiesList();
    this.fetchAllergensList();
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
    async fetchActivitiesList() {
      try {
        const response = await axios.get(
          "http://localhost:8020/po_app/Activities/",
          {
            headers: {
              Authorization: `Bearer ${this.$store.getters.getAccessToken}`,
            },
          }
        );
        this.activitiesList = response.data;
      } catch (error) {
        console.error("Error fetching activities list:", error);
      }
    },
    async fetchAllergensList() {
      try {
        const response = await axios.get(
          "http://localhost:8020/po_app/Allergens/",
          {
            headers: {
              Authorization: `Bearer ${this.$store.getters.getAccessToken}`,
            },
          }
        );
        this.allergensList = response.data;
      } catch (error) {
        console.error("Error fetching allergens list:", error);
      }
    },
    showActivityDesc(activity) {
      activity.showDescription = true;
    },
    hideActivityDesc(activity) {
      activity.showDescription = false;
    },
    showAllergenDesc(allergen) {
      allergen.showDescription = true;
    },
    hideAllergenDesc(allergen) {
      allergen.showDescription = false;
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
  background-color: var(--color-header-footer);
  border-radius: var(--default-radius);
  font-family: var(--font-family);
  color: var(--color-white);
  cursor: pointer;
}

.checkbox-container {
  display: flex;
  flex-direction: column;
  margin-bottom: 12px;
  margin-left: 40px;
  align-items: flex-start;
  vertical-align: top;
  width: 100%;
}

input[type="checkbox"],
input[type="radio"] {
  display: inline;
  width: auto;
  margin-right: 15px;
}

.description {
  display: inline-block;
  color: var(--color-header-footer);
  padding: 5px;
  border-radius: 4px;
  margin-top: 5px;
  font-size: var(--font-size-small);
  max-width: 300px;
}

.error {
  color: var(--color-error-msg);
}
</style>
