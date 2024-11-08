<template>
  <div>
    <HeaderThree>
      <img slot="logo" src="../assets/img/bg.jpg" />
    </HeaderThree>

    <!-- Start Bradcaump area -->
    <div class="bradcaump_area">
      <div
        class="bg-fixed bradcaump_area static-breadcaump"
        data-black-overlay="5"
        :style="{ 'background': 'url('+require('../assets/img/bg.jpg')+')'}"
      >
        <v-container>
          <v-row>
            <v-col cols="12">
              <div class="text-center bradcaump_inner">
                <h2 class="bradcaump-title">Contact</h2>
                <p>
                  Communication can make hard work to easy. We are ready 24
                  hours to help you. If you want, you can send me message
                  without any hesitation.
                </p>
              </div>
            </v-col>
          </v-row>
        </v-container>
      </div>
    </div>
    <!-- End Bradcaump area -->

    <!-- Start Contact Area -->
    <div class="rf-contact-area ">
      <div class="contact-wrapper">
        <v-row align="center">
          <v-col lg="5" md="6" sm="12" cols="12">
            <ValidationObserver v-slot="{ handleSubmit }">
              <form @submit.prevent="handleSubmit(onSubmit)">
                <div class="form-wrapper">
                  <ValidationProvider
                    name="name"
                    rules="required"
                    v-slot="{ errors }"
                  >
                    <label>
                      <input
                        type="text"
                        v-model="formData.name"
                        placeholder="Your Name *"
                      />
                      <span class="inpur-error">{{ errors[0] }}</span>
                    </label>
                  </ValidationProvider>

                  <ValidationProvider
                    name="subject"
                    rules="required"
                    v-slot="{ errors }"
                  >
                    <label>
                      <input
                        type="text"
                        v-model="formData.subject"
                        placeholder="Subject *"
                      />
                      <span class="inpur-error">{{ errors[0] }}</span>
                    </label>
                  </ValidationProvider>
                  <ValidationProvider
                    name="message"
                    rules="required"
                    v-slot="{ errors }"
                  >
                    <label>
                      <textarea
                        v-model="formData.message"
                        placeholder="Message *"
                      ></textarea>
                      <span class="inpur-error">{{ errors[0] }}</span>
                    </label>
                  </ValidationProvider>
                  <button type="submit">
                    <span>Submit</span>
                    <svg
                      fill="#000"
                      width="25"
                      height="8"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <path
                        d="M44.102 4l-2.444-2.445.009-1.405 4.325 4.325-4.38 4.38.01-1.423L44.101 5H.002V4z"
                        fill-rule="evenodd"
                      ></path>
                    </svg>
                  </button>
                </div>
              </form>
            </ValidationObserver>
            <div class="form-output">
              <p class="form-messege-active"></p>
            </div>
          </v-col>
          <v-col lg="7" md="6" sm="12" cols="12">
            <div class="contact-address">
              <h2 class="heading-title">Address</h2>
              <div
                class="address"
                v-for="(address, i) in addressContent"
                :key="i"
              >
                <i class="icon" v-html="iconSvg(address.icon)"></i>
                <div class="content">
                  <p v-if="address.isAddress">
                    {{ address.desc1 }} <br />
                    {{ address.desc2 }}
                  </p>
                  <p v-if="address.isNumber">
                    <a :href="address.to">{{ address.num1 }}</a>
                  </p>
                  <p v-if="address.isNumber">
                    <a :href="address.to">{{ address.num2 }}</a>
                  </p>
                  <p v-if="address.isMail">
                    <a :href="`mailto:${address.to}`">{{ address.mail }}</a>
                  </p>
                </div>
              </div>
            </div>
          </v-col>
        </v-row>
      </div>
    </div>
    <!-- End Contact Area -->


  </div>
</template>

<script>
  import feather from "feather-icons";
import authorization from "../utils/authorization"

  import { ValidationObserver } from "vee-validate";
  import { ValidationProvider } from "vee-validate/dist/vee-validate.full.esm";
import HeaderThree from "../components/header/HeaderThree.vue";
  export default {
    components: {
      HeaderThree,
      ValidationObserver,
      ValidationProvider,
    },
    data() {
      return {
        auth_email: null,

        formData: {
          name: "",
          email: "",
          subject: "",
          message: "",
          auth_email: "",
        },
        addressContent: [
          {
            icon: "map-pin",
            desc1: "500 South Main Street",
            desc2: " Bishop, CA 93514 93514",
            isAddress: true,
          },
          {
            icon: "smartphone",
            num1: "+012 3344 556677",
            num2: "+012 3344 556677",
            to: "tel:0123344556677",
            isNumber: true,
          },
          {
            icon: "mail",
            mail: "example@gmail.com",
            to: "mailto:example@domain.com",
            isMail: true,
          },
        ],
      };
    },
    mounted() {
        this.auth_email = this.$route.params.Email
        console.log('222' + this.auth_email)
        this.formData.email = localStorage.getItem('email')
    },
    methods: {
      iconSvg(icon) {
        return feather.icons[icon].toSvg();
      },
      async onSubmit() {
        authorization().then((response) => {
          if (response[0]) {
        try {
      const token = localStorage.getItem('access')
          if (this.auth_email) {
            this.formData.auth_email = this.auth_email;

          } else {
          this.formData.auth_email = 'liuyang5407@163.com'
          }
          console.log(this.formData)
          const response = fetch('/api/notes/contact', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              Authorization: 'Bearer ' + token
            },
            body: JSON.stringify(this.formData)
          });

            console.log(response)
          
            alert('Your message has been sent successfully!')


        } catch (error) {
          console.error('Error:', error);
          
            alert('Failed to send message. Please try again later.')
        }}else {
        alert('Auth information out of date,login again')
      }
      })
      }
    },
  };
</script>

<style lang="scss" scoped>
  .inpur-error,
  .inpur-success {
    display: block;
    margin-top: 5px;
    font-size: 14px;
  }
  .inpur-error {
    color: #f10;
  }
  .gmap_canvas {
    overflow: hidden;
    background: none !important;
    height: 800px;
    width: 100%;

    iframe {
      width: 100%;
      height: 100%;
    }
  }
  .mapouter {
    position: relative;
    width: 100%;
    height: 100%;
  }
</style>
