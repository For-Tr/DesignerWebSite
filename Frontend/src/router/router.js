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
            title: 'PBuilder || Creative Minimal Portfolio'
        }
    },
    {
        path: '/login',
        name: 'login',
        meta: {
            title: 'PBuilder || Login'
        },
        component: () =>
            import('../views/login.vue')
    },
    {
        path: '/register',
        name: 'register',
        meta: {
            title: 'PBuilder || Register'
        },
        component: () =>
            import('../views/register.vue')
    },
    {
        path: '/password',
        name: 'password',
        meta: {
            title: 'PBuilder || Password Change'
        },
        component: () =>
            import('../views/password.vue')
    },

    {
        path: '/main-demo',
        name: 'MainDemo',
        meta: {
            title: 'PBuilder || Main Demo Portfolio'
        },
        component: () =>
            import ('../views/all-home-version/MainDemo.vue')
    },
    {
        path: '/freelancer',
        name: 'Freelancer',
        meta: {
            title: 'PBuilder || Freelancer Portfolio'
        },
        component: () =>
            import ('../views/all-home-version/Freelancer.vue')
    },
    {
        path: '/agency',
        name: 'Agency',
        meta: {
            title: 'PBuilder || Agency Portfolio'
        },
        component: () =>
            import ('../views/all-home-version/Agency.vue')
    },
    {
        path: '/minimal-agency',
        name: 'MinimalAgency',
        meta: {
            title: 'PBuilder || Minimal Agency Portfolio'
        },
        component: () =>
            import ('../views/all-home-version/MinimalAgency.vue')
    },
    {
        path: '/creative-portfolio',
        name: 'CreativePortfolio',
        meta: {
            title: 'PBuilder || Creative Portfolio'
        },
        component: () =>
            import ('../views/all-home-version/CreativePortfolio.vue')
    },
    {
        path: '/designer-portfolio',
        name: 'DesignerPortfolio',
        meta: {
            title: 'PBuilder || Designer Portfolio'
        },

        component: () =>
            import ('../views/all-home-version/DesignerPortfolio.vue')
    },
    {
        path: '/vertical-portfolio',
        name: 'VerticalPortfolio',
        meta: {
            title: 'PBuilder || Vertical Portfolio'
        },
        component: () =>
            import ('../views/all-home-version/VerticalPortfolio.vue')
    },
    {
        path: '/multiscroll-portfolio',
        name: 'MultiScrollPortfolio',
        meta: {
            title: 'PBuilder || Multiscroll Portfolio'
        },
        component: () =>
            import ('../views/all-home-version/MultiScrollPortfolio.vue')
    },
    {
        path: '/parallax-home',
        name: 'ParallaxHome',
        meta: {
            title: 'PBuilder || Parallax Portfolio'
        },
        component: () =>
            import ('../views/all-home-version/ParallaxHome.vue')
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