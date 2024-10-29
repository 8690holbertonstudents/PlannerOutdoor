<template>
  <div class="weather-details-container">
    <div class="title-item">
      <h2>
        Weather at {{ itemCity }} - <ConvertToDate :timestamp="itemDt" /> -
        <ConvertToDay :timestamp="itemDt" />
      </h2>
    </div>
  </div>
</template>

<script>
import ConvertToDate from "@/components/ConvertToDate.vue";
import ConvertToDay from "@/components/ConvertToDay.vue";
//import ConvertToTemp from "@/components/ConvertToTemp.vue";

export default {
  components: { ConvertToDate, ConvertToDay },
  computed: {
    itemCity() {
      return this.$route.params.itemCity;
    },
    itemDt() {
      return this.$route.params.itemDt;
    },
  },
};
</script>

<style scoped>
.weather-details-container {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  justify-content: center;
  align-items: flex-start;
}
</style>
