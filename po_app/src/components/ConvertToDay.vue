<template>
  <span>{{ convertToDay }}</span>
</template>

<script>
export default {
  name: "ConvertToDay",
  props: {
    timestamp: {
      type: Number,
      required: true,
    },
  },
  computed: {
    convertToDay() {
      const date = new Date(this.timestamp * 1000);
      const dayOfWeek = date
        .toLocaleDateString("en-EN", { weekday: "long" })
        .toUpperCase();
      const dayOfMonth = date.getDate();
      return `${dayOfWeek} ${dayOfMonth}`;
    },
  },
};
</script>
