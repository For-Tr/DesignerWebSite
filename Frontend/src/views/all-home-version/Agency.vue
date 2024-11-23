<template>
  <div>
    <HeaderMultiPageRoute />
    <SliderTwo />
    <!-- Start Portfolio Area -->
    <div class="rn-portfolio-area section-ptb-xl" id="portfolio">
      <v-container>
        <v-row>
          <v-col lg="12">
            <div class="text-center section-title-2">
              <h2>Our Portfolio</h2>
              <p>My work will prove my quality</p>
            </div>
          </v-col>
        </v-row>
        <PortfolioTwo />
      </v-container>
    </div>

  </div>
</template>

<script>

  import SliderTwo from "../../components/slider/SliderTwo";
  import PortfolioTwo from "../../components/portfolio/PortfolioTwo";
import HeaderMultiPageRoute from "../../components/header/HeaderMultiPageRoute.vue";
  export default {
    components: {
      HeaderMultiPageRoute,
      SliderTwo,
      PortfolioTwo,

    },
    data() {
      return {};
    },
  };
</script>

<style lang="scss" scoped></style>
