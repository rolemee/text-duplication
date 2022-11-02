const Layout = () => import('@/layout/index.vue')

export default {
    path: '/job_manage',
    component: Layout,
    redirect: '/job_manage/list',
    name: 'jobManage',
    meta: {
        title: '作业管理',
        icon: 'ep:edit-pen'
    },
    children: [
        {
            path: 'list',
            name: 'jobManageList',
            component: () => import('@/views/job_manage/list.vue'),
            meta: {
                title: '作业管理',
                sidebar: false,
                breadcrumb: false,
                activeMenu: '/job_manage',
                cache: []
            }
        }
    ]
}
