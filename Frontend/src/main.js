import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router/router';
import VueScrollactive from 'vue-scrollactive';
import "vue-slick-carousel/dist/vue-slick-carousel.css";
import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";
import "hooper/dist/hooper.css";
import './assets/scss/style.scss'

Vue.config.productionTip = false
Vue.use(VueScrollactive);


new Vue({
    vuetify,
    router,
    render: h => h(App),
}).$mount('#app')