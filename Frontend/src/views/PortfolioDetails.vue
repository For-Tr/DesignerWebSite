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
        newPath:null,
        status: null,

      }

    },
    mounted() {
          this.id = this.$route.params.id
          this.type = this.$route.params.type
          this.status = this.$route.params.status
          console.log(this.id)
          if (this.type == 'Mult') {
            if (this.status == 'edit') {
              this.newPath = '/multiscroll-portfolioEdit'
            } else {
                this.newPath = '/multiscroll-portfolioShow'
            }
             
          }
          if (this.type == 'Mini') {
            if (this.status == 'edit') {
              this.newPath = '/minimal-agencyEdit'
            } else {
              this.newPath = '/minimal-agencyShow'}
          }
          if (this.type == 'Free') {
            if (this.status == 'edit') {
              this.newPath = '/freelancerEdit'
            } else {
              this.newPath = '/freelancerShow'}
          }
          if (this.type == 'Agency') {
            if (this.status == 'edit') {
              this.newPath = '/agencyEdit'
            } else {
              this.newPath = '/agencyShow'}
          }
          if (this.type == 'Para') {
            if (this.status == 'edit') {
              this.newPath = '/parallax-homeEdit'
            } else {
              this.newPath = '/parallax-homeShow'}
          }
          if (this.type == 'Main') {
            if (this.status == 'edit') {
              this.newPath = '/main-demoEdit'
            } else {
              this.newPath = '/main-demoShow'}
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
