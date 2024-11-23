<template>
  <div class="freelancer-page">
    <HeaderMultiPageRoute />
    <SliderOne />
    <!-- Start Portfolio Area -->
    <div class="rn-portfolio-area section-ptb-xl" id="portfolio">
      <v-container>
        <v-row>
          <v-col lg="12">
            <div class="section-title-2 text-center">
              <h2>Our Portfolio</h2>
              <p>My work will prove my quality</p>
            </div>
          </v-col>
        </v-row>
        <Portfolio />
      </v-container>
    </div>
    <!-- End Portfolio Area -->


  </div>
</template>

<script>

  import SliderOne from "../../components/slider/SliderOne";
  import Portfolio from "../../components/portfolio/Portfolio";
import HeaderMultiPageRoute from "../../components/header/HeaderMultiPageRoute.vue";
  export default {
    components: {
      HeaderMultiPageRoute,
      SliderOne,
      Portfolio,
    },
    data() {
      return {};
    },
  };
</script>

<style lang="scss" scoped>
  .freelancer-page .logo {
    img {
      @media only screen and (max-width: 575px) {
        max-width: 80%;
      }
    }
  }
</style>
