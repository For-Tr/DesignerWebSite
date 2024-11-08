<template>
  <div>
    <HeaderThree />

    <!-- Start Bradcaump area -->
    <div class="bradcaump_area">
      <div class="parallaxContainer paralaxbg--3" data-black-overlay="6">
        <v-container>
          <v-row>
            <v-col cols="12">
              <div class="text-center bradcaump_inner">
                <h2 class="bradcaump-title">
                  Blog
                </h2>
                <p>Fresh From The Press Discription</p>
              </div>
            </v-col>
          </v-row>
        </v-container>
      </div>
    </div>
    <!-- End Bradcaump area -->

    <News />
    <!-- End News -->

  </div>
</template>

<script>
import HeaderThree from "../components/header/HeaderThree.vue";
  import News from "../components/news/News";
  export default {
    components: {
      HeaderThree,
      News,
    },
    data() {
      return {};
    },
  };
</script>

<style lang="scss" scoped></style>
