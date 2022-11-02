let detailForm = {
    view: {
        form: [
            {
                label: '作业名称',
                name: 'jobName'
            },
            {
                label: '课程名',
                name: 'CourseName'
            },
            {
                label: '备注',
                name: 'jobRemarks'
            },
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
    submit: {
        form: [
            {
                label: '作业名称',
                name: 'jobName'
            },
            {
                label: '课程名',
                name: 'CourseName'
            },
            {
                label: '备注',
                name: 'jobRemarks'
            },
            {
                label: '提交',
                type: 'upload'
            }
        ]
    }
}

export default detailForm
