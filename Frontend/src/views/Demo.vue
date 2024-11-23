<template>
  <div>
    <HeaderThree />


    <!-- Banner -->
    <div class="banner-wrapper">
      <v-container fluid>
        <div class="banner-inner">
          <div class="banner-content">
            <h1>
              PBuilder - Minimal Creative Portfolio for <br />
              Designers, Developers & Freelancers.
            </h1>
          </div>
          <div class="banner-image">
            <div class="banner-image-inner">
              <img
                class="laptop"
                src="../assets/img/demos/laptop.png"
                alt="laptop"
              />
              <img
                class="tablet"
                src="../assets/img/demos/tablet.png"
                alt="tablet"
              />
              <img
                class="phone"
                src="../assets/img/demos/phone.png"
                alt="phone"
              />
            </div>
          </div>
        </div>
      </v-container>
    </div>
    <!-- End Banner -->

    <!-- Demos -->
    <div class="demo-wrapper bg_color--1">
      <v-container fluid>
        <v-row>
          <v-col md="12" class="text-center">
            <div class="title-wrapper">
              <h1 class="text-center">Templates</h1>
              <p>
                Choose one of the templates to create your portfolio
              </p>
            </div>
          </v-col>
        </v-row>
        <v-row>
          <v-col
            lg="4"
            md="6"
            sm="12"
            cols="12"
            v-for="(item, i) in demoContent"
            :key="i"
          >
            <div class="demo-item">
              <router-link :to="item.href" target="_blank">
                <img :src="item.src" alt="Main Demo" />
                <span>{{ item.title }}</span>
              </router-link>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </div>
    <!-- End Demos -->



    <!-- Footer -->
    <footer class="footer demo-footer bg_color--1">
      <div class="slider-area slide--5" id="home">
        <v-container>
          <v-row>
            <v-col lg="12">
              <div class="text-center content">
                <h1>
                  Use PBuilder and make your portfolio excellent.
                </h1>

              </div>
            </v-col>
          </v-row>
        </v-container>
      </div>
    </footer>
    <!--// Footer -->
  </div>
</template>

<script>
  import feather from "feather-icons";
  import HeaderThree from "../components/header/HeaderThree";

  export default {
    components: {
      HeaderThree
    },
    data() {
      return {
        demoContent: [
        {
            src: require("../assets/img/demos/multiscroll.jpg"),
            title: "Multi Scroll",
            href: "/multiscroll-portfolio",
          },
          {
            src: require("../assets/img/demos/home-3.jpg"),
            title: "Minimal Agency",
            href: "/minimal-agency",
          },
          {
            src: require("../assets/img/demos/home-9.jpg"),
            title: "Freelancer",
            href: "/freelancer",
          },
          {
            src: require("../assets/img/demos/home-7.jpg"),
            title: "Parallax",
            href: "/parallax-home",
          },
          {
            src: require("../assets/img/demos/home-8.jpg"),
            title: "Agencies",
            href: "/agency",
          },

          {
            src: require("../assets/img/demos/home-1.jpg"),
            title: "Main Demo",
            href: "/main-demo",
          },
          {
            src: require("../assets/img/demos/home-6.jpg"),
            title: "Vertical Portfolio",
            href: "/vertical-portfolio",
          },
          {
            src: require("../assets/img/demos/home-5.jpg"),
            title: "Creative Portfolio",
            href: "/creative-portfolio",
          },
        

          {
            src: require("../assets/img/demos/home-4.jpg"),
            title: "Designer Portfolio",
            href: "/designer-portfolio",
          },
        
          {
            src: require("../assets/img/demos/home-coming.jpg"),
            title: "More templates is coming",
            href: "/",
          },
         
        ],
        
        
        panel: 0,
      };
    },
    methods: {
      iconSvg(icon) {
        return feather.icons[icon].toSvg();
      },
      

    },
  };
</script>

