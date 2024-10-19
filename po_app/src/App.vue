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
  /*
  --section-header-align: center;
  --section-tagline-transform: uppercase;
  --section-title-margin: 0;
  --section-title-color: var(--color-black);
  --section-padding: 5rem 0;
  --section-header-padding: 0 0 3rem;
  --section-body-padding: 0 0 3rem;
  --section-footer-padding: 3rem 0 0;
  --section-footer-align: center;
  --footer-padding: 5rem 0 1rem;
  --nav-item-font-family: var(--font-family-title);
  --nav-item-font-weight: var(--font-weight-bold);
  --nav-item-font-size: var(--font-size-medium);
  --nav-item-letter-spacing: 0.04rem;
  --nav-item-display: inline-block;
  --nav-item-margin: 0 0 3rem 0;
  --nav-item-link-hover: var(--color-white);
  --section-tagline-margin: 0;
  --button-display: inline-block;
  --button-padding: 1.5rem 3rem;
  --button-border: 0.2rem solid var(--color-primary);
  --button-color: var(--color-black);
  --button-text-decoration: none;
  --button-font-size: var(--font-size-large);
  --button-hover-color: var(--color-white);
  --button-hover-text-decoration: none;
  --button-hover-background: var(--color-primary);
  --header-padding: 4rem 0 0;
  --header-logo-position: relative;
  --header-logo-link-display: inline-block;
  --header-logo-link-position: absolute;
  --header-logo-link-top: -1rem;
  --header-logo-link-left: 0;
  --transition-duration: 0.3s;
  --transition-cubic-bezier: cubic-bezier(0.17, 0.67, 0, 1.01);
  */
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
