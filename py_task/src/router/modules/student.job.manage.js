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
                cache: ['taskManageList', 'detailMatch']
            }
        },
        {
            path: 'task/:workId',
            name: 'taskManageList',
            component: () => import('@/views/comparative_table/detail.vue'),
            meta: {
                title: '学生作业查重率',
                sidebar: false,
                breadcrumb: true,
                activeMenu: '/student_job_manage',
                cache: true,
                noCache: 'studentJobManageList'
            },
            children: [
                {
                    path: 'detail/:homeworkId/:id',
                    name: 'detailMatch',
                    component: () => import('@/views/detail_show/index.vue'),
                    meta: {
                        title: '查看详情',
                        sidebar: false,
                        activeMenu: '/student_job_manage',
                        cache: true,
                        noCache: 'taskManageList'
                    }
                }
            ]
        }
    ]
}
