<template>
  <PageHeader />
  <div id="app">
    <router-view></router-view>
    <!-- Affiche la vue correspondante -->
  </div>
  <PageFooter />
</template>

<script>
import PageHeader from "@/components/PageHeader.vue";
import PageFooter from "./components/PageFooter.vue";

export default {
  name: "App",
  components: {
    PageHeader,
    PageFooter,
  },
};
</script>

<style>
#app {
  font-family: "Segoe UI", Tahoma, "Geneva", "Verdana", "sans-serif";
}
body {
  min-height: 100vh;
  display: grid;
  grid-template-rows: [header] auto [content] 1fr [footer] auto;
}
</style>
