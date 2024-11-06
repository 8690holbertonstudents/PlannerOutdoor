<template>
  <div :style="backgroundStyle" class="background-container"></div>
</template>

<script>
const backgroundImages = [
  "adventure-1851092.jpg",
  "away-3408119.jpg",
  "bird-8132549.jpg",
  "field-5236879.jpg",
  "fishing-209112.jpg",
  "forest-3804001.jpg",
  "gardening-7146939.jpg",
  "hochybrig-4683994.jpg",
  "kiters-3724717.jpg",
  "lake-3113868.jpg",
  "leaves-8355509.jpg",
  "mount-everest-6395759.jpg",
  "mountains-6964409.jpg",
  "paraglider-4751693.jpg",
  "rock-climbing-1283693.jpg",
  "snowboard-113784.jpg",
  "tent-548022.jpg",
  "trees-4830285.jpg",
  "water-7055153.jpg",
  "windsurfing-2298647.jpg",
];

const transitionTime = 5000;

const transitionsBackground = [
  "2s ease",
  "2s linear",
  "2s ease-in",
  "2s ease-out",
  "2s ease-in-out",
];

export default {
  name: "AnimatedBackgroundApp",

  data() {
    return {
      backgroundImage: backgroundImages[0],
      indexImage: 0,
      transitionsBackground: transitionsBackground[0],
    };
  },

  computed: {
    backgroundStyle() {
      return {
        backgroundImage: `url('/background/${this.backgroundImage}')`,
        transition: `background-image ${this.transitionsBackground}`,
      };
    },
  },

  methods: {
    getRandomBackgroundImage() {
      this.indexImage = (this.indexImage + 1) % backgroundImages.length;
      this.backgroundImage = backgroundImages[this.indexImage];
      this.transitionsBackground = [
        Math.floor(Math.random() * transitionsBackground.length),
      ];
    },
  },

  mounted() {
    this.getRandomBackgroundImage();
    setInterval(this.getRandomBackgroundImage, transitionTime);
  },
};
</script>

<style scoped>
.background-container {
  position: fixed;
  top: 0;
  left: 0;
  z-index: -1;
  height: 100vh;
  width: 100vw;
  background-size: cover;
  background-position: center;
  background-repeat: repeat-y;
}
</style>
