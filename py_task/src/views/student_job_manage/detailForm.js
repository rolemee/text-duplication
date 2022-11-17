let detailForm = {
    view: {
        form: [
            {
                label: '作业名称',
                name: 'jobName'
            },
            {
                prop: 'jobType',
                label: '作业类型'
            },
            {
                label: '作业描述',
                name: 'CourseName'
            },
            // {
            //     label: '备注',
            //     name: 'jobRemarks'
            // },
            {
                label: '发布时间',
                name: 'jobStartTime',
                type: 'picker'
            },
            {
                label: '截止时间',
                name: 'jobEndTime',
                type: 'picker'
            },
            {
                label: '作业详情',
                name: 'detailFile',
                type: 'link',
                link: {
                    src: '',
                    name: ''
                }
            }
        ]
    },
    edit: {
        form: [
            {
                label: '作业名称',
                name: 'jobName'
            },
            {
                prop: 'jobType',
                label: '作业类型'
            },
            {
                label: '作业描述',
                name: 'CourseName'
            },
            // {
            //     label: '备注',
            //     name: 'jobRemarks'
            // },
            {
                label: '截止时间',
                name: 'jobEndTime',
                type: 'picker'
            },
            {
                prop: 'teacherClass',
                label: '老师',
                sortable: true
            },
            {
                label: '详情提交',
                type: 'upload'
            }
        ]
    }
}

export default detailForm
