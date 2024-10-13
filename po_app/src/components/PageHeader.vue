<template>
  <header>
    <nav class="menu">
      <router-link to="/">Home</router-link>
      <router-link to="/weather">Weather</router-link>
    </nav>
  </header>
</template>

<script>
export default {
  name: "PageHeader",
};
</script>

<style scoped>
header {
  grid-row: header;
  height: 50px;
  width: 98%;
  background-color: #209fe8;
  border-radius: 5px;
  color: white;
  margin: 0 auto;
  padding: 10px;
}
.menu {
  padding: 15px;
}
</style>
