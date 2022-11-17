<script setup name="DuplicateCheckingIndex">
import api from '@/api'
import useUserStore from '@/store/modules/user'
import { ElMessage } from 'element-plus'
const userStore = useUserStore()

// const route = useRoute()
const router = useRouter()

const ext = [ 'c', 'cpp', 'java', 'py', 'word', 'go', 'rs', 'txt', 'asm']
const data = ref({
    loading: false,
    uploadData: {
        token: userStore.token || '',
        homeworkId: 0
    },
    cacheHomeworkId: 0,
    uploadUrl: 'http://121.5.161.87:8888/upload',
    uploadType: {
        first: '',
        second: ''
    },
    filePath: {
        first: '',
        second: ''
    },
    fileList: {
        first: [],
        second: []
    },
    uploadName: '',
    uploadStatus: {
        first: true,
        second: true
    },
    uploadFiles: [],
    showResult: false,
    hasResult: false,
    // table表格
    tableData: [],
    columns: [
        {
            prop: 'id1',
            label: '文件1'
        },
        {
            prop: 'id2',
            label: '文件2'
        },
        {
            prop: 'similarity',
            label: '重复率'
        }
    ],
    option: {
        stripe: true,
        fit: true,
        border: true,
        pagination: false,
        operation: false
    },
    detailLoading: false
})
onMounted(() => {
    data.value.uploadData.homeworkId = new Date().getTime()
})

const fileFirst = ref()
const fileSecond = ref()

function onChange(file, fileList) {
    console.log(file)
    console.log(fileList)
    if (data.value.uploadFiles.length === 2) {
        // console.log(data.value.uploadData.homeworkId)
        data.value.uploadFiles = []
        if (data.value.uploadStatus.first && data.value.uploadStatus.second) {
            if (data.value.uploadType.first === 'cpp') {
                data.value.uploadType.second = data.value.uploadType.first = 'c++'
            }
            data.value.detailLoading = true
            data.value.showResult = true
            api.post('/checkAllHomework', {
                homeworkId: data.value.uploadData.homeworkId,
                filetype: data.value.uploadType.first
            }).then(res => {
                data.value.tableData = res.data
                data.value.detailLoading = false
            }).catch(() => {
                data.value.detailLoading = false
            })
            data.value.hasResult = true
            data.value.cacheHomeworkId = data.value.uploadData.homeworkId
        }
        data.value.uploadStatus = {
            first: true,
            second: true
        }
        data.value.loading = false
        data.value.uploadData.homeworkId = new Date().getTime()
        // console.log(data.value.cacheHomeworkId)
    } else {
        if (fileList.length > 1) {
            fileList.shift()
        }
        const fileName = file.name.split('.')
        const fileExt = fileName[fileName.length - 1]
        const isTypeOk = ext.indexOf(fileExt) !== -1
        if (!isTypeOk) {
            ElMessage.error(`文件上传只支持${ ext.join('/') }格式`)
        } else {
            if (data.value.uploadName === 'first') {
                // console.log(data.value.fileList.first)
                data.value.uploadType.first = fileExt
                data.value.filePath.first = document.getElementsByClassName('el-upload__input')[0].value
            } else if (data.value.uploadName === 'second') {
                // console.log(data.value.fileList.second)
                data.value.uploadType.second = fileExt
                data.value.filePath.second = document.getElementsByClassName('el-upload__input')[1].value
                console.log(data.value.filePath.second)
            }
            // console.log(fileExt)
        }
    }
}

function handleSuccess(res, type) {
    console.log('提交成功', type)
    console.log(data.value.uploadData.homeworkId)
    console.log(res)
    data.value.uploadName = ''
    data.value.uploadFiles.push(type)
    if (res.error !== '') {
        ElMessage.error(res.error)
        if (type === 'first') {
            data.value.fileList.first.forEach(item => {
                fileFirst.value.handleRemove(item)
            })
            data.value.filePath.first = ''
        } else {
            data.value.fileList.second.forEach(item => {
                fileSecond.value.handleRemove(item)
            })
            data.value.filePath.second = ''
        }
        data.value.uploadStatus[type] = false
    } else {
        ElMessage.success('上传成功')
        console.log(data.value.filePath.second)
        data.value.uploadStatus[type] = true
    }
}

