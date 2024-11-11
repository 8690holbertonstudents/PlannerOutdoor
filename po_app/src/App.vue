<template>
  <div class="app-container">
    <AnimatedBackgroundApp />
    <PageHeader class="header" />
    <router-view />
    <PageFooter class="footer" />
  </div>
</template>

<script>
import PageHeader from "@/components/PageHeader.vue";
import PageFooter from "./components/PageFooter.vue";
import AnimatedBackgroundApp from "./components/AnimatedBackgroundApp.vue";

export default {
  name: "App",
  components: {
    PageHeader,
    PageFooter,
    AnimatedBackgroundApp,
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
  --color-error-msg: #c63434;
  --color-success-msg: #1d01a8;
  --color-header-footer: rgba(32, 159, 232, 0.75);
  --color-button: rgba(32, 159, 232, 1);
  --header-footer-opacity: 0.7;
  --color-background-modal: rgba(0, 0, 0, 0.5);
  --color-background-item: rgba(255, 255, 255, 0.7);
  --header-footer-shadow: 5px 5px 5px var(--color-medium-grey);
  --modal-shadow: 30px 30px 30px var(--color-dark-grey);
  --header-footer-height: 50px;
  --margin-header-footer: calc((var(--header-footer-height)) + 10px);
  --header-footer-width: 100%;
  --default-radius: 10px;
  --font-family: "Ubuntu", sans-serif;
  --font-size-small: 0.7rem;
  --font-size-medium: 1.2rem;
  --font-size-large: 1.5rem;
  --font-size-x-large: 2rem;
  --font-size-xx-large: 3rem;
  --font-weight-regular: 400;
  --font-weight-bold: 700;
}

html,
body,
.app-container {
  height: 100vh;
  width: 100vw;
  margin: 0;
}

.app-container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: stretch;
  font-family: var(--font-family);
}

.header {
  position: fixed;
  top: 0;
}

.footer {
  position: fixed;
  bottom: 0;
}
</style>
