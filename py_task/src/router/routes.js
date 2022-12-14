import pinia from '@/store'
import useSettingsStore from '@/store/modules/settings'

// 固定路由（默认路由）
let constantRoutes = [
    {
        path: '/',
        redirect: '/dashboard'
    },
    {
        path: '/login',
        name: 'login',
        component: () => import('@/views/login.vue'),
        meta: {
            title: '登录'
        }
    },
    {
        path: '/:all(.*)*',
        name: 'notFound',
        component: () => import('@/views/[...all].vue'),
        meta: {
            title: '找不到页面'
        }
    }
]

// 系统路由
let systemRoutes = [
    {
        path: '/dashboard',
        component: () => import('@/layout/index.vue'),
        meta: {
            title: () => {
                return useSettingsStore().dashboard.title
            },
            breadcrumb: false
        },
        children: [
            {
                path: '',
                name: 'dashboard',
                component: () => import('@/views/index.vue'),
                meta: {
                    title: () => {
                        return useSettingsStore().dashboard.title
                    },
                    breadcrumb: false
                }
            }
        ]
    },
    {
        path: '/personal',
        component: () => import('@/layout/index.vue'),
        redirect: '/personal/setting',
        meta: {
            title: '个人中心',
            breadcrumb: false
        },
        children: [
            {
                path: 'setting',
                name: 'personalSetting',
                component: () => import('@/views/personal/setting.vue'),
                meta: {
                    title: '个人设置',
                    cache: 'personalEditPassword'
                },
                children: [
                    {
                        path: 'edit/password',
                        name: 'personalEditPassword',
                        component: () => import('@/views/personal/edit.password.vue'),
                        meta: {
                            title: '修改密码',
                            cache: true,
                            noCache: 'personalSetting'
                        }
                    },
                    {
                        path: 'edit/email',
                        name: 'personalEditEmail',
                        component: () => import('@/views/personal/edit.email.vue'),
                        meta: {
                            title: '修改邮箱',
                            cache: true,
                            noCache: 'personalSetting'
                        }
                    }
                ]
            }
        ]
    },
    {
        path: '/reload',
        component: () => import('@/layout/index.vue'),
        meta: {
            title: '重新加载',
            breadcrumb: false
        },
        children: [
            {
                path: '',
                name: 'reload',
                component: () => import('@/views/reload.vue'),
                meta: {
                    title: '重新加载',
                    breadcrumb: false
                }
            }
        ]
    }
]

import JobManage from './modules/job.manage'
import StudentJobManage from './modules/student.job.manage'
import DuplicateChecking from './modules/duplicate.checking'
// 动态路由（异步路由、导航栏路由）
let asyncRoutes = [
    {
        meta: {
            title: '作业管理',
            icon: 'ep:compass',
            auth: [0]
        },
        children: [
            JobManage
        ]
    },
    {
        meta: {
            title: '学生作业管理',
            icon: 'ep:compass',
            auth: [1]
        },
        children: [
            StudentJobManage
        ]
    },
    {
        meta: {
            title: '文件查重模块',
            auth: [1]
        },
        children: [
            DuplicateChecking
        ]
    }
]


export {
    constantRoutes,
    systemRoutes,
    asyncRoutes
}
