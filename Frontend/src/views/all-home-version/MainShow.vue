<template>
    <div class="main-demo-page">

      <!-- End Header One Area -->
  
      <!-- Start Slider Area -->
      <div class="rv-slider-wrapper black-pagination pagination-bottom" id="home">
        <div class="slider-wrapper default-home-slider">
    <VueSlickCarousel v-bind="settings" class="slider-activation-with-slick">
      <div
        class="slide slider-container"
        v-for="(slider, i) in sliderContent"
        :key="i"
      >
        <div class="slider-inner">
          <div class="slide-content txt">
            <div class="txt-wrapper">
              <span class="copy">{{ slider.info }}</span>
              <h2 class="copy2">{{ slider.title }}</h2>
              <p class="excerpt copy3">{{ slider.desc }}</p>
            </div>
          </div>

          <div class="slide-content img">
            <img :src="slider.src" alt="personal portfolio" />
          </div>
        </div>
      </div>
    </VueSlickCarousel>
  </div>
      </div>
      <!-- End Slider Area -->
  
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
  // import Social from "../social/Social";
  export default {
    components: { VueSlickCarousel, HeaderShow },
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
    text15: null
  }
      return {
        newForm: newForm,
        sliderContent: [
          {
            src: require("../../assets/img/slider/slider-1.jpg"),
            info: "Hello!",
            title: "I’m Ms. Rainfo",
            desc: `There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form.`,

          },
          {
            src: require("../../assets/img/slider/slider-2.jpg"),
            info: "What I Do!",
            title: "Development",
            desc: `There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form.`,
         
          },
          {
            src: require("../../assets/img/slider/slider-3.jpg"),
            info: "What I Do!",
            title: "UX Research",
            desc: `There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form.`,
          
          },
          {
            src: require("../../assets/img/slider/slider-4.jpg"),
            info: "What I Do!",
            title: "Visual Design",
            desc: `There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form.`,
          
          },
          {
            src: require("../../assets/img/slider/slider-5.jpg"),
            info: "What I Do!",
            title: "Development",
            desc: `There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form.`,
           
          },
        ],
        settings: {
          fade: true,
          dots: true,
          arrows: false,
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
       
        this.sliderContent[0].info = this.newForm.text1
this.sliderContent[0].title = this.newForm.text2
        this.sliderContent[0].desc = this.newForm.text3
        this.sliderContent[0].src = this.newForm.pic1
        this.sliderContent[1].info = this.newForm.text4
        this.sliderContent[1].title = this.newForm.text5
        this.sliderContent[1].desc = this.newForm.text6
        this.sliderContent[1].src = this.newForm.pic2
        this.sliderContent[2].info = this.newForm.text7
        this.sliderContent[2].title = this.newForm.text8
        this.sliderContent[2].desc = this.newForm.text9
        this.sliderContent[2].src = this.newForm.pic3
        this.sliderContent[3].info = this.newForm.text10
        this.sliderContent[3].title = this.newForm.text11
        this.sliderContent[3].desc = this.newForm.text12
        this.sliderContent[3].src = this.newForm.pic4
        this.sliderContent[4].info = this.newForm.text13
        this.sliderContent[4].title = this.newForm.text14
        this.sliderContent[4].desc = this.newForm.text15
        this.sliderContent[4].src = this.newForm.pic5
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
  .main-demo-page {
    @media only screen and (max-width: 767px) {
      .rn-skill-right {
        order: 2;
      }
      .rn-story-area {
        margin-top: -8px;
      }
    }
  }
</style>
