<template>
  <div id="home">
    <v-navigation-drawer
      class="hidden-md-and-up custom-navigation-drawer"
      v-model="drawer"
      fixed
      dark
      right
      temporary
      width="320"
    >
    <div class="purchase-button" style="padding-left: 2vw;" v-if="hasLogin">
        <a
          @click="goProfile"
          >{{ username }}</a
        >
        <a  @click="logOut">
          logout
        </a>
      </div>
      
    <div class="purchase-button" style="padding-left: 2vw;" v-else>
        <a
          target="_blank"
          @click="goLogin"
          >Login</a
        >
      </div>
      <scrollactive
        active-class="v-btn--active"
        bezier-easing-value=".5,0,.35,1"
        :offset="116"
        :duration="1000"
      >
        <v-list flat>
          <v-list-item
            :ripple="false"
            v-for="item in items"
            :key="item.title"
            :to="item.to"
            link
            class="scrollactive-item"
          >
            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <!-- End mobile menu sidebar item list -->
        </v-list>
      </scrollactive>
      <div class="menu menu-toggle open" id="menu-toggle">
        <div class="menu-toggle-inner" @click="drawer = !drawer">
          <div class="menu-text-wrap">
            <span class="menu-text close-text">Close</span>
          </div>
          <div class="hamburger-wrap">
            <div id="hamburger">
              <span></span>
              <span></span>
              <span></span>
            </div>
          </div>
        </div>
      </div>
    </v-navigation-drawer>
    <!-- End sidebar mobile menu -->

    <v-app-bar class="header header-flat" height="116" flat>
      <router-link to="/" class="logo">
        <img src="../../assets/img/logo/logo.jpg" alt="PBuilder" style="height: 5vw;"
        />
      </router-link>
      <!-- End brand logo -->
      <v-spacer></v-spacer>
      <v-app-bar-nav-icon
        class="hidden-md-and-up"
        @click="drawer = !drawer"
      ></v-app-bar-nav-icon>
      <!-- End mobile menu icon -->
      <v-toolbar-items
        class="hidden-xs-only hidden-sm-only height-auto mainmenu-wrap"
      >
        <v-btn
          v-for="item in items"
          :key="item.title"
          :to="item.to"
          link
          :ripple="false"
          text
          class="scrollactive-item"
          >{{ item.title }}</v-btn
        >
        <div class="text-right purchase-button" v-if="hasLogin">
        <a
          target="_blank"
          @click="goProfile"
          >{{ username }}</a
        >
        <a style="margin-left: 1vw;" @click="logOut">
          logout
        </a>
      </div>
        <div class="text-right purchase-button" v-else>
        <a
          target="_blank"
          @click="goLogin"
          >Login</a
        >
      </div>
      </v-toolbar-items>
      <!-- End header menu item -->
    </v-app-bar>
    <!-- End top header navbar -->
  </div>
</template>

<script>
  import authorization from '../../utils/authorization'
  export default {
    data: () => ({
      drawer: false,
      items: [
        { title: "Home", to: "/" },
        { title: "Portfolio", to: "/portfolio" },
        { title: "Awards", to: "/awards" },
        { title: "Blog", to: "/blog" },
        { title: "Contact", to: "/contact" },
      ],
      icon: "menu",
      hasLogin: false,
      username: '',
    }),
    methods: {
      goLogin() {
        this.$router.push({name: 'login'})
      },
      goProfile() {
        this.$router.push({name: 'profile'})
      },
      logOut() {
        localStorage.clear()
        alert('Logout Successfully')
        location.reload()
      }                                                                           
    },
    mounted() {
      authorization().then((data) => [this.hasLogin, this.username] = data);
    }
  };
</script>
