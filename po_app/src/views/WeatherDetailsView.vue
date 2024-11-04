<template>
  <main class="weather-details-container">
    <section>
      <h2>
        Weather at {{ itemCity }} - <ConvertToDate :timestamp="itemDt" /> -
        <ConvertToDay :timestamp="itemDt" />
      </h2>
    </section>
    <section v-if="forecastDayData" class="details-container">
      <div class="details-item">
        <h4>Weather</h4>
        <p>Sky:</p>
        <p>{{ forecastDayData.weather[0].description }}</p>
        <p>Clouds:</p>
        <p>{{ forecastDayData.clouds }}%</p>
        <p>Pressure:</p>
        <p>{{ forecastDayData.pressure }} hpa</p>
        <p>Humidity:</p>
        <p>{{ forecastDayData.humidity }}%</p>
        <p>Precipitation Chance:</p>
        <p>{{ (forecastDayData.pop * 100).toFixed(0) }}%</p>
        <p>Volume Precipitation:</p>
        <p>{{ forecastDayData.rain ? forecastDayData.rain : 0 }} mm</p>
        <p>Sunrise at <ConvertToTime :timestamp="forecastDayData.sunrise" /></p>
        <p>Sunset at <ConvertToTime :timestamp="forecastDayData.sunset" /></p>
      </div>
      <div class="details-item">
        <h4>Real temperature</h4>
        <p>Morning:</p>
        <p>
          <ConvertToTemp :tempK="forecastDayData.temp.morn" unit="C" /> /
          <ConvertToTemp :tempK="forecastDayData.temp.day" unit="F" />
        </p>
        <p>Day:</p>
        <p>
          <ConvertToTemp :tempK="forecastDayData.temp.day" unit="C" /> /
          <ConvertToTemp :tempK="forecastDayData.temp.day" unit="F" />
        </p>
        <p>Evening:</p>
        <p>
          <ConvertToTemp :tempK="forecastDayData.temp.eve" unit="C" /> /
          <ConvertToTemp :tempK="forecastDayData.temp.day" unit="F" />
        </p>
        <p>Night:</p>
        <p>
          <ConvertToTemp :tempK="forecastDayData.temp.night" unit="C" /> /
          <ConvertToTemp :tempK="forecastDayData.temp.day" unit="F" />
        </p>
        <h4>"Feels like" temperature</h4>
        <p>Morning:</p>
        <p>
          <ConvertToTemp :tempK="forecastDayData.feels_like.morn" unit="C" /> /
          <ConvertToTemp :tempK="forecastDayData.feels_like.day" unit="F" />
        </p>
        <p>Day:</p>
        <p>
          <ConvertToTemp :tempK="forecastDayData.feels_like.day" unit="C" /> /
          <ConvertToTemp :tempK="forecastDayData.feels_like.day" unit="F" />
        </p>
        <p>Evening:</p>
        <p>
          <ConvertToTemp :tempK="forecastDayData.temp.eve" unit="C" /> /
          <ConvertToTemp :tempK="forecastDayData.temp.day" unit="F" />
        </p>
        <p>Night:</p>
        <p>
          <ConvertToTemp :tempK="forecastDayData.temp.night" unit="C" /> /
          <ConvertToTemp :tempK="forecastDayData.temp.day" unit="F" />
        </p>
      </div>
      <div class="details-item">
        <h4>Wind</h4>
        <p>Speed:</p>
        <p>{{ forecastDayData.speed }} m/s</p>
        <p>{{ (forecastDayData.speed * 3.6).toFixed(1) }} km/h</p>
        <p>Gusts:</p>
        <p>{{ forecastDayData.gust }} m/s</p>
        <p>{{ (forecastDayData.gust * 3.6).toFixed(1) }} km/h</p>
        <p>Direction:</p>
        <p>
          <ConvertWindDirection :degrees="forecastDayData.deg" />
        </p>
      </div>
      <div v-if="pollutionDayData" class="details-item">
        <h4>Air Pollution</h4>
        <p>
          <AirPollutionAverage :components="pollutionDayData.components" />
        </p>
      </div>
      <div v-else class="details-item">
        <h4>Air Pollution</h4>
        <p>No data for selected day</p>
      </div>
    </section>
    <section v-else>
      <p>No data available for the selected date.</p>
    </section>
  </main>
</template>

<script>
import axios from "axios";
import ConvertToDate from "@/components/ConvertToDate.vue";
import ConvertToDay from "@/components/ConvertToDay.vue";
import ConvertToTemp from "@/components/ConvertToTemp.vue";
import ConvertToTime from "@/components/ConverToTime.vue";
import ConvertWindDirection from "@/components/ConvertWindDirection.vue";
import AirPollutionAverage from "@/components/AirPollutionAverage.vue";

export default {
  components: {
    ConvertToDate,
    ConvertToDay,
    ConvertToTemp,
    ConvertToTime,
    ConvertWindDirection,
    AirPollutionAverage,
  },
  data() {
    return {
      forecastDetails: null,
      forecastDayData: null,
      pollutionDetails: null,
      pollutionDayData: null,
    };
  },
  computed: {
    itemCity() {
      return this.$route.params.itemCity;
    },
    itemDt() {
      return this.$route.params.itemDt;
    },
    getAccessToken() {
      return this.$store.getters.getAccessToken;
    },
  },
  created() {
    this.fetchWeatherDetailsData();
  },
  methods: {
    async fetchWeatherDetailsData() {
      try {
        const lat = this.$route.query.lat;
        const lon = this.$route.query.lon;
        const openWeatherForecastResponse = await axios.get(
          `http://localhost:8020/po_app/WeatherDetails/?lat=${lat}&lon=${lon}`,
          {
            headers: {
              Authorization: `Bearer ${this.getAccessToken}`,
            },
          }
        );
        this.forecastDetails = openWeatherForecastResponse.data;
        const openWeatherPollutionResponse = await axios.get(
          `http://localhost:8020/po_app/WeatherPollution/?lat=${lat}&lon=${lon}`,
          {
            headers: {
              Authorization: `Bearer ${this.getAccessToken}`,
            },
          }
        );
        this.pollutionDetails = openWeatherPollutionResponse.data;
        this.filterSelectedDayData();
      } catch (error) {
        console.error("Request error:", error);
      }
    },
    filterSelectedDayData() {
      const itemDay = Math.floor(parseInt(this.itemDt) / 86400);
      if (this.forecastDetails && this.forecastDetails.list) {
        this.forecastDayData = this.forecastDetails.list.find(
          (day) => Math.floor(day.dt / 86400) === itemDay
        );
      }
      if (this.pollutionDetails && this.pollutionDetails.list) {
        this.pollutionDayData = this.pollutionDetails.list.find(
          (day) => Math.floor(day.dt / 86400) === itemDay
        );
      }
    },
  },
};
</script>

<style scoped>
/*body {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}*/

.weather-details-container {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  flex-grow: 1;
}

.details-container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
  margin: 0% 1.5% 0% 1%;
}

.details-item {
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
</style>
