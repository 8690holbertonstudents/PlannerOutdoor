<template>
  <div id="app">
    <div id="header-app">
      <PageHeader />
    </div>
    <main class="main-content">
      <router-view />
    </main>
    <div id="footer-app">
      <PageFooter />
    </div>
  </div>
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
:root {
  --color-black: #090909;
  --color-white: #ffffff;
  --color-light-grey: #f3f3f3;
  --color-medium-grey: #726a6a;
  --color-dark-grey: #353535;
  --color-header-footer: #209fe8;
  --color-background-modal: rgba(0, 0, 0, 0.5);
  --header-footer-shadow: 5px 5px 5px var(--color-medium-grey);
  --modal-shadow: 30px 30px 30px var(--color-dark-grey);
  --header-footer-height: 35px;
  --header-footer-width: 98%;
  --header-footer-border: 10px;
  --font-family: "Ubuntu", sans-serif;
  --font-size-small: 0.7rem;
  --font-size-medium: 1.2rem;
  --font-size-large: 1.5rem;
  --font-size-x-large: 2rem;
  --font-size-xx-large: 3rem;
  --font-weight-regular: 400;
  --font-weight-bold: 700;
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  overflow-y: auto;
  font-family: var(--font-family);
}

#app > #header-app {
  flex-shrink: 0;
}

#app > #footer-app {
  flex-shrink: 0;
}

.main-content {
  display: flex;
  flex: 1;
  overflow-y: auto;
}
</style>
