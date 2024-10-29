<template>
  <span>{{ convertToTemp }}°{{ unit }}</span>
</template>

<script>
export default {
  props: {
    tempK: {
      type: Number,
      required: true,
    },
    unit: {
      type: String,
      default: "C",
    },
  },
  computed: {
    convertToTemp() {
      let convertedTemperature;
      if (this.unit === "C") {
        convertedTemperature = (this.tempK - 273.15).toFixed(1);
      } else if (this.unit === "F") {
        convertedTemperature = (((this.tempK - 273.15) * 9) / 5 + 32).toFixed(
          1
        );
      }
      return convertedTemperature;
    },
  },
};
</script>
