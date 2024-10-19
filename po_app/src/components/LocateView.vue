<template>
  <div id="locate-form">
    <input
      type="text"
      v-model="city"
      placeholder="Enter a city..."
      @keyup.enter="submitCity"
    />
  </div>
</template>

<script>
export default {
  data() {
    return {
      city: "",
    };
  },
  methods: {
    submitCity() {
      if (this.city) {
        // Redirige vers WeatherView avec la localisation en tant que query param
        this.$router.push({
          name: "Weather",
          query: { city: this.city },
        });
      }
    },
  },
};
</script>

<style scoped>
input {
  height: 10px;
  width: 150px;
  padding: 8px;
  border-radius: var(--header-footer-border);
  border: 1px solid var(--color-white);
  font-size: var(--font-size-small);
}
</style>
