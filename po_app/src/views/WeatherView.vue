<template>
  <main class="main-container">
    <section>
      <h2 v-if="success">Weather at {{ city.name }}</h2>
      <h3 v-else>No weather data or bad city name</h3>
    </section>
    <section v-show="success" class="weather-container">
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
          <ConvertToTemp :tempK="item.temp.day" unit="C" /> /
          <ConvertToTemp :tempK="item.temp.day" unit="F" />
        </p>
        <img
          v-if="item.weather[0].icon"
          :src="`http://openweathermap.org/img/wn/${item.weather[0].icon}@2x.png`"
          :alt="item.weather[0].description"
        />
        <p><button @click="goToDetails(item)">Details</button></p>
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
import ConvertToDate from "@/components/ConvertToDate.vue";
import ConvertToDay from "@/components/ConvertToDay.vue";
import ConvertToTemp from "@/components/ConvertToTemp.vue";

export default {
  components: { LoginPrompt, ConvertToDate, ConvertToDay, ConvertToTemp },
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
    "$route.query.city": "fetchWeatherData",
  },
  computed: {
    userLoggedIn() {
      return this.$store.getters.isLoggedIn;
    },
  },
  methods: {
    async fetchWeatherData() {
      try {
        const city = this.$route.query.city;
        this.success = false;
        const openWeatherMapApiResponse = await axios.get(
          `http://localhost:8020/po_app/Weather/?city=${city}`
        );
        this.city = openWeatherMapApiResponse.data.city;
        this.forecast = openWeatherMapApiResponse.data;
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
            itemCity: this.city.name,
            itemDt: item.dt,
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
  margin: 0% 1.5% 0% 1%;
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
  cursor: pointer;
}
</style>
