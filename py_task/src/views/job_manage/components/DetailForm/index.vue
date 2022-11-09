<template>
    <div v-loading="data.loading">
        <el-form
            :model="data.form"
            :rules="myRule"
            label-suffix=":"
            label-width="100px"
        >
            <template v-for="(item,index) in props.data" :key="index" >
                <el-form-item :label="item.label" :prop="item.name">
                    <el-date-picker
                        v-if="item.type === 'picker'"
                        size="default"
                        v-model="data.form[item.name]"
                        type="datetime"
                        :disabled="props.disabled"
                        :default-value="new Date(new Date().getFullYear(),new Date().getMonth(),new Date().getDay())"
                        clearable
                    />
                    <template v-else-if="item.type === 'link'">
                        <svg-icon name="ep:money" style="margin-right: 10px"/>
                        <el-link :href="item.link.src" type="primary" target="_blank">{{item.link.name}}</el-link>
                    </template>
                    <template v-else-if="item.type === 'upload'">
                        <el-upload
                            drag
                            ref="fileList"
                            :action="item.uploadUrl"
                            :data="props.uploadData"
                            :file-list="data.fileList"
                            class="upload"
                            :on-success="onSuccess"
                            :before-upload="beforeUpload"
                            :on-change="handleChange"
                        >
                            <el-button type="primary" text>
                                上传文件
                            </el-button>
                        </el-upload>
                    </template>
                    <el-input
                        v-else
                        v-model="data.form[item.name]"
                        :placeholder="item.placeholder"
                        :disabled="props.disabled"
                        clearable
                    />
                </el-form-item>
            </template>
        </el-form>
    </div>
</template>

<script setup>
import {ElMessage} from "element-plus"
import api from "@/api";

const props = defineProps({
    data: {
        type: Array,
        default: []
    },
    rules: {
        type: Object,
        default: {}
    },
    disabled: {
        type: Boolean,
        default: false
    },
    type: {
        type: String,
        default: null
    },
    id: {
        type: [Number, String],
        default: null
    },
    uploadData: {
        type: Object,
        default: {}
    },
    ext: {
        type: Array,
        default: [ 'c', 'cpp', 'java', 'py', 'word']
    }
})

const fileList = ref()
const data = ref({
    loading: false,
    form: {},
    fileList: [],
    cacheFile: []
})
const myVisible = ref(false)

const myRule = computed({
    get:function(){
        return props.rules
    }
})

onMounted(() => {
    console.log(JSON.stringify(props.uploadData))
    getForm();
})

//初始化数据
function getForm(){//通过id获取数据
    data.value.loading = true
    api.post('/getHomeworkList',{
        usernameId: props.id
    }).then(res => {
        data.value.form = {
            'jobName': res.data.homeworkName,
            'jobType': 'code',
            'jobTeacher': '蒋师傅',
            'CourseName': '网络攻防',
            'jobRemarks': '无',
            'jobStartTime': new Date(res.data.start_time).getTime() / 1000,
            'jobEndTime': new Date(res.data.stop_time).getTime() / 1000,
            'homeworkType': res.data.homework_type,
            'homeworkId': res.data.homeworkId
        }
        data.value.loading = false
    }).catch(() => {
        data.value.loading = false
    })
}

// //上传操作
// import api from '@/api/index'
// function handleUpload(file) {
//     console.log(file)
//     console.log(file.action)
//     api.post(file.action, {
//         file: file.file
//     }).then(res => {
//         console.log(res)
//     })
// }

function onSuccess(res) {
    if (res.error !== '') {
        ElMessage.error(res.error)
        if (Object.keys(data.value.cacheFile).length !== 0)
            data.value.fileList = JSON.parse(JSON.stringify(data.value.cacheFile))
        else
            data.value.fileList = []
    }else {
        ElMessage.success("上传成功")
    }
}

function beforeUpload(file) {
    console.log(file.name.split('.'))
    const fileName = file.name.split('.')
    const fileExt = fileName[fileName.length - 1]
    const isTypeOk = props.ext.indexOf(fileExt) !== -1
    if (!isTypeOk) {
        ElMessage.error(`文件上传只支持${ props.ext.join('/') }格式`)
        data.value.fileList.pop()
    }
}

function handleChange(file,fileList) {
    if (fileList.length > 1) {
        data.value.cacheFile = [fileList[0]]
        data.value.fileList = [file]
    }
}
</script>

<style lang="scss" scoped>
.upload-video :deep {
    margin: 0;
    .el-upload-dragger {
        padding: 0;
        border: none;
    }
}
.upload :deep{
    margin: 0;
    .el-upload-dragger {
        padding: 0;
        border: none;
    }
}
</style>
