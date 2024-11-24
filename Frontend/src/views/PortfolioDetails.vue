<template>
 <div class="portfolio-page">
    <HeaderThree></HeaderThree>

    <!-- Start Bradcaump area -->
    <div class="bradcaump_area">
      <div class="parallaxContainer paralaxbg--3" data-black-overlay="6" :style="{ 'background': 'url('+require('../assets/img/bg.jpg')+')'}">
        <v-container>
          <v-row>
            <v-col cols="12">
              <div class="text-center bradcaump_inner">
                <h2 class="bradcaump-title">
                  Portfolio
                </h2>
                <p> Using Pbuilder Website</p>
              </div>
            </v-col>
          </v-row>
        </v-container>
      </div>
    </div>
    <!-- End Bradcaump area -->

    <!-- Start Portfolio Area -->
    <div class="rn-portfolio-area section-ptb-100" id="portfolio">
      <v-container>
        <v-row>
          <v-col lg="12">
            <div class="section-title-2 text-center">

              <p>Your work will prove your quality</p>
            </div>
          </v-col>
        </v-row>
<PortfolioFive/>
      </v-container>
    </div>
    <!-- End Portfolio Area -->


    <!-- End Footer -->
  </div>
</template>

<script>
  import HeaderThree from "../components/header/HeaderThree";
import PortfolioFive from "../components/portfolio/PortfolioFive.vue";

  export default {
    components: {
      HeaderThree,
      PortfolioFive
    },
    data() {
      return{
        id : null,
        type: null,  
        newPath:null
      }

    },
    mounted() {
          this.id = this.$route.params.id
          this.type = this.$route.params.type
          console.log(this.id)
          if (this.type == 'Mult') {
              this.newPath = '/multiscroll-portfolioShow'
          }
          if (this.type == 'Mini') {
              this.newPath = '/minimal-agencyShow'
          }
          if (this.type == 'Free') {
              this.newPath = '/freelancerShow'
          }
          if (this.type == 'Agency') {
              this.newPath = '/agencyShow'
          }
          if (this.type == 'Para') {
              this.newPath = '/parallax-homeShow'
          }
          if (this.type == 'Main') {
              this.newPath = '/main-demoShow'
          }
          this.$router.push({path: this.newPath, query: {id: this.id}}); 
    }
  };
</script>

<style lang="scss" scoped>
  .portfolio-details-page .-rn-footer {
    background: #f9f9f9;
  }
</style>
