<template>
  <div id="locate-form">
    <input
      type="text"
      v-model="city"
      placeholder="Enter a city name..."
      @input="fetchSelections"
    />
    <ul v-if="selections.length">
      <li
        v-for="(selection, index) in selections"
        :key="index"
        @click="selectCity(selection)"
      >
        {{ selection.name ? selection.name : "Unknown" }},
        {{ selection.country ? selection.country : "Unknown" }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LocateView",
  data() {
    return {
      city: "",
      selections: [],
    };
  },
  methods: {
    async fetchSelections() {
      if (this.city.length > 3) {
        try {
          const response = await axios.get(
            `http://localhost:8020/po_app/Geocode/?location=${this.city}`
          );
          this.selections = response.data.data || [];
        } catch (error) {
          console.error("Error fetching city selections:", error);
          this.selections = [];
        }
      } else {
        this.selections = [];
      }
    },
    selectCity(selection) {
      if (selection && selection.name && selection.country) {
        this.city = `${selection.name}, ${selection.country}`;
        this.selections = [];
        this.$router.push({
          name: "Weather",
          query: {
            lat: selection.lat,
            lon: selection.lon,
          },
        });
        this.city = "";
      } else {
        console.error("Invalid selection object:", selection);
      }
    },
  },
};
</script>

<style scoped>
#locate-form {
  position: relative;
}
input {
  height: 15px;
  width: 200px;
  padding: 8px;
  border-radius: var(--default-radius);
  border: 1px solid var(--color-white);
  font-size: var(--font-size-small);
}
ul {
  list-style: none;
  padding: 0;
  margin: 0;
  border: 2px solid var(--color-medium-grey);
  border-radius: var(--default-radius);
  background: var(--color-white);
  position: absolute;
  width: 100%;
  max-height: 200px;
  overflow-y: auto;
}

li {
  color: var(--color-black);
  font-size: var(--font-size-small);
  padding: 8px;
  cursor: pointer;
}

li:hover {
  background-color: var(--color-light-grey);
}
</style>
