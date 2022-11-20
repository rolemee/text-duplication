let detailForm = {
    view: {
        form: [
            {
                label: '作业名称',
                name: 'jobName'
            },
            {
                label: '作业描述',
                name: 'CourseName'
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
                label: '作业描述',
                name: 'CourseName'
            },
            {
                label: '提交',
                type: 'upload',
                uploadUrl: 'http://121.5.161.87:8888/upload'
            }
        ]
    }
}

export default detailForm