function onSubmit() {
    if (!data.value.filePath.first && !data.value.filePath.second) {
        ElMessage.error('必须上传两个文件')
    } else if (data.value.uploadType.first !== data.value.uploadType.second) {
        if (!document.getElementsByClassName('el-upload__input')[1].value || !document.getElementsByClassName('el-upload__input')[0].value) {
            ElMessage.error('重新对比必须再次提交两个文件')
        } else
            ElMessage.error('两个文件必须是统一个文件类型,eg: 1.cpp 2.cpp')
    } else {
        data.value.loading = true
        fileFirst.value.submit()
        fileSecond.value.submit()
    }
}

function onCancel() {
    data.value.filePath.first = ''
    data.value.filePath.second = ''
    data.value.fileList.first.forEach(item => {
        fileFirst.value.handleRemove(item)
    })
    data.value.fileList.second.forEach(item => {
        fileSecond.value.handleRemove(item)
    })
}

function handleClick(val) {
    router.push({
        name: 'duplicateDetailMatch',
        params: {
            homeworkId: data.value.cacheHomeworkId,
            homeworkType: data.value.uploadType.first,
            leftName: val.id1,
            rightName: val.id2,
            type: 'onlyDuplicate'
        }
    })
    data.value.showResult = false
}
</script>

<template>
    <div>
        <page-header title="文件对比模块" />
        <page-main v-loading="data.loading">
            <div>
                <div class="tip">
                    第一组文件夹：
                </div>
                <div class="fileUpload">
                    <el-input v-model="data.filePath.first" disabled placeholder="请输入地址" style="width: 92%" />
                    <el-upload
                        ref="fileFirst"
                        :action="data.uploadUrl"
                        :data="data.uploadData"
                        :file-list="data.fileList.first"
                        :show-file-list="false"
                        :on-change="onChange"
                        :on-success="res => handleSuccess(res, 'first')"
                        :auto-upload="false"
                        class="upload"
                    >
                        <el-button type="primary" plain @click="data.uploadName = 'first'">选择文件</el-button>
                    </el-upload>
                </div>
                <div style="border-bottom: #CDD0D6 1px dashed ;margin: 20px 0 15px 0" />
                <div class="tip">第二组文件夹：</div>
                <div class="fileUpload">
                    <el-input v-model="data.filePath.second" disabled placeholder="请输入地址" style="width: 92%" />
                    <el-upload
                        ref="fileSecond"
                        :action="data.uploadUrl"
                        :data="data.uploadData"
                        :file-list="data.fileList.second"
                        :show-file-list="false"
                        :on-change="onChange"
                        :on-success="res => handleSuccess(res, 'second')"
                        :auto-upload="false"
                        class="upload"
                    >
                        <el-button type="primary" plain @click="data.uploadName = 'second'">选择文件</el-button>
                    </el-upload>
                </div>
            </div>
            <div style="border-bottom: #CDD0D6 1px dashed ;margin: 20px 0 15px 0" />
            <div style="display: flex; justify-content: flex-end;margin-right: 10px">
                <el-button
                    v-if="data.hasResult"
                    text
                    type="primary"
                    style="position:absolute;left: 0;"
                    @click="data.showResult = true"
                >
                    查看结果
                </el-button>
                <el-button type="primary" plain @click="onSubmit">确 定</el-button>
                <el-button @click="onCancel">取 消</el-button>
            </div>
            <div class="endTip">
                注意：一次上传要上传两个同类型的文件，且只能上传两个；上传一次后再次对比需要再提供两个文件
            </div>
        </page-main>
        <div v-loading="data.detailLoading">
            <el-dialog
                v-model="data.showResult"
                draggable title="查重结果"
                width="600px"
                :close-on-click-modal="false"
                append-to-body
                destroy-on-close
            >
                <DetailTable
                    :table-data="data.tableData"
                    :columns="data.columns"
                    :option="data.option"
                    @handleClick="handleClick"
                />
            </el-dialog>
        </div>
    </div>
</template>

<style lang="scss" scoped>
// scss
:deep(.fileUpload) {
    display: flex;
    justify-content: space-between;
    margin-bottom: 10px;
    .upload {
        width: 8%;
        margin-left: 5px;
    }
}
:deep(.tip) {
    margin-bottom: 10px;
    font-size: 16px;
    color: #303133;
    font-weight: 540;
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
}
:deep(.endTip) {
    font-size: 12px;
    color: #C0C4CC;
    font-weight: 540;
    position: absolute;
    text-align: center;
}
</style>
