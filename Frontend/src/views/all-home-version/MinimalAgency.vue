<template>
  <div class="box-layout">
    <HeaderMultiPageRoute>

</HeaderMultiPageRoute>

    <!-- Start Hero Area -->
    <SliderFour />
    <!-- Start Story Area -->

    <div class="mt--100 mt-sm-10">
      <About />
    </div>
    <!-- End Story Area -->


  </div>
</template>

<script>
  import HeaderMultiPageRoute from "../../components/header/HeaderMultiPageRoute";
  import SliderFour from "../../components/slider/SliderFour";
  import About from "../../components/about/About";
  export default {
    components: {
      HeaderMultiPageRoute,
      SliderFour,
      About,
    },
    data() {
      return {
        aboutSrc: require("../../assets/img/portfolio/about-image.jpg"),
      };
    },
  };
</script>

<style lang="scss" scoped>
  .box-layout {
    .-rn-footer {
      background: #f9f9f9;
    }
    header.header.header-flat {
      padding: 0;
    }
  }
</style>
<style lang="scss">
  .box-layout {
    header.header.header-flat,
    .v-toolbar__content {
      padding: 0;
    }
    .mt--100.mt-sm-10 {
      margin-top: 50px;
    }
  }
</style>
