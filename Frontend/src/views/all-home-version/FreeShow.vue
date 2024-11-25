<template>
    <div class="freelancer-page">
       <!-- Start Single Slider -->
  <div>
    <VueSlickCarousel
      v-bind="settings"
      class="slider-activation-with-slick rn-slick-dot dot-light mb--0"
    >
      <div
        class="slider--8 fullscreen d-flex align-center justify-center fullscreen bg_image rfanimation-style--1"
        v-for="(slider, i) in sliderContent"
        :key="i"
        :style="{ backgroundImage: 'url(' + slider.src + ')' }"
      >
        <v-container>
          <v-row>
            <v-col cols="12">
              <div class="content text-center">
                <h2 class="heading-title">{{ slider.title }}</h2>
                <p class="description">
                  {{ slider.desc }}
                </p>
                <div class="slide-btn mt-10">
                  <router-link class="rf-btn" to="/contact"
                    >Contact Us</router-link
                  >
                </div>
              </div>
            </v-col>
          </v-row>
        </v-container>
      </div>
      <!-- End Single Slide  -->
    </VueSlickCarousel>
  </div>
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
          <div
    class="row portfolio-wrapper row--55 rn-custom-portfolio-wrapper rn-hil-portfolio"
  >
    <v-col
      lg="4"
      md="4"
      sm="6"
      cols="12"
      v-for="(content, i) in portfolioContent"
      :key="i"
    >
      <router-link to="" class="portfolio-wrap">
        <div class="item-shadow"  :style="{ backgroundImage: 'url(' + content.src + ')' }">
        </div>
        <div class="portfolio" :style="{ backgroundImage: 'url(' + content.src + ')' }">
          <div class="content"> 
            <h4 class="title">{{ content.title }}</h4>
            <span class="desc">{{ content.desc }}</span>
          </div>
        </div>
      </router-link>
    </v-col>
    <!-- Start Single Portfoli -->
  </div>
        </v-container>
      </div>
      <!-- End Portfolio Area -->
  
      <div style="display: flex; justify-content: center;">
      <HeaderShow :Email="Email"></HeaderShow>

       </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
import {BASE_URL} from "../../utils/BASE"
    import VueSlickCarousel from "vue-slick-carousel";
    import HeaderShow from '../../components/header/HeaderShow.vue';
    export default {
        components: { VueSlickCarousel, HeaderShow},
      data() {
        const newForm = {
    pic1: require("../../assets/img/bg/bg-image-14.jpg"),
    pic2: require("../../assets/img/bg/bg-image-13.jpg"),
    pic3: require("../../assets/img/bg/bg-image-15.jpg"),
    pic4: require("../../assets/img/slider/slider-6.jpg"),
    pic5: require("../../assets/img/slider/slider-6.jpg"),
    pic6: require("../../assets/img/bg/bg-image-14.jpg"),
    pic7: require("../../assets/img/bg/bg-image-13.jpg"),
    pic8: require("../../assets/img/bg/bg-image-15.jpg"),
    pic9: require("../../assets/img/slider/slider-6.jpg"),
    text1: null,
    text2: null,
    text3: null,
    text4: null,
    text5: null,
    text6: null,
    text7: null,
    text8: null,
    text9: null,
    text10: null,
    text11: null,
    text12: null,
    text13: null,
    text14: null,

  }
        return {
        newForm: newForm,
            sliderContent: [
          {
            src:  require("../../assets/img/bg/bg-image-13.jpg"),
            title: "Developer",
            desc: ` There are many variations of passages of Lorem Ipsum available
                  but the majority have suffered alteration.`,
          },
          {
            src: require("../../assets/img/bg/bg-image-13.jpg"),
            title: "Designer",
            desc: `There are many variations of passages of Lorem Ipsum available 
                  but the majority have suffered alteration.`,
          },

          {
            src: require("../../assets/img/bg/bg-image-15.jpg"),
            title: "Visual Design",
            desc: ` There are many variations of passages of Lorem Ipsum available
                  but the majority have suffered alteration.`,
          },
        ],
        portfolioContent: [
          {
            src: "",
            title: "",
          },
          {
            src: "",
            title: "",
          },
          {
            src: "",
            title: "",
          },
          {
            src: "",
            title: "",
          },
          {
            src: "",
            title: "",
          },
          {
            src: "",
            title: "",
          },

        ],
        settings: {
          fade: true,
          dots: true,
          arrows: true,
          infinite: true,
          speed: 1000,
          slidesToShow: 1,
          slidesToScroll: 1,
          margin: 20,
        },
        };
      },
      mounted() {
    this.id = this.$route.query.id;
    this.fetchData()
  },
  methods: {
    async fetchData() {
      if (!this.id) {
        this.error = 'No ID provided';
        alert(this.error)
        return;
      }

      this.loading = true; // 开始加载

      try {
        const response = await axios.get(`/api/notes/${this.id}`);

       


        response.data.pic.forEach(item => {
            const key = `pic${item.order_num}`;
            this.newForm[key] = BASE_URL + item.pic; 
        });

        this.Email = response.data.user.email
        console.log('111' + this.Email)
        response.data.text.forEach(item => {
            const key = `text${item.order_num}`;
            this.newForm[key] = item.text; 
        });


        console.log(this.newForm);
        this.sliderContent[0].title = this.newForm.text1
        this.sliderContent[0].desc = this.newForm.text2
        this.sliderContent[0].src = this.newForm.pic1
        this.sliderContent[1].title = this.newForm.text3
        this.sliderContent[1].desc = this.newForm.text4
        this.sliderContent[1].src = this.newForm.pic2
        this.sliderContent[2].title = this.newForm.text5
        this.sliderContent[2].desc = this.newForm.text6
        this.sliderContent[2].src = this.newForm.pic3

this.portfolioContent[0].title =this.newForm.text7
this.portfolioContent[0].src = this.newForm.pic4
this.portfolioContent[1].title =this.newForm.text8
this.portfolioContent[1].src = this.newForm.pic5
this.portfolioContent[2].title =this.newForm.text9
this.portfolioContent[2].src = this.newForm.pic6
this.portfolioContent[3].title =this.newForm.text10
this.portfolioContent[3].src = this.newForm.pic7
this.portfolioContent[4].title =this.newForm.text11
this.portfolioContent[4].src = this.newForm.pic8
this.portfolioContent[5].title =this.newForm.text12
this.portfolioContent[5].src = this.newForm.pic9
      } catch (error) {
        this.error = 'Failed to fetch data: ' + error.message;
      } finally {
        this.loading = false; 
      }
    },

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
    .slick-slide {
    img {
      display: block;
      width: 100%;
    }
  }
  </style>
  