<template>
    <div class="box-layout">

<div>
    <div
      class="slider slider--3 ptb--200 pl--150 rfanimation-style--2"
      v-for="(slider, i) in sliderContent"
      :key="i"
      :style="{ backgroundImage: 'url(' + newForm.pic1 + ')' }" 
      >

      <v-container>
        <v-row>
          <v-col cols="12">
            <div class="content">

              <h3 class="heading-title">{{ slider.subTitle }}</h3>

              <h1>{{ slider.title }}</h1>

              <p class="description">
                {{ slider.desc }}
              </p>

            </div>
          </v-col>
        </v-row>
      </v-container>
    </div>
    <!-- End Single Slide  -->
  </div>
  
      <div class="mt--100 mt-sm-10">
        <div class="about-page">
    <div class="rn-story-area d-flex bg_color--3" id="about">
      <div
        class="rn-story-left w-50 rn-story-bg-wrapper"
        :style="{ backgroundImage: 'url(' + newForm.pic2 + ')' }"
      >

    </div>
      <div class="rn-story-right w-50 d-flex align-items-center">
        <div
          class="story-style--3 story-content text-left rn-plr--160 section-ptb-xl"
        >
          <div class="content text-left">
            <h2>
              {{ newForm.text4 }}
            </h2>

            <p>
                {{ newForm.text5 }}
            </p>

            <p>
                {{ newForm.text6 }}
            </p>

            <div
              class="story-btn  wow newFadeInUp"
              data-wow-duration="1s"
              data-wow-delay="1000ms"
            >
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- End Story Area -->
    <!-- Start Skill Area -->
    <div class="rn-skill-area home-one-skill d-flex bg_color--3" id="skill">
        
      <div class="rn-skill-right w-50 d-flex align-items-center">
        <div class="text-left rn-skill rn-plr section-ptb-xl">
            <div class="content">

   <!-- Start Single Progress Bar -->
   <div class="progress_wrapper">
      <h2 class="section-title text-left">My Skill</h2>
      <div class="single-skill">
        <p>{{ newForm.text7 }}</p>

        <div
          class="progress progress-height-6 progress-bar-bg--1 progress-label-top"
        >
          <div
            class="progress-bar wow fadeInLeft progress-bar-bg--1"
            role="progressbar"
             :style="{ width: newForm.text10 + '%' }"
            aria-valuenow="100"
            aria-valuemin="0"
            aria-valuemax="100"
          >
            <span class="percent-label">{{ newForm.text10 }}%</span>
          </div>
        </div>
      </div>

      <div class="single-skill">
        <p>{{ newForm.text8 }}</p>

        <div
          class="progress progress-height-6 progress-bar-bg--1 progress-label-top"
        >
          <div
            class="progress-bar wow fadeInLeft progress-bar-bg--1"
            role="progressbar"
           :style="{ width: newForm.text11 + '%' }"
            aria-valuenow="80"
            aria-valuemin="0"
            aria-valuemax="100"
          >
            <span class="percent-label">{{ newForm.text11 }}%</span>
          </div>
        </div>
      </div>

      <div class="single-skill">
        <p>{{ newForm.text9 }}</p>

        <div
          class="progress progress-height-6 progress-bar-bg--1 progress-label-top"
        >
          <div
            class="progress-bar wow fadeInLeft progress-bar-bg--1"
            role="progressbar"
            :style="{ width: newForm.text12 + '%' }"
            aria-valuenow="90"
            aria-valuemin="0"
            aria-valuemax="100"
          >
            <span class="percent-label">{{ newForm.text12 }}%</span>
          </div>
        </div>
      </div>
    </div>
    <!-- End Single Progress Bar -->
  </div>
        </div>
      </div>
      <div
        class="rn-skill-left w-50 rn-skill-bg-wrapper"
        :style="{ backgroundImage: 'url(' + newForm.pic3 + ')' }"
      ></div>
    </div>
    <!-- End Skill Area -->
  </div>
      </div>
      <!-- End Story Area -->
<div style="display: flex; justify-content: center;">
  <HeaderShow :Email="Email"></HeaderShow>

</div>
    </div>
    
  </template>
  
  <script>

import axios from 'axios';
import {BASE_URL} from "../../utils/BASE"
import HeaderShow from "../../components/header/HeaderShow.vue";

    export default {
      components: {
        HeaderShow,
      },
      data() {
        return {
            newForm: {
        pic1: require("../../assets/img/slider/slider-6.jpg"),
        pic2: require("../../assets/img/slider/slider-6.jpg"),
        pic3: require("../../assets/img/slider/slider-6.jpg"),
        pic4: require("../../assets/img/slider/slider-6.jpg"),
        pic5: require("../../assets/img/slider/slider-6.jpg"),
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

      },
      settings: {
        vertical: true,
        mouseDrag: false,
        infiniteScroll: true,
        transition: 800,
      },
      Email: null,
      loading: false,
      id: null,
      error: null,
          sliderContent: [
          {
            imgClass: "bg_image--8",
            title: "",
            subTitle: "",
            desc: "",
          },
        ],
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
        this.sliderContent[0].title = this.newForm.text2
        this.sliderContent[0].subTitle = this.newForm.text1
        this.sliderContent[0].desc = this.newForm.text3
        
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
  