<template>
  <span>{{ convertToDate }}</span>
</template>

<script>
export default {
  name: "ConvertToDate",
  props: {
    timestamp: {
      type: Number,
      required: true,
    },
  },
  computed: {
    convertToDate() {
      const date = new Date(this.timestamp * 1000);
      const month = date
        .toLocaleString("en-EN", { month: "long" })
        .toUpperCase();
      const year = date.getFullYear();
      return `${month} ${year}`;
    },
  },
};
</script>
