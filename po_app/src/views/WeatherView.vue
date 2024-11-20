<template>
  <div class="main-container">
    <div class="main-item">
      <h2 v-if="success">Weather at {{ city }}</h2>
      <h3 v-else>No weather data or bad city name</h3>
    </div>
    <div v-show="success" class="weather-container">
      <div
        v-for="(item, index) in forecast.list"
        :key="index"
        class="weather-item"
      >
        <p>
          <ConvertToDate :timestamp="item.dt" />
        </p>
        <p>
          <ConvertToDay :timestamp="item.dt" />
        </p>
        <p>
          <ConvertToCelcius :tempK="item.temp.day" /> °C /
          <ConvertToFahrenheit :tempK="item.temp.day" /> °F
        </p>
        <img
          v-if="item.weather[0].icon"
          :src="`http://openweathermap.org/img/wn/${item.weather[0].icon}@2x.png`"
          :alt="item.weather[0].description"
        />
        <p><button @click="goToDetails(item)">Details</button></p>
      </div>
    </div>
    <LoginPrompt
      v-if="showModal"
      :show="showModal"
      @close="showModal = false"
    />
  </div>
</template>

<script>
import axios from "axios";
import LoginPrompt from "@/components/LoginPrompt.vue";
import ConvertToDate from "@/components/ConvertToDate.vue";
import ConvertToDay from "@/components/ConvertToDay.vue";
import ConvertToCelcius from "@/components/ConvertToCelcius.vue";
import ConvertToFahrenheit from "@/components/ConvertToFahrenheit.vue";

export default {
  name: "WeatherView",
  components: {
    LoginPrompt,
    ConvertToDate,
    ConvertToDay,
    ConvertToCelcius,
    ConvertToFahrenheit,
  },
  data() {
    return {
      city: {},
      forecast: {},
      success: false,
      showModal: false,
    };
  },
  created() {
    this.fetchWeatherData();
  },
  watch: {
    "$route.query.lat": "fetchWeatherData",
    "$route.query.lon": "fetchWeatherData",
  },
  computed: {
    userLoggedIn() {
      return this.$store.getters.isLoggedIn;
    },
  },
  methods: {
    async fetchWeatherData() {
      try {
        const lat = this.$route.query.lat;
        const lon = this.$route.query.lon;
        this.success = false;
        const response = await axios.get(
          `http://localhost:8020/po_app/Weather/?lat=${lat}&lon=${lon}`
        );
        const cityData = response.data.data.city;
        this.city = `${cityData.name}, ${cityData.country}`;
        this.forecast = response.data.data;
        this.success = true;
      } catch (error) {
        console.error("Request error:", error);
        this.success = false;
      }
    },
    goToDetails(item) {
      if (this.userLoggedIn) {
        this.$router.push({
          name: "WeatherDetails",
          params: {
            itemCity: this.city,
            itemDt: item.dt,
          },
          query: {
            lat: this.$route.query.lat,
            lon: this.$route.query.lon,
          },
        });
      } else {
        this.showModal = true;
      }
    },
  },
};
</script>

<style scoped>
.main-container {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  flex-basis: 100vh;
  margin-top: var(--margin-header-footer);
}

.main-item {
  background-color: var(--color-background-item);
  border: 1px solid var(--color-light-grey);
  border-radius: var(--default-radius);
  margin: 10px;
  padding: 20px;
  align-self: center;
  text-align: center;
  flex-grow: 1;
}

.weather-container {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: center;
  align-items: flex-start;
  gap: 20px;
  flex-grow: 19;
  margin-bottom: var(--margin-header-footer);
  padding-bottom: 20px;
}

.weather-item {
  background-color: var(--color-background-item);
  border: 1px solid var(--color-light-grey);
  border-radius: var(--default-radius);
  margin: 10px;
  padding: 20px;
  min-width: 200px;
  max-height: 330px;
  text-align: center;
  font-size: var(--font-size-medium);
}

button {
  height: 30px;
  width: 80px;
  background-color: var(--color-button);
  border: 0;
  border-radius: var(--default-radius);
  font-family: var(--font-family);
  color: var(--color-white);
  cursor: pointer;
}
</style>
