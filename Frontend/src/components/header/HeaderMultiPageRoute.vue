<template>
  <div>
    <v-app-bar class="header header-flat" height="90" flat>

        <div class="purchase-button" style="padding-right: 6vw;">
        <a
          target="_blank"
          @click="handleBack"
          >BACK</a
        >
      </div>
      <h1 style="padding-right: 6vw;">What About This Template?</h1>
      <div class="purchase-button">
        <a
          target="_blank"
          @click="goNext"
          >Use this</a
        >
      </div>

      
      </v-app-bar>
  </div>
  
</template>

<script>


  export default {
    data: () => ({
      drawer: false,
      items: [
        { title: "home", to: "/" },
        { title: "about us", to: "/about-us" },
        { title: "best services", to: "/service" },
        { title: "awesome works", to: "/portfolio" },
        { title: "our awards", to: "/awards" },
        { title: "latest post", to: "/blog" },
        { title: "contact us", to: "/contact" },
      ],
      active: false,
    }),
    methods: {
      handleBack() {
        this.$router.push({name: 'home'})
      },
      goNext() {
        alert(111)
      }
    },
  };
</script>


<style scoped> 
.header { 
  display: flex; 
  justify-content: space-between; 
  align-items: center; 
} 
.purchase-button { 
  margin: 0 10px; 
  } 
</style>
