import dayjs from 'dayjs'

let detailTable = {
    columns: [
        {
            prop: 'jobName',
            label: '作业名称',
        },
        {
            prop: 'jobType',
            label: '作业类型'
        },
        {
            prop: 'jobTeacher',
            label: '教师名称'
        },
        {
            prop: 'CourseName',
            label: '作业描述'
        },
        {
            prop: 'jobStartTime',
            label: '发布时间',
            sortable: true,
            width: '180px'
        },
        {
            prop: 'jobEndTime',
            label: '截止时间',
            sortable: true,
            width: '180px'
        },
        {
            prop: 'status',
            label: '完成状态',
            icon: 'ep:compass',
            sortable: true,
            iconText: true
        }
    ],
    option: {
        controlSize: "default",
        stripe: true,
        fit: true,
        isSelected: false,
        pagination: true,
        border: true,
        operation: true,
        dropdown: false,
        edit: true,
        view: true,
        operate: {
            edit: '提交',
            width: '180px'
        },
        getDataType: 'static'
    }
}
export default detailTable
