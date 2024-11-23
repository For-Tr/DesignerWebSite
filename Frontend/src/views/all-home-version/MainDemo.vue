<template>
  <div class="main-demo-page">
    <HeaderMultiPageRoute>

    </HeaderMultiPageRoute>
    <!-- End Header One Area -->

    <!-- Start Slider Area -->
    <div class="rv-slider-wrapper black-pagination pagination-bottom" id="home">
      <SliderThree />
    </div>
    <!-- End Slider Area -->

   
  </div>
</template>

<script>
  import HeaderMultiPageRoute from "../../components/header/HeaderMultiPageRoute";
  import SliderThree from "../../components/slider/SliderThree";

  export default {
    components: {
      HeaderMultiPageRoute,
      SliderThree,

    },
    data() {
      return {
        aboutSrc: require("../../assets/img/portfolio/our-story.jpg"),
        skillSrc: require("../../assets/img/portfolio/my-skill.jpg"),
      };
    },
  };
</script>

<style lang="scss" scoped>
  .main-demo-page {
    @media only screen and (max-width: 767px) {
      .rn-skill-right {
        order: 2;
      }
      .rn-story-area {
        margin-top: -8px;
      }
    }
  }
</style>
