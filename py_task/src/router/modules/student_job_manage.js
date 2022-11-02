const Layout = () => import('@/layout/index.vue')

export default {
    path: '/student_job_manage',
    component: Layout,
    redirect: '/student_job_manage/list',
    name: 'studentJobManage',
    meta: {
        title: '学生作业管理',
        icon: 'ep:edit-pen'
    },
    children: [
        {
            path: 'list',
            name: 'studentJobManageList',
            component: () => import('@/views/student_job_manage/list.vue'),
            meta: {
                title: '学生作业管理',
                sidebar: false,
                breadcrumb: false,
                activeMenu: '/student_job_manage',
                cache: []
            }
        }
    ]
}
