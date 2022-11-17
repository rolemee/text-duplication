<route>
{
    name: 'jobManageList',
    meta: {
        title: "作业管理"
    }
}
</route>
<script setup name="JobManageList">
import detailTable from "./detailTable"
import detailForm from "./detailForm"
import FormMode from './components/FormMode/index.vue'
import api from "@/api"

const router = useRouter()

import useUserStore from "@/store/modules/user"
const userStore = useUserStore()

let formDetail = ref(detailForm.view.form)
const data = ref({
    loading: false,
    //表格
    detailTable: detailTable,
    tableData: [],
    //搜索
    search: {
        detailForm:[
            {
                name: 'CourseName',
                label: '作业描述',
            },
            {
                name: 'jobName',
                label: '作业名称'
            },
            {
                name: 'jobType',
                label: '作业类型',
                type: 'select',
                loadingText: '加载类型....'
            }
        ],
        rules: null,
        datePick: true
    },
    options: {
        'jobType': []
    },
    searchData: {
        searchTime: {},
        searchString: {}
    },
    //form
    /**
     * 详情展示模式
     * dialog 对话框
     * drawer 抽屉
     */
    formMode: 'dialog',
    //详情
    formModeProps: {
        visible: false,
        data: formDetail,//详细
        title: '',
        disabled: false,
        type: '',
        id: ''
    },
})

onMounted(() => {
    getList()
})

function getList() {
    api.post('/getHomeworkList',{
        usernameId: userStore.userId
    }).then(res => {
        data.value.tableData = []
        console.log(res.data)
        // console.log(res.data.lenght)
        // console.log(new Date(res.data.start_time).getTime() / 1000)
        for (let i = 0; i < res.data.length; i++) {
            data.value.tableData.push({
                'jobName': res.data[i]['homeworkName'],
                'CourseName': res.data[i]['homeworkDescribe'],
                'teacherClass': res.data[i]['teacher_name'],
                'jobRemarks': '无',
                'jobStartTime': res.data[i]['start_time'],
                'jobEndTime': new Date(res.data.stop_time).getTime() / 1000,
                'color': 'color: red',
                'completeRatio': res.data[i]['completeness'],
                'homeworkType': res.data[i]['homework_type'],
                'homeworkId': res.data[i]['homeworkId']
            })
            console.log(data.value.tableData)
        }

    })
    data.value.options['jobType'].push({
        name: 'code',
        value: '编程'
    })
}

// 搜索栏
// 搜索
function handleSearch(val, callback) {
    data.value.searchData.searchString = {}
    data.value.searchData.searchTime = {}
    // console.log(val)
    if (val.hasOwnProperty('startTime')) {
        data.value.searchData.searchTime['startTime'] = new Date(val.startTime).getTime()/1000
        data.value.searchData.searchTime['endTime'] = new Date(val.endTime).getTime()/1000
    }
    if (val.CourseName || val.jobName || val.jobType ){
        data.value.searchData.searchString = {
            CourseName: val.CourseName,
            jobName: val.jobName,
            jobType: val.jobType
        }
    }
    getList()
    callback && callback()
}

// table操作
function handleView(val) {
    console.log(val.homeworkId)
    router.push({
        name: 'taskManageList',
        params: {
            workId: val.homeworkId,
            workType: val.homeworkType
        }
    })
}
function handleEdit(val) {
    // console.log(val)
    console.log('编辑')
    data.value.formModeProps.title = val.jobName
    data.value.formModeProps.id = val.id
    data.value.formModeProps.type = 'edit'
    formDetail.value = JSON.parse(JSON.stringify(detailForm.edit.form))
    data.value.formModeProps.disabled = true
    data.value.formModeProps.visible = true
}

</script>

<template>
    <div>
        <page-header title="学生作业管理模块" />
        <page-main v-loading="data.loading">
            <TopSearch :search="data.search" :options="data.options" @handleSearch="handleSearch" />
            <DetailTable
                :columns="data.detailTable.columns"
                :tableData="data.tableData"
                :option="data.detailTable.option"
                @handleView="handleView"
                @handleEdit="handleEdit"
            />
        </page-main>
        <FormMode
            v-if="['dialog', 'drawer'].includes(data.formMode)"
            :id="data.formModeProps.id"
            :title="data.formModeProps.title"
            :type="data.formModeProps.type"
            :disabled="data.formModeProps.disabled"
            :data="data.formModeProps.data"
            v-model="data.formModeProps.visible"
            :mode="data.formMode"
            @update:modelValue="val => data.formModeProps.visible = val"
        />
    </div>
</template>
<style scoped lang="scss">
//scss
</style>
