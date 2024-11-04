<template>
  <footer>
    <div id="footer-text">PlannerOutdoor portfolio project - November 2024</div>
  </footer>
</template>

<script>
export default {
  name: "PageFooter",
};
</script>

<style scoped>
footer {
  display: flex;
  justify-content: center;
  margin-bottom: 10px;
  height: var(--header-footer-height);
  width: var(--header-footer-width);
  background-color: var(--color-header-footer);
  color: var(--color-white);
  border-radius: var(--header-footer-border);
  box-shadow: var(--header-footer-shadow);
}
#footer-text {
  display: flex;
  align-items: center;
  font-size: var(--font-size-small);
}
</style>
