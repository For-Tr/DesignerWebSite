<template>
  <div>
<HeaderThree></HeaderThree>
    <!-- Start Bradcaump area -->
    <div class="bradcaump_area">
      <div class="parallaxContainer paralaxbg--3" data-black-overlay="6">
        <v-container>
          <v-row>
            <v-col cols="12">
              <div class="text-center bradcaump_inner">
                <h2 class="bradcaump-title">
                  Awards
                </h2>
                <p>Fresh From The Press Discription</p>
              </div>
            </v-col>
          </v-row>
        </v-container>
      </div>
    </div>
    <!-- End Bradcaump area -->

    <Awards />
    <!-- End Awards -->

    <Footer />
    <!-- End Footer -->
  </div>
</template>

<script>
  import Awards from "../components/awards/Awards";
  import Footer from "../components/footer/Footer";
import HeaderThree from "../components/header/HeaderThree.vue";
  export default {
    components: {
      HeaderThree,
      Awards,
      Footer,
    },
    data() {
      return {};
    },
  };
</script>

<style lang="scss" scoped></style>
