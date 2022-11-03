import dayjs from 'dayjs'

let detailTable = {
    columns: [
        {
            prop: 'jobName',
            label: '作业名称',
        },
        {
            prop: 'CourseName',
            label: '课程名'
        },
        {
            prop: 'teacherClass',
            label: '教学班级',
            sortable: true
        },
        {
            prop: 'jobStartTime',
            label: '发布时间',
            sortable: true,
            width: '180px',
            formatter: (row, column, cellValue) => dayjs(cellValue*1000).format('YYYY-MM-DD HH:mm:ss')
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
