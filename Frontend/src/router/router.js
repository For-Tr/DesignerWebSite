import Vue from 'vue'
import VueRouter from 'vue-router'
import goTo from 'vuetify/es5/services/goto'

import Demo from '../views/Demo.vue'


Vue.use(VueRouter)

const routes = [{
        path: '/',
        name: 'home',
        component: Demo,
        meta: {
            title: 'Rainfo || Creative Minimal Portfolio'
        }
    },
    {
        path: '/login',
        name: 'login',
        meta: {
            title: 'Rainfo || Login'
        },
        component: () =>
            import('../views/login.vue')
    },
    {
        path: '/register',
        name: 'register',
        meta: {
            title: 'Rainfo || Register'
        },
        component: () =>
            import('../views/register.vue')
    },
    

    {
        path: '/multiscroll-portfolio',
        name: 'MultiScrollPortfolio',
        meta: {
            title: 'Rainfo || Multiscroll Portfolio'
        },
        component: () =>
            import ('../views/all-home-version/MultiScrollPortfolio.vue')
    },
   

    
    
]

const router = new VueRouter({
    mode: 'history',
    routes,
    scrollBehavior: (to, from, savedPosition) => {
        let scrollTo = 0

        if (to.hash) {
            scrollTo = to.hash
        } else if (savedPosition) {
            scrollTo = savedPosition.y
        }

        return goTo(scrollTo)
    },
})

router.beforeEach((to, from, next) => {
    document.title = to.meta.title
  
    next()

})


export default router