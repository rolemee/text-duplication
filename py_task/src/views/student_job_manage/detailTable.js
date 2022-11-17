import dayjs from 'dayjs'

let detailTable = {
    columns: [
        {
            prop: 'jobName',
            label: '作业名称',
        },
        {
            prop: 'CourseName',
            label: '作业描述'
        },
        {
            prop: 'teacherClass',
            label: '老师',
            sortable: true
        },
        {
            prop: 'jobStartTime',
            label: '发布时间',
            sortable: true,
            width: '180px',
            // formatter: (row, column, cellValue) => dayjs(cellValue*1000).format('YYYY-MM-DD HH:mm:ss')
        },
        {
            prop: 'completeRatio',
            label: '完成比例',
            icon: 'ep:circle-check-filled',
            iconText: true
        }
    ],
    option: {
        controlSize: "default",
        stripe: true,
        fit: true,
        isSelected: true,
        pagination: true,
        border: true,
        operation: true,
        dropdown: false,
        edit: true,
        view: true,
        operate: {
            width: '180px'
        },
        getDataType: 'static'
    }
}
export default detailTable
