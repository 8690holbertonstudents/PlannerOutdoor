<template>
  <div class="account-item">
    <h3>Your prefered activities</h3>
    <div v-if="!errorActivitiesMsg">
      <div
        v-for="activity in activitiesList"
        :key="activity.activity_id"
        class="checkbox-container"
      >
        <label>
          <input
            type="checkbox"
            :value="activity.activity_id"
            v-model="activity.isChecked"
          />
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
      <p v-if="successUpdateActivitiesMsg" class="success">
        {{ successUpdateActivitiesMsg }}
      </p>
      <p v-else class="error">
        {{ errorUpdateActivitiesMsg }}
      </p>
      <div class="button-container">
        <button v-if="!isValidate" @click="updateSelectedActivities">
          {{ buttonText }}
        </button>
        <button v-else @click="clearMessages">{{ buttonText }}</button>
      </div>
    </div>
    <div v-else>
      <p class="error">{{ errorActivitiesMsg }}</p>
      <div class="button-container">
        <button @click="clearMessages">Ok</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "FetcActivities",
  props: {
    userIdUrl: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      errorActivitiesMsg: "",
      successUpdateActivitiesMsg: "",
      errorUpdateActivitiesMsg: "",
      fetchError: false,
      buttonText: "Validate",
      isValidate: false,
      activitiesList: [],
      selectedActivities: [],
    };
  },
  mounted() {
    this.fetchSelectedActivities();
  },
  methods: {
    async fetchSelectedActivities() {
      try {
        const response = await axios.get(
          "http://localhost:8020/po_app/UserActivities/GetUserActivities",
          {
            headers: {
              Authorization: `Bearer ${this.$store.getters.getAccessToken}`,
            },
          }
        );
        this.selectedActivities = response.data.data.map((item) => ({
          user_activity_id: item.user_activity_id,
          activity_id: item.activity_id,
        }));
        this.fetchActivitiesList();
      } catch (error) {
        this.errorActivitiesMsg =
          error.response?.data?.error || "An unexpected error occurred";
        console.error("Error:", error);
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
        this.activitiesList = response.data.map((activity) => {
          const isSelected = this.selectedActivities.find(
            (selected) => selected.activity_id === activity.url
          );
          return {
            ...activity,
            isChecked: !!isSelected,
            userActivityId: isSelected ? isSelected.user_activity_id : null,
          };
        });
      } catch (error) {
        this.errorActivitiesMsg =
          error.response?.error || "An unexpected error occurred";
        console.error("Error:", error);
      }
    },
    async updateSelectedActivities() {
      for (const activity of this.activitiesList) {
        const isChecked = activity.isChecked;
        const selectedActivity = this.selectedActivities.find(
          (selected) => selected.activity_id === activity.url
        );
        const isAlreadySelected = !!selectedActivity;
        if (isChecked && isAlreadySelected) {
          continue;
        }
        if (!isChecked && isAlreadySelected) {
          try {
            await axios.delete(
              `http://localhost:8020/po_app/UserActivities/DeleteUserActivities/${selectedActivity.user_activity_id}/`
            );
            continue;
          } catch (error) {
            this.fetchError = true;
            this.errorUpdateActivitiesMsg =
              error.response?.error || "An unexpected error occurred";
            console.error("Error:", error);
          }
        }
        if (isChecked && !isAlreadySelected) {
          try {
            await axios.post(
              "http://localhost:8020/po_app/UserActivities/PostUserActivities/",
              {
                user_id: this.userIdUrl,
                activity_id: activity.url,
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
            this.errorUpdateActivitiesMsg =
              errorsSerializer ||
              error.response?.data?.error ||
              "An unexpected error occurred";
            console.error("Error:", error);
          }
        }
      }
      if (!this.fetchError) {
        this.successUpdateActivitiesMsg = "Activities validation is sucessfull";
      }
      this.isValidate = true;
      this.buttonText = "Ok";
      await this.fetchSelectedActivities();
    },
    showActivityDesc(activity) {
      activity.showDescription = true;
    },
    hideActivityDesc(activity) {
      activity.showDescription = false;
    },
    clearMessages() {
      this.successUpdateActivitiesMsg = "";
      this.errorUpdateActivitiesMsg = "";
      this.errorActivitiesMsg = "";
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
