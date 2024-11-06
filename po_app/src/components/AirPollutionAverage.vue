<template>
  <div>
    <p>Vehicle Emissions:</p>
    <span>{{ vehiclePollution }}</span>
    <p>Industrial Emissions:</p>
    <p>
      <span>{{ industrialPollution }}</span>
    </p>
    <p>Agricultural Emissions:</p>
    <p>
      <span>{{ agriculturalPollution }}</span>
    </p>
  </div>
</template>

<script>
export default {
  name: "AirPollutionAverage",
  props: {
    components: {
      type: Object,
      required: true,
    },
  },
  computed: {
    vehiclePollution() {
      const average = this.calculateAverage([
        this.components.co,
        this.components.no,
        this.components.no2,
        this.components.pm2_5,
        this.components.pm10,
      ]);
      return this.vehiculePollutionLevels(average);
    },
    industrialPollution() {
      const average = this.calculateAverage([
        this.components.co,
        this.components.so2,
      ]);
      return this.IndustrialPollutionLevels(average);
    },
    agriculturalPollution() {
      const average = this.calculateAverage([this.components.nh3]);
      return this.agriculturalPollutionLevels(average);
    },
  },
  methods: {
    calculateAverage(values) {
      const validValues = values.filter((value) => value !== undefined);
      if (validValues.length === 0) return "Unknown";
      return validValues.reduce((a, b) => a + b, 0) / validValues.length;
    },
    vehiculePollutionLevels(average) {
      if (average <= 60) return "Good";
      if (average <= 150) return "Moderate";
      if (average <= 450) return "Unhealthy";
      return "Very Unhealthy";
    },
    IndustrialPollutionLevels(average) {
      if (average <= 50) return "Good";
      if (average <= 250) return "Moderate";
      if (average <= 550) return "Unhealthy";
      return "Very Unhealthy";
    },
    agriculturalPollutionLevels(average) {
      if (average <= 40) return "Good";
      if (average <= 220) return "Moderate";
      if (average <= 600) return "Unhealthy";
      return "Very Unhealthy";
    },
  },
};
</script>
