<template>
    <div class="parallax-home-page">
  
  
      <!-- Start Hero Area -->
      <div
        class="slider-area paralx-slider parallax fullscreen d-flex align-center rn-bg-position-fixed"
        :style="{ backgroundImage: 'url(' + newForm.pic1 + ')' }"
      >
        <v-container>
          <v-row class="row">
            <v-col lg="12">
              <div class="text-center content">
                <h2>{{ newForm.text1 }}</h2>
                <p>
                  {{ newForm.text2 }}
                </p>
                <router-link class="mt--30 rf_btn" to="/contact"
                  >Contact Us</router-link
                >
              </div>
            </v-col>
          </v-row>
        </v-container>
      </div>
      <!-- End Hero Area -->
  
      <!-- Start Hero Area -->
      <div
        class="slider-area paralx-slider parallax fullscreen d-flex align-center rn-bg-position-fixed"
        :style="{ backgroundImage: 'url(' + newForm.pic2 + ')' }"
      >
        <v-container>
          <v-row class="row">
            <v-col lg="12">
              <div class="text-center content">
                <h2>{{ newForm.text3 }}</h2>
                <p>
                  {{ newForm.text4 }}
                </p>
                <router-link class="mt--30 rf_btn" to="/contact"
                  >Contact Us</router-link
                >
              </div>
            </v-col>
          </v-row>
        </v-container>
      </div>
      <!-- End Hero Area -->
  
      <!-- Start Hero Area -->
      <div
        class="slider-area paralx-slider parallax fullscreen d-flex align-center rn-bg-position-fixed"
        :style="{ backgroundImage: 'url(' + newForm.pic3 + ')' }"
      >
        <v-container>
          <v-row class="row">
            <v-col lg="12">
              <div class="text-center content">
                <h2>{{ newForm.text5 }}</h2>
                <p>
                  {{ newForm.text6 }}
                </p>
                <router-link class="mt--30 rf_btn" to="/contact"
                  >Contact Us</router-link
                >
              </div>
            </v-col>
          </v-row>
        </v-container>
      </div>
      <!-- End Hero Area -->
  
      <!-- Start Hero Area -->
      <div
        class="slider-area paralx-slider parallax fullscreen d-flex align-center rn-bg-position-fixed"
        :style="{ backgroundImage: 'url(' + newForm.pic4 + ')' }"
      >
        <v-container>
          <v-row class="row">
            <v-col lg="12">
              <div class="text-center content">
                <h2>{{ newForm.text7 }}</h2>
                <p>
                  {{ newForm.text8 }}
                </p>
                <router-link class="mt--30 rf_btn" to="/contact"
                  >Contact Us</router-link
                >
              </div>
            </v-col>
          </v-row>
        </v-container>
      </div>
      <!-- End Hero Area -->
      <div style="display: flex; justify-content: center;">
      <HeaderShow :Email="Email"></HeaderShow>

       </div>
    </div>
    </template>
  
  <script>
    import axios from 'axios';
import {BASE_URL} from "../../utils/BASE"
import HeaderShow from '../../components/header/HeaderShow.vue';
    export default {
      components : {
HeaderShow
      },
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
  