<template>
  <div class="account-item">
    <h3>Your known allergens</h3>
    <div v-if="!errorAllergensMsg">
      <div
        v-for="allergen in allergensList"
        :key="allergen.allergen_id"
        class="checkbox-container"
      >
        <label>
          <input
            type="checkbox"
            :value="allergen.allergen_id"
            v-model="allergen.isChecked"
          />
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
      <p v-if="successUpdateAllergensMsg" class="success">
        {{ successUpdateAllergensMsg }}
      </p>
      <p v-else class="error">
        {{ errorUpdateAllergensMsg }}
      </p>
      <div class="button-container">
        <button v-if="!isValidate" @click="updateSelectedAllergens">
          {{ buttonText }}
        </button>
        <button v-else @click="clearMessages">{{ buttonText }}</button>
      </div>
    </div>
    <div v-else>
      <p class="error">{{ errorAllergensMsg }}</p>
      <div class="button-container">
        <button @click="clearMessages">Ok</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "FetcAllergens",
  props: {
    userIdUrl: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      errorAllergensMsg: "",
      successUpdateAllergensMsg: "",
      errorUpdateAllergensMsg: "",
      fetchError: false,
      buttonText: "Validate",
      isValidate: false,
      allergensList: [],
      selectedAllergens: [],
    };
  },
  mounted() {
    this.fetchSelectedAllergens();
  },
  methods: {
    async fetchSelectedAllergens() {
      try {
        const response = await axios.get(
          "http://localhost:8020/po_app/UserAllergens/GetUserAllergens",
          {
            headers: {
              Authorization: `Bearer ${this.$store.getters.getAccessToken}`,
            },
          }
        );
        this.selectedAllergens = response.data.data.map((item) => ({
          user_allergen_id: item.user_allergen_id,
          allergen_id: item.allergen_id,
        }));
        this.fetchAllergensList();
      } catch (error) {
        this.errorAllergensMsg =
          error.response?.data?.error || "An unexpected error occurred";
        console.error("Error:", error);
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
        this.allergensList = response.data.map((allergen) => {
          const isSelected = this.selectedAllergens.find(
            (selected) => selected.allergen_id === allergen.url
          );
          return {
            ...allergen,
            isChecked: !!isSelected,
            userAllergenId: isSelected ? isSelected.user_allergen_id : null,
          };
        });
      } catch (error) {
        this.errorAllergensMsg =
          error.response?.error || "An unexpected error occurred";
        console.error("Error:", error);
      }
    },
    async updateSelectedAllergens() {
      for (const allergen of this.allergensList) {
        const isChecked = allergen.isChecked;
        const selectedAllergen = this.selectedAllergens.find(
          (selected) => selected.allergen_id === allergen.url
        );
        const isAlreadySelected = !!selectedAllergen;
        if (isChecked && isAlreadySelected) {
          continue;
        }
        if (!isChecked && isAlreadySelected) {
          try {
            await axios.delete(
              `http://localhost:8020/po_app/UserAllergens/DeleteUserAllergens/${selectedAllergen.user_allergen_id}/`
            );
            continue;
          } catch (error) {
            this.fetchError = true;
            this.errorUpdateAllergensMsg =
              error.response?.error || "An unexpected error occurred";
            console.error("Error:", error);
          }
        }
        if (isChecked && !isAlreadySelected) {
          try {
            await axios.post(
              "http://localhost:8020/po_app/UserAllergens/PostUserAllergens/",
              {
                user_id: this.userIdUrl,
                allergen_id: allergen.url,
              }
            );
          } catch (error) {
            this.fetchError = true;
            let errorsSerializer = "";
            if (error.response?.data?.errors) {
              errorsSerializer = Object.values(error.response.data.errors)
                .flat()
                .join("\n");
            }
            this.errorUpdateAllergensMsg =
              errorsSerializer ||
              error.response?.data?.error ||
              "An unexpected error occurred";
            console.error("Error:", error);
          }
        }
      }
      if (!this.fetchError) {
        this.successUpdateAllergensMsg = "Allergens validation is sucessfull";
      }
      this.isValidate = true;
      this.buttonText = "Ok";
      await this.fetchSelectedAllergens();
    },
    showAllergenDesc(allergen) {
      allergen.showDescription = true;
    },
    hideAllergenDesc(allergen) {
      allergen.showDescription = false;
    },
    clearMessages() {
      this.successUpdateAllergensMsg = "";
      this.errorUpdateAllergensMsg = "";
      this.errorAllergensMsg = "";
      this.isValidate = false;
      this.buttonText = "Validate";
    },
  },
};
</script>

<style scoped>
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
  color: var(--color-dark-grey);
  padding: 5px;
  border-radius: 4px;
  margin-top: 5px;
  font-size: var(--font-size-small);
  max-width: 300px;
}

.success {
  color: var(--color-success-msg);
}

.error {
  color: var(--color-error-msg);
}
</style>