<style lang="scss" scoped>
  .theme--light.about-expension-panels .v-expansion-panel-content p {
    color: #333;
    font-size: 15px;
    margin-bottom: 0;
  }
  .slide--5 .content h1 {
    color: #000;
  }
  b,
  strong {
    font-weight: 400;
  }
  .theme--light.about-expension-panels .v-expansion-panel-header {
    margin-top: 20px;
    margin-bottom: 15px;
    padding: 0 0 10px 0;
    font-size: 18px;
    color: #000;
    border: none;
    @media only screen and (max-width: 767px) {
      margin-bottom: 5px;
    }
  }
  .theme--light.about-expension-panels .v-expansion-panel {
    background-color: transparent;
    color: #1f1f25;
  }

  .demo-wrapper {
    margin-top: 130px;

    &.inner-pages {
      margin-top: 0;
    }
  }
  .bg_color--1 {
    background: #f9f9f9;
  }
  .bg_color--2 {
    background: #fff;
  }
  .section-title {
    h2 {
      font-size: 50px;
      font-weight: 600;
      line-height: 62px;
      margin-bottom: 20px;
      color: #000 !important;
      @media only screen and (max-width: 767px) {
        font-size: 34px;
        line-height: 45px;
      }
    }
    p {
      color: #333;
    }
  }

  @media only screen and (max-width: 767px) {
    .pv-feaq-area {
      &.ptb--120 {
        padding: 60px 0;
      }
    }
    .section-title h2 {
      font-size: 30px;
      line-height: 40px;
    }
    .section-title.text-left.pb--30 {
      padding-bottom: 0;
    }
    .slide--5 .content h1 {
      font-size: 25px;
      line-height: 40px;
    }
  }

  .single-feature {
    background: #fff;
    padding: 50px;
    transition: transform 0.65s cubic-bezier(0.05, 0.2, 0.1, 1),
      box-shadow 0.65s cubic-bezier(0.05, 0.2, 0.1, 1);
    z-index: 2;
    border-radius: 10px;
    height: 100%;
    @media only screen and (max-width: 767px) {
      padding: 25px 15px;
    }

    .icon {
      font-weight: 400;
      margin-bottom: 23px;
      display: inline-flex;
    }

    h3 {
      margin-bottom: 19px;
      font-weight: 600;
      font-size: 20px;
      color: #333;
    }
    p {
      color: #333;
    }
  }
  .plr--120 {
    padding: 0 120px;
  }
  .features-area {
    [class*="col-"] {
      margin-top: 30px;
    }
  }
  .features-area {
    .col-lg-12 {
      margin-top: 0;
    }
  }
  strong,
  .theme-gradient,
  .v-application .pv-feaq-area a {
    color: #f42a59 !important;
  }
  .demo-wrapper {
    @media screen and (min-width: 768px) {
      [class*="col-"] {
        padding: 0 35px;
      }
    }
    .demo-item {
      background: #fff;
      box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.05);
    }
  }
  .demo-wrapper {
    &.inner-pages {
      .demo-item {
        box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.05);
      }
    }
  }
  @media (max-width: 767px) {
    .banner-content h1 {
      font-size: 28px;
      line-height: 42px;
    }
  }
  .section-title {
    @media (max-width: 767px) {
      &.pb_md--0 {
        padding-bottom: 0;
      }
      p {
        margin-bottom: 10px;
      }
    }
  }
</style>

<style lang="scss">
  .theme--light.about-expension-panels {
    .v-expansion-panel-header {
      min-height: 30px;
      padding: 0 0 5px 0;
      margin-top: 7px;
      margin-bottom: 8px;
      font-size: 16px;
      line-height: 24px;
      font-weight: 500;
      display: inline-flex;
      width: auto;
      font-family: "Poppins", sans-serif;

      &::after {
        position: absolute;
        content: "";
        left: 0;
        bottom: 0;
        width: 100%;
        height: 1px;
        background: #555;
        -webkit-transition: 0.3s;
        -o-transition: 0.3s;
        transition: 0.3s;
      }
      &:not(.v-expansion-panel-header--mousedown):focus::before {
        opacity: 0;
      }
    }
    .v-expansion-panel {
      background-color: transparent;
      color: #1f1f25;
    }
    .v-expansion-panel-content__wrap {
      font-size: 18px;
      line-height: 30px;
      background: none;
      border: none;
      padding: 0 0 15px;
    }
  }
  .single-feature {
    svg {
      width: 54px;
      height: 54px;
      stroke-width: 1 !important;
    }
    &:hover {
      box-shadow: 0 2px 70px 0 rgb(253 71 102 / 5%);
      transform: translateY(-5px);
    }
    .vue {
      color: #42b883;
    }
    .vuetify {
      color: #1867c0;
    }
    .code {
      color: #12d8df;
    }
    .sass {
      color: #59c98d;
    }
    .support {
      color: #f767b4;
    }
    .speed {
      color: #6f41f6;
    }
    .responsive {
      color: #337dff;
    }
    .modern {
      color: #fd4766;
    }
  }
  .features-area {
    padding: 120px 120px;
    @media only screen and (max-width: 767px) {
      padding: 60px 15px;
    }
  }
  .pv-feaq-area.ptb--120 {
    @media only screen and (max-width: 991px) {
      padding: 100px 0;
    }
  }
</style>
