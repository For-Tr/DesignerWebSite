<template>
    <div>

  
      <hooper :settings="settings" class="multiscroll-slider-wrapper">
        <slide>
            <div class="ms-container-wrapper">
      <div class="ms-left">
        <div
          class="ms-section bg_image "
          :style="{ backgroundImage: 'url(' + newForm.pic1 + ')' }" 
        >

        </div>

      </div>
      <div class="ms-right">
        <div class="ms-section ms-table">
          <div class="slipt-content-inner ms-tableCell slider rn-plr rn-ptb-100">
            <div class="content">
                <span>{{ newForm.text1 }}</span>
              <h2>{{ newForm.text2 }}</h2>
              <p>{{ newForm.text3 }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
        </slide>
        <slide>
            <div class="ms-container-wrapper">
    <div class="ms-left">
      <div
        class="ms-section bg_image "
        :style="{ backgroundImage: 'url(' + newForm.pic2 + ')' }"
      >
    

    </div>
    </div>
    <div class="ms-right">
      <div class="ms-section ms-table">
        <div class="slipt-content-inner ms-tableCell rn-plr rn-ptb-100">
          <div class="story-content">
            <div class="text-left content">
                <h2>{{ newForm.text4 }}</h2>
              <p>{{ newForm.text5 }}</p>
   
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
        </slide>
        <slide>
            <div class="ms-container-wrapper">
      <div class="ms-left">
        <div
          class="ms-section bg_image "
          :style="{ backgroundImage: 'url(' + newForm.pic3 + ')' }"
        >

        </div>
      </div>
      <div class="ms-right">
        <div class="ms-section ms-table">
          <div class="slipt-content-inner ms-tableCell slider rn-plr rn-ptb-100">
            <div class="content">
                <span>{{ newForm.text6 }}</span>
              <h2>{{ newForm.text7 }}</h2>
              <p>{{ newForm.text8 }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
        </slide>
        <slide>
            <div class="ms-container-wrapper">
      <div class="ms-left">
        <div
          class="ms-section bg_image "
          :style="{ backgroundImage: 'url(' + newForm.pic4 + ')' }"
        >
    

        </div>
      </div>
      <div class="ms-right">
        <div class="ms-section ms-table">
          <div class="slipt-content-inner ms-tableCell slider rn-plr rn-ptb-100">
            <div class="content">
                <span>{{ newForm.text9 }}</span>
              <h2>{{ newForm.text10 }}</h2>
              <p>{{ newForm.text11 }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
        </slide>
        <slide>
            <div class="ms-container-wrapper">
      <div class="ms-left">
        <div
          class="ms-section bg_image "
          :style="{ backgroundImage: 'url(' + newForm.pic5 + ')' }"
        >
    

        </div>
      </div>
      <div class="ms-right">
        <div class="ms-section ms-table">
          <div class="slipt-content-inner ms-tableCell slider rn-plr rn-ptb-100">
            <div class="content">
                <span>{{ newForm.text12 }}</span>
              <h2>{{ newForm.text13 }}</h2>
              <p>{{ newForm.text14 }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
        </slide>

        <hooper-pagination slot="hooper-addons"></hooper-pagination>
      </hooper>
      <!-- End hooper slider content -->
       <div style="display: flex; justify-content: center;">
      <HeaderShow :Email="Email"></HeaderShow>

       </div>
    </div>
  </template>
  
  <script>

import { Hooper, Slide, Pagination as HooperPagination } from "hooper";
import axios from 'axios';
import {BASE_URL} from "../../utils/BASE"
import HeaderShow from "../../components/header/HeaderShow.vue";
export default {
  components: {
    Hooper,
    Slide,
    HooperPagination,
    HeaderShow
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
      error: null
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
        
      } catch (error) {
        this.error = 'Failed to fetch data: ' + error.message;
      } finally {
        this.loading = false; 
      }
    },

  },
};
</script>
  
  <style lang="scss">
    .ms-right,
    .ms-section.ms-table,
    .ms-tableCell {
      height: 100%;
    }
    .ms-section.ms-table {
      display: table;
      width: 100%;
    }
    .ms-tableCell {
      display: table-cell;
      vertical-align: middle;
      width: 100%;
    }
    .ms-container-wrapper {
      display: flex;
      height: 100vh;
  
      .ms-left {
        flex: 0 0 50%;
        max-width: 50%;
        @media only screen and (max-width: 1199px) {
          flex: 0 0 100%;
          max-width: 100%;
        }
      }
      .ms-right {
        flex: 0 0 50%;
        max-width: 50%;
        @media only screen and (max-width: 1199px) {
          flex: 0 0 100%;
          max-width: 100%;
          position: absolute;
          width: 100%;
          height: 100vh;
          background: rgba(255, 255, 255, 0.6);
        }
      }
      .ms-section {
        height: 100%;
      }
    }
    .multiscroll-slider-wrapper.hooper {
      @media only screen and (max-width: 767px) {
        .hooper-indicators {
          display: none;
        }
      }
      .hooper-pagination.is-vertical {
        @media only screen and (max-width: 1199px) {
          right: 15px;
          padding: 0;
        }
      }
    }
    .multiscroll-slider-wrapper
      .hooper-pagination.is-vertical
      .hooper-indicator::after,
    .multiscroll-slider-wrapper .hooper-pagination.is-vertical .hooper-indicator {
      transition: all 0.5s ease-in-out;
    }
  </style>
  