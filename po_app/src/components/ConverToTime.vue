<template>
  <span>{{ convertToTime }}</span>
</template>

<script>
export default {
  props: {
    timestamp: {
      type: Number,
      required: true,
    },
  },
  computed: {
    convertToTime() {
      const date = new Date(this.timestamp * 1000);
      return date.toLocaleTimeString("en-GB", {
        hour: "2-digit",
        minute: "2-digit",
      });
    },
  },
};
</script>
