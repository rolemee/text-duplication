<route>
{
    name: 'jobManageList',
    meta: {
        title: "作业管理"
    }
}
</route>
<script setup name="JobManageList">
import detailTable from "@/views/job_manage/detailTable"
import detailForm from "@/views/job_manage/detailForm"
import FormMode from './components/FormMode/index.vue'
import api from "@/api"

import useUserStore from '@/store/modules/user'
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
                label: '课程名',
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
        id: '',
        uploadData: {
            data: {
                'token': userStore.token || '',
            }
        }
    },
})

onMounted(() => {
    getList()
})

function getList() {
    api.post('/getHomeworkList',{
        usernameId: userStore.userId
    }).then(res => {
        // console.log(res.data)
        data.value.tableData = [
            {
                'jobName': res.data.homeworkName,
                'jobType': 'code',
                'jobTeacher': '蒋师傅',
                'CourseName': '网络攻防',
                'jobRemarks': '无',
                'jobStartTime': new Date(res.data.start_time).getTime() / 1000,
                'jobEndTime': new Date(res.data.stop_time).getTime()/1000,
                'status': '未完成',
                'color': 'color: red',
                'homeworkType': res.data.homework_type,
                'homeworkId': res.data.homeworkId,
                'id': userStore.userId
            }
        ]
    })
    data.value.options['jobType'].push({
        name: 'code',
        value: '编程'
    })
}

//搜索栏
//下拉表
function remoteMethod() {}
function onChange() {}
//搜索
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

//table操作
function handleView(val) {
    // console.log(val)
    data.value.formModeProps.title = val.jobName
    data.value.formModeProps.id = val.id
    data.value.formModeProps.type = 'view'
    formDetail.value = JSON.parse(JSON.stringify(detailForm.view.form))
    formDetail.value[formDetail.value.length-1]['link'] = {//获取链接
        src: 'https://ctf.show/',
        name: 'ctf'
    }
    data.value.formModeProps.disabled = true
    data.value.formModeProps.visible = true
}
function handleEdit(val) {
    // console.log(val)
    console.log('编辑')
    data.value.formModeProps.title = val.jobName
    data.value.formModeProps.id = val.id
    data.value.formModeProps.type = 'edit'
    data.value.formModeProps.uploadData.data['homeworkId'] = val.homeworkId
    formDetail.value = JSON.parse(JSON.stringify(detailForm.submit.form))
    data.value.formModeProps.disabled = true
    data.value.formModeProps.visible = true
}

//弹窗
function getDataList() {}
</script>

<template>
    <div>
        <page-header title="作业管理模块" />
        <page-main v-loading="data.loading">
            <TopSearch :search="data.search" :options="data.options" @handleSearch="handleSearch" @remoteMethod="remoteMethod" @onChange="onChange"/>
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
            :uploadData="data.formModeProps.uploadData.data"
            v-model="data.formModeProps.visible"
            :mode="data.formMode"
            @success="getDataList"
            @update:modelValue="val => data.formModeProps.visible = val"
        />
    </div>
</template>
<style scoped lang="scss">
//scss
</style>
