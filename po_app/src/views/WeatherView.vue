<template>
  <main class="main-container">
    <section>
      <h2 v-if="loading">Weather at {{ city.name }}</h2>
      <h3 v-else>No weather data or bad city name</h3>
    </section>
    <section v-show="loading" class="weather-container">
      <div
        v-for="(item, index) in forecast.list"
        :key="index"
        class="weather-item"
      >
        <p>{{ formatMonthYear(item.dt) }}</p>
        <p>{{ formatDay(item.dt) }}</p>
        <p>
          {{ convertTemp(item.temp.day) }}°C /
          {{ convertToFahrenheit(item.temp.day) }}°F
        </p>
        <img
          v-if="item.weather[0].icon"
          :src="`http://openweathermap.org/img/wn/${item.weather[0].icon}@2x.png`"
          :alt="item.weather[0].description"
        />
        <p><button @click="handleDetailsClick">Details</button></p>
      </div>
    </section>
    <LoginPrompt
      v-if="showModal"
      :show="showModal"
      @close="showModal = false"
    />
  </main>
</template>

<script>
import axios from "axios";
import LoginPrompt from "@/components/LoginPrompt.vue";

export default {
  components: { LoginPrompt },
  data() {
    return {
      city: {},
      forecast: {},
      loading: true,
      showModal: false,
      userLoggedIn: false,
    };
  },
  created() {
    this.fetchWeatherData();
  },
  watch: {
    "$route.query.city": "fetchWeatherData",
  },
  methods: {
    fetchWeatherData() {
      const city = this.$route.query.city;
      this.loading = true;

      axios
        .get(`http://localhost:8020/po_app/Weather/?city=${city}`)
        .then((response) => {
          this.city = response.data.city;
          this.forecast = response.data;
          this.loading = true;
        })
        .catch((error) => {
          console.error("Request error:", error);
          this.loading = false;
        });
    },
    formatMonthYear(timestamp) {
      const date = new Date(timestamp * 1000);
      const month = date
        .toLocaleString("en-EN", { month: "long" })
        .toUpperCase();
      const year = date.getFullYear();
      return `${month} ${year}`;
    },
    formatDay(timestamp) {
      const date = new Date(timestamp * 1000);
      const dayOfWeek = date
        .toLocaleDateString("en-EN", { weekday: "long" })
        .toUpperCase();
      const dayOfMonth = date.getDate();
      return `${dayOfWeek} ${dayOfMonth}`;
    },
    convertTemp(tempK) {
      const tempCelcius = (tempK - 273.15).toFixed(1);
      return `${tempCelcius}`;
    },
    convertToFahrenheit(tempK) {
      const tempFahrenheit = (((tempK - 273.15) * 9) / 5 + 32).toFixed(1);
      return `${tempFahrenheit}`;
    },
    handleDetailsClick() {
      if (this.userLoggedIn) {
        // Placeholder pour rediriger vers les détails de la météo.
        console.log("Redirection vers les détails météo...");
      } else {
        // Affiche le modal si l'utilisateur n'est pas connecté.
        this.showModal = true;
      }
    },
  },
};
</script>

<style scoped>
body {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.main-container {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  flex-grow: 1;
}

.weather-container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
  margin: 0% 1% 1% 1%;
}

.weather-item {
  background-color: var(--color-white);
  box-shadow: var(--header-footer-shadow);
  border: 2px solid var(--color-light-grey);
  border-radius: var(--header-footer-border);
  margin: 10px;
  padding: 20px;
  min-width: 200px;
  min-height: 100px;
  text-align: center;
  font-size: var(--font-size-medium);
}

button {
  height: 30px;
  width: 80px;
  background-color: var(--color-header-footer);
  border: 0;
  border-radius: var(--header-footer-border);
  font-family: var(--font-family);
  color: var(--color-white);
}
</style>
