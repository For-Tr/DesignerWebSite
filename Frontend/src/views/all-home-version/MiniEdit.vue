<template>
    <div class="box-layout">
        <HeaderEdit>
  
</HeaderEdit>
<div>
    <div
      class="slider slider--3 ptb--200 pl--150 rfanimation-style--2"
      v-for="(slider, i) in sliderContent"
      :key="i"
      :class="slider.imgClass"
    >                <v-file-input style="padding-top: 30vw;"
                    accept="image/png, image/jpeg, image/bmp"
                    label="UPLOAD HERE"
                    placeholder="Pick a picture of your works"
                    @change="(file) => {beforeUpload(file, 'pic1')}"
                ></v-file-input>
      <v-container>
        <v-row>
          <v-col cols="12">
            <div class="content">

              <h3 class="heading-title">{{ slider.subTitle }}</h3>
              <input type="text" v-model="form.text1" placeholder="Enter words like text1" maxlength="20" class="input-dom">

              <h1>{{ slider.title }}</h1>
              <input type="text" v-model="form.text2" placeholder="Enter words like text2" maxlength="20" class="input-dom">

              <p class="description">
                {{ slider.desc }}
              </p>
              <input type="text" v-model="form.text3" placeholder="Enter words like text3" maxlength="20" class="input-dom">

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
        :style="{ backgroundImage: 'url(' + aboutSrc + ')' }"
      >
      <v-file-input style="padding-top: 30vw;"
                    accept="image/png, image/jpeg, image/bmp"
                    label="UPLOAD HERE"
                    placeholder="Pick a picture of your works"
                   @change="(file) => {beforeUpload(file, 'pic2')}"
                ></v-file-input>
    </div>
      <div class="rn-story-right w-50 d-flex align-items-center">
        <div
          class="story-style--3 story-content text-left rn-plr--160 section-ptb-xl"
        >
          <div class="content text-left">
            <h2>
              Text4
            </h2>
            <input type="text" v-model="form.text4" placeholder="Enter words like text4" maxlength="20" class="input-dom">

            <p>
              Text5
            </p>
            <input type="text" v-model="form.text5" placeholder="Enter words like text5" maxlength="20" class="input-dom">

            <p>
              Text6
            </p>
            <input type="text" v-model="form.text6" placeholder="Enter words like text6" maxlength="20" class="input-dom">

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
                <v-file-input style="padding-top: 30vw;"
                    accept="image/png, image/jpeg, image/bmp"
                    label="UPLOAD HERE"
                    placeholder="Pick a picture of your works"
                   @change="(file) => {beforeUpload(file, 'pic3')}"
                ></v-file-input>
    <!-- Start Single Progress Bar -->
    <div class="progress_wrapper">
      <h2 class="section-title text-left">My Skill</h2>
      <div class="single-skill">
        <p>Skill1</p>
        <input type="text" v-model="form.text7" placeholder="Enter skill" maxlength="20" class="input-dom">

        <div
          class="progress progress-height-6 progress-bar-bg--1 progress-label-top"
        >
          <div
            class="progress-bar wow fadeInLeft progress-bar-bg--1"
            role="progressbar"
            style="width: 100%;"
            aria-valuenow="100"
            aria-valuemin="0"
            aria-valuemax="100"
          >
            <span class="percent-label">100%</span>
          </div>
        </div>
      </div>

      <div class="single-skill">
        <p>Skill2</p>
        <input type="text" v-model="form.text8" placeholder="Enter skill" maxlength="20" class="input-dom">

        <div
          class="progress progress-height-6 progress-bar-bg--1 progress-label-top"
        >
          <div
            class="progress-bar wow fadeInLeft progress-bar-bg--1"
            role="progressbar"
            style="width: 80%;"
            aria-valuenow="80"
            aria-valuemin="0"
            aria-valuemax="100"
          >
            <span class="percent-label">80%</span>
          </div>
        </div>
      </div>

      <div class="single-skill">
        <p>Skill3</p>
        <input type="text" v-model="form.text9" placeholder="Enter skill" maxlength="20" class="input-dom">

        <div
          class="progress progress-height-6 progress-bar-bg--1 progress-label-top"
        >
          <div
            class="progress-bar wow fadeInLeft progress-bar-bg--1"
            role="progressbar"
            style="width: 90%;"
            aria-valuenow="90"
            aria-valuemin="0"
            aria-valuemax="100"
          >
            <span class="percent-label">90%</span>
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
        :style="{ backgroundImage: 'url(' + skillSrc + ')' }"
      ></div>
    </div>
    <!-- End Skill Area -->
  </div>
      </div>
      <!-- End Story Area -->

  
    </div>
  </template>
  
  <script>
import HeaderEdit from "../../components/header/HeaderEdit";
import { useFormStore } from '../../stores/formStore.js';

    export default {
      components: {
        HeaderEdit,
      },
      data() {
        const formStore = useFormStore();
        return {
          aboutSrc: require("../../assets/img/portfolio/about-image.jpg"),
          skillSrc: require("../../assets/img/portfolio/my-skill.jpg"),
          formStore,
          form: formStore.form,
          sliderContent: [
          {
            imgClass: "bg_image--8",
            title: "Text2",
            subTitle: "Text1",
            desc: `Text3`,
          },
        ],
        };
      },
      mounted() {
    this.form.temp = 'Mini'
  },
  methods: {
    beforeUpload(file, picname) {
      const fileName = new Date().getTime().toString() + '.' + file.type.substring(6);
      const copyFile = new File([file], fileName);
      this.$pinia.use(() => ({
        formStore: useFormStore(),
      }));
      this.formStore.updatePicField(picname, copyFile);
      console.log(this.formStore)
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
  