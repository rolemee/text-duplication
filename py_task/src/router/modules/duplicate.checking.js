const Layout = () => import('@/layout/index.vue')

export default {
    path: '/duplicateChecking',
    component: Layout,
    redirect: '/duplicateChecking/list',
    name: 'duplicateChecking',
    meta: {
        title: '文件对比模块',
        icon: 'ep:document-copy'
    },
    children: [
        {
            path: 'list',
            name: 'duplicateCheckingList',
            component: () => import('@/views/duplicate_checking/index.vue'),
            meta: {
                title: '文件对比模块',
                sidebar: false,
                breadcrumb: false,
                activeMenu: '/duplicateChecking',
                cache: ['duplicateDetailMatch']
            }
        },
        {
            path: 'detail/:homeworkId/:homeworkType/:rightName/:leftName/:type',
            name: 'duplicateDetailMatch',
            component: () => import('@/views/detail_show/index.vue'),
            meta: {
                title: '查重详情',
                sidebar: false,
                activeMenu: '/duplicateChecking',
                cache: true,
                noCache: 'duplicateCheckingList'
            }
        }
    ]
}
