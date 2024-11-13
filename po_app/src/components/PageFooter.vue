<template>
  <footer class="footer-container">
    <div class="footer-item-left">
      <a href="https://www.holbertonschool.fr/" target="_blank">
        <img src="/images/seahorse_white.png" alt="holberton" />
      </a>
    </div>
    <div class="footer-item-center">
      <p>PlannerOutdoor portfolio project - November 2024</p>
    </div>
    <div class="footer-item-right">
      <div class="link-container">
        <a
          href="https://github.com/8690holbertonstudents/PlannerOutdoor"
          target="_blank"
          class="link-item"
        >
          <img src="/images/github.png" alt="github project" />
        </a>
        <a
          href="https://www.linkedin.com/in/emmanuel-mg197274470/"
          target="_blank"
          class="link-item"
        >
          <img src="/images/linkedin.png" alt="linkedin" />
        </a>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "PageFooter",
};
</script>

<style scoped>
.footer-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  height: var(--header-footer-height);
  width: var(--header-footer-width);
  background-color: var(--color-header-footer);
  color: var(--color-white);
}

.footer-item-left {
  flex-basis: 5%;
}

.footer-item-left img {
  height: 1.5rem;
  width: 1.5rem;
  padding-left: 1rem;
}

.footer-item-center {
  flex-basis: 90%;
  text-align: center;
  font-size: var(--font-size-small);
  font-weight: var(--font-weight-bold);
}

.footer-item-right {
  flex-basis: 5%;
}

.footer-item-right img {
  height: 1.5rem;
  width: 1.5rem;
  padding-right: 1rem;
}

.link-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.link-item {
  margin: 0 0.5rem;
}
</style>
