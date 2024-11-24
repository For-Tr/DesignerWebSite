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

  </div>
  </template>
  
  <script>
    export default {
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
window.addEventListener('message', (event) => {
if (event.origin !== window.location.origin) return;

if (event.data.type === 'formUpdate') {
  console.log('Received data in iframe:', event.data);
  // 处理收到的数据
  this.handleFormUpdate(event.data.data);
}
});

// 通知父窗口iframe已准备就绪
window.parent.postMessage({
type: 'iframeReady'
}, '*');
},

methods: {
handleFormUpdate(data) {

Object.keys(data).forEach(key => {
    if (data[key] !== undefined) {
if (data[key] instanceof File) {
this.newForm[key] = URL.createObjectURL(data[key]); 

console.log("File object assigned:", this.newForm[key]);
} else {
this.newForm[key] = data[key];
console.log("Other type assigned:", this.newForm[key]);
}

}
});
}
}


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
  