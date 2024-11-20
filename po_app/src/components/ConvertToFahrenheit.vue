<template>
  <span>{{ convertToFahrenheit }}</span>
</template>

<script>
export default {
  name: "ConvertToFahrenheit",
  props: {
    tempK: {
      type: Number,
      required: true,
    },
  },
  computed: {
    convertToFahrenheit() {
      const tempInFahrenheit = (this.tempK - 273.15) * 1.8 + 32;
      if (tempInFahrenheit) {
        return tempInFahrenheit.toFixed(1);
      } else {
        return "Input temp. err!";
      }
    },
  },
};
</script>
