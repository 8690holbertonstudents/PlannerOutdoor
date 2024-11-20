<template>
  <span>{{ convertToCelcius }}</span>
</template>

<script>
export default {
  name: "ConvertToCelcius",
  props: {
    tempK: {
      type: Number,
      required: true,
    },
  },
  computed: {
    convertToCelcius() {
      const tempInCelsius = this.tempK - 273.15;
      if (tempInCelsius) {
        return tempInCelsius.toFixed(1);
      } else {
        return "Input temp. err!";
      }
    },
  },
};
</script>
