<template>
  <div>
      <hooper :settings="settings" class="multiscroll-slider-wrapper">
          <slide v-for="index in 5" :key="index">
              <div class="ms-container-wrapper">
                  <div class="ms-left">
                      <div class="ms-section">
                          <!-- 根据媒体类型显示图片或视频 -->
                          <template v-if="mediaData[index] && mediaData[index].type === 'video'">
                              <video 
                                  :src="mediaData[index].url"
                                  class="video-player"
                                  controls
                                  autoplay
                                  loop
                                  muted
                                  style="width: 100%; height: 100%; object-fit: cover;"
                              ></video>
                          </template>
                          <template v-else>
                            <div
                              class="ms-section bg_image "
                              :style="{ backgroundImage: 'url(' + newForm['pic' + index] + ')' }"
                            ></div>
                          </template>
                      </div>
                  </div>
                  <div class="ms-right">
                      <div class="ms-section ms-table">
                          <div class="slipt-content-inner ms-tableCell slider rn-plr rn-ptb-100">
                              <div class="content">
                                  <span>{{ newForm['text' + ((index-1)*3 + 1)] }}</span>
                                  <h2>{{ newForm['text' + ((index-1)*3 + 2)] }}</h2>
                                  <p>{{ newForm['text' + ((index-1)*3 + 3)] }}</p>
                              </div>
                          </div>
                      </div>
                  </div>
              </div>
          </slide>
          <hooper-pagination slot="hooper-addons"></hooper-pagination>
      </hooper>
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
            mediaData: {}, // 新增：存储媒体数据
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
    methods: {
      getImageUrl(index) {
      if (this.mediaData[index] && this.mediaData[index].type === 'image') {
        return this.mediaData[index].url;
      }
      return this.newForm[`pic${index}`] || '';
    },
        async fetchData() {
            if (!this.id) {
                this.error = 'No ID provided';
                alert(this.error);
                return;
            }

            this.loading = true;

            try {
                const response = await axios.get(`/api/notes/${this.id}`);
                
                // 处理图片和视频数据
                response.data.pic.forEach(item => {
                    const orderNum = item.order_num;
                    if (item.media_type === 'video') {
                        this.mediaData[orderNum] = {
                            type: 'video',
                            url: BASE_URL + item.video
                        };
                    } else {
                        this.mediaData[orderNum] = {
                            type: 'image',
                            url: BASE_URL + item.pic
                        };
                        const key = `pic${item.order_num}`;
                        this.newForm[key] = BASE_URL + item.pic;
                    }
                    console.log(this.newForm)
                });

                this.Email = response.data.user.email;
                
                // 处理文本数据
                response.data.text.forEach(item => {
                    const key = `text${item.order_num}`;
                    this.newForm[key] = item.text;
                });
                console.log(this.newForm)

            } catch (error) {
                this.error = 'Failed to fetch data: ' + error.message;
            } finally {
                this.loading = false;
            }
        },
    },
    mounted() {
        this.id = this.$route.query.id;
        this.fetchData();
    }
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
  