<template>
  <div class="home-container">
    <div class="title-item">
      <h1>Welcome to PlannerOutdoor !</h1>
      <p>The goal of this project is.....in progress</p>
    </div>
    <div>
      <GeolocateView />
      <!-- Not made yet !!!!!! -->
    </div>
  </div>
</template>

<script>
import GeolocateView from "@/components/GeolocateView.vue";

export default {
  components: {
    GeolocateView,
  },
};
</script>

<style scoped>
.home-container {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  justify-content: center;
  align-items: flex-start;
}

p {
  text-align: center;
}
</style>
