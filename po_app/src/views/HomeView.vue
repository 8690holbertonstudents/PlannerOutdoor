<template>
  <div class="home-container">
    <div class="title-item">
      <h1>Welcome to PlannerOutdoor !</h1>
      <h3>
        This project enables users with an account to plan their outdoor
        activities, taking into account weather conditions and any allergies
        they may have.
      </h3>
      <h3>
        This project is not yet complete, and unfortunately not all features
        have been implemented.
      </h3>
      <h2>Work in progress !!!</h2>
    </div>
    <div>
      <GeolocateView />
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

.title-item {
  margin-top: 50px;
  width: 500px;
}

h1,
h2 {
  text-align: center;
  margin-bottom: 50px;
}

h3 {
  text-align: justify;
  margin-bottom: 50px;
}
</style>
