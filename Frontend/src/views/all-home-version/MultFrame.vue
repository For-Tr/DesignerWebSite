<template>
    <div>

  
      <hooper :settings="settings" class="multiscroll-slider-wrapper">
        <slide>
            <div class="ms-container-wrapper">
      <div class="ms-left">
        <div
          class="ms-section bg_image "
          :style="{ backgroundImage: 'url(' + src + ')' }"
        >
    

        </div>
      </div>
      <div class="ms-right">
        <div class="ms-section ms-table">
          <div class="slipt-content-inner ms-tableCell slider rn-plr rn-ptb-100">
            <div class="content">
                <span>Text 1</span>
              <h2>Text 2</h2>
              <p>Text 3</p>
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
        :style="{ backgroundImage: 'url(' + src + ')' }"
      >
    
      
    </div>
    </div>
    <div class="ms-right">
      <div class="ms-section ms-table">
        <div class="slipt-content-inner ms-tableCell rn-plr rn-ptb-100">
          <div class="story-content">
            <div class="text-left content">
                <h2>Text 4</h2>
              <p>Text 5</p>
   
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
          :style="{ backgroundImage: 'url(' + src + ')' }"
        >

        </div>
      </div>
      <div class="ms-right">
        <div class="ms-section ms-table">
          <div class="slipt-content-inner ms-tableCell slider rn-plr rn-ptb-100">
            <div class="content">
                <span>Text 6</span>
              <h2>Text 7</h2>
              <p>Text 8</p>
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
          :style="{ backgroundImage: 'url(' + src + ')' }"
        >
    

        </div>
      </div>
      <div class="ms-right">
        <div class="ms-section ms-table">
          <div class="slipt-content-inner ms-tableCell slider rn-plr rn-ptb-100">
            <div class="content">
                <span>Text 9</span>
              <h2>Text 10</h2>
              <p>Text 11</p>
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
          :style="{ backgroundImage: 'url(' + src + ')' }"
        >

        </div>
      </div>
      <div class="ms-right">
        <div class="ms-section ms-table">
          <div class="slipt-content-inner ms-tableCell slider rn-plr rn-ptb-100">
            <div class="content">
                <span>Text 12</span>
              <h2>Text 13</h2>
              <p>Text 14</p>
            </div>
          </div>
        </div>
      </div>
    </div>
        </slide>

        <hooper-pagination slot="hooper-addons"></hooper-pagination>
      </hooper>
      <!-- End hooper slider content -->
    </div>
  </template>
  
  <script>
import { Hooper, Slide, Pagination as HooperPagination } from "hooper";
import { useFormStore } from '../../stores/formStore.js';

export default {
  components: {
    Hooper,
    Slide,
    HooperPagination,
  },
  data() {
    const formStore = useFormStore();
    return {
      formStore,
      form: formStore.form,
      settings: {
        vertical: true,
        mouseDrag: false,
        infiniteScroll: true,
        transition: 800,
      },
      src: require("../../assets/img/slider/slider-6.jpg"),


    };
  },
  mounted() {
    this.form.temp = 'Mult'
  },
  methods: {
    beforeUpload(file, picname) {
      const fileName = new Date().getTime().toString() + '.' + file.type.substring(6);
      const copyFile = new File([file], fileName);
      this.$pinia.use(() => ({
        formStore: useFormStore(),
      }));
      this.formStore.updatePicField(picname, copyFile);
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
  